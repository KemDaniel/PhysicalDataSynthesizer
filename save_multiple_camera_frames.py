import os
import sys
import time
from datetime import datetime, timedelta
import re
import depthai as dai
from multiprocessing import Process
import cv2
import keyboard
import pandas as pd
from rembg import remove
from PIL import Image
import re

start_time = datetime.now() + timedelta(seconds=2) # Waiting time until all Oak D are started (6 secs)
dir_tool = "recording_tool"
dir_data = "data"
dir_result = "results"
date = datetime.today().strftime('%Y-%m-%d')
FPS = 25

def directory_structure():
    product_number = input("Type the product number: ")
    while not (re.search("^([1-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][1-9])$", str(product_number))):
        product_number = input("   >>> Please type a 4 digit number without 0000: ")
    product = input("Type the product: ")

    global dir_product
    global product_name

    dir_product = f"{product_number}"
    product_name = f"{product}"

    parent_dir_data = os.getcwd() + f"\\{dir_tool}" 
    parent_dir_product = os.getcwd() + f"\\{dir_tool}\\{dir_data}" 
    parent_dir_result = os.getcwd() + f"\\{dir_tool}\\{dir_result}"
        
    create_dir_data = os.path.join(parent_dir_data, dir_data)
    create_dir_result = os.path.join(parent_dir_data, dir_result)

    create_dir_data_product = os.path.join(parent_dir_product, dir_product)
    create_dir_data_results= os.path.join(parent_dir_result, dir_product)

    if os.path.exists(create_dir_data):
        print(f"\nDirectory '{dir_data}' exists already.\n")
        if os.path.exists(create_dir_data_product):
            print(f"Directory '{dir_product}' exists already.\n")

            print(">>> Type 'y' if you know that this is already an exisiting product.")       # Security question to prevent data loss
            if input(">>> ") == 'y':
                print("\n>>> You are now taking new pictures of this product.\n")
            else:
                sys.exit()
        else:
            os.mkdir(create_dir_data_product)
            print(f"Directory '{dir_data}/{dir_product}' created.\n")

        if os.path.exists(create_dir_data_results):
            print(f"Directory '{dir_result}' exists already.\n")
        else:
            os.mkdir(create_dir_data_results)
            print(f"Directory '{dir_result}/{dir_product}' created.\n")
    else:
        os.mkdir(create_dir_data)
        print(f"\nDirectory '{dir_data}' created.\n")
        os.mkdir(create_dir_data_product)
        print(f"Directory '{dir_data}/{dir_product}' created.\n")
        if os.path.exists(create_dir_result):
            print(f"Directory '{dir_result}' exists already.\n")
        else:
            os.mkdir(create_dir_result)
            print(f"Directory '{dir_result}' created.\n")
        os.mkdir(create_dir_data_results)
        print(f"Directory '{dir_result}/{dir_product}' created.\n")
        

def save_stream_per_camera(camera_ip, dir_product, product_name):
    # Start defining a pipeline
    pipeline = dai.Pipeline()

    # Define a source - color camera
    cam = pipeline.createColorCamera()
    cam.setBoardSocket(dai.CameraBoardSocket.RGB)
    cam.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    #cam.setImageOrientation(dai.CameraImageOrientation.ROTATE_180_DEG)
    cam.setFps(FPS)

    # Create an encoder, consuming the frames and encoding them using H.265 encoding
    videoEncoder = pipeline.createVideoEncoder()
    videoEncoder.setDefaultProfilePreset(1, dai.VideoEncoderProperties.Profile.MJPEG)
    cam.video.link(videoEncoder.input)

    # Create output
    videoOut = pipeline.create(dai.node.XLinkOut)
    videoOut.setStreamName('rgb')
    cam.video.link(videoOut.input)

    xoutStill = pipeline.create(dai.node.XLinkOut)
    xoutStill.setStreamName("still")
    videoEncoder.bitstream.link(xoutStill.input)

    # Pipeline is defined, now we can connect to the device
    device_info = dai.DeviceInfo()
    device_info.name = camera_ip

    try:
        with dai.Device(pipeline, device_info) as device:
            # Output queue will be used to get the encoded data from the output defined above
            q = device.getOutputQueue(name="rgb", maxSize=FPS, blocking=False)
            qStill = device.getOutputQueue(name="still", maxSize=1, blocking=False)
    
            print(f"{camera_ip} is recording...  ", datetime.now())


            pl = dir_product 
            pl_name = product_name
            pl_frame = {'product number': [pl], 'product name': [pl_name]}
            pl_DF = pd.DataFrame(pl_frame, columns=['product number', 'product name'])

            path_pl = f"{dir_tool}/product_list.csv"

            if not os.path.exists(path_pl):
                pl_DF.to_csv(path_pl, mode='a', header=True, index=False, sep=';')
            else:
                file=pd.read_csv(path_pl)
                if f"{dir_product}" not in file.to_string():
                    pl_DF.to_csv(path_pl, mode='a', header=False, index=False, sep=';')

            first_frame = 1

            while True: 
                if first_frame and start_time <= datetime.now():
                    inRgb = q.tryGet()  # Non-blocking call, will return a new data that has arrived or None otherwise
                    if inRgb is not None:
                        frame = inRgb.getCvFrame()
                        # 4k / 4
                        frame = cv2.pyrDown(frame)
                        frame = cv2.pyrDown(frame)
                        cv2.imshow(f"rgb {camera_ip}", frame)

                    key = cv2.waitKey(1)
                
                    if keyboard.is_pressed('s'):
                        fName = f"{dir_tool}/{dir_data}/{dir_product}/{camera_ip}.png"
                        with open(fName, "wb") as f:
                            f.write(qStill.get().getData())
                            print(f'Image saved to', fName)
                            time.sleep(0.25)
                    if keyboard.is_pressed('q'):
                        break
    except Exception as e:
        print(f"ERROR On {camera_ip} : {e}")
                    
            
                   
if __name__ == "__main__":
    threads_stream = []
    threads_convert = []
   
    directory_structure()

    device_infos = dai.Device.getAllAvailableDevices()
    print("Found", len(device_infos), "devices")

    ips = ["169.254.1.223", "169.254.1.224","169.254.1.225","169.254.1.226", "169.254.1.227", "169.254.1.228"]
    
    for ip in ips:
        #camera_ip = device_info.name

        threads_stream.append(Process(target=save_stream_per_camera, args=[ip, dir_product, product_name]))
        
    for thread in threads_stream:
        thread.start()
        time.sleep(0.1)
       
    time.sleep(5)
    print('\nPress "s" to save pictures.')
    print('\nType in "r" to remove the background.\n')
    if input("") == 'r':
        
        path1 = f"{dir_tool}/{dir_data}/{dir_product}/169.254.1.223.png"
        path2 = f"{dir_tool}/{dir_data}/{dir_product}/169.254.1.224.png"
        path3 = f"{dir_tool}/{dir_data}/{dir_product}/169.254.1.225.png"
        path4 = f"{dir_tool}/{dir_data}/{dir_product}/169.254.1.226.png"
        path5 = f"{dir_tool}/{dir_data}/{dir_product}/169.254.1.227.png"
        path6 = f"{dir_tool}/{dir_data}/{dir_product}/169.254.1.228.png"

        outputPath1 = f"{dir_tool}/{dir_result}/{dir_product}/223.png"
        outputPath2 = f"{dir_tool}/{dir_result}/{dir_product}/224.png"
        outputPath3 = f"{dir_tool}/{dir_result}/{dir_product}/225.png"
        outputPath4 = f"{dir_tool}/{dir_result}/{dir_product}/226.png"
        outputPath5 = f"{dir_tool}/{dir_result}/{dir_product}/227.png"
        outputPath6 = f"{dir_tool}/{dir_result}/{dir_product}/228.png"

        input1 = Image.open(path1)
        input2 = Image.open(path2)
        input3 = Image.open(path3)
        input4 = Image.open(path4)
        input5 = Image.open(path5)
        input6 = Image.open(path6)

        output1 = remove(input1)
        output2 = remove(input2)
        output3 = remove(input3)
        output4 = remove(input4)
        output5 = remove(input5)
        output6 = remove(input6)

        # output1.getbbox()
        # output2.getbbox()
        # output3.getbbox()
        # output4.getbbox()
        # output5.getbbox()
        # output6.getbbox()

        op1 = output1.crop(output1.getbbox())
        op2 = output2.crop(output2.getbbox())
        op3 = output3.crop(output3.getbbox())
        op4 = output4.crop(output4.getbbox())
        op5 = output5.crop(output5.getbbox())
        op6 = output6.crop(output6.getbbox())


        op1.save(outputPath1)
        op2.save(outputPath2)
        op3.save(outputPath3)
        op4.save(outputPath4)
        op5.save(outputPath5)
        op6.save(outputPath6)

        print('\nThe Background is removed.\n\nPress "q" to end the script.')

