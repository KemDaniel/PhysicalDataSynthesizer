from PIL import Image
import random
import os
import re
import glob
from natsort import natsorted
import datetime

dir_tool = "recording_tool"
dir_mp = "manipulated_images"
dir_all_vid = "videos"
dir_vid = "vid"
dir_vid1 = "vid1"
dir_vid2 = "vid2"
dir_vid3 = "vid3"
cam1 = "223"
cam2 = "224"
cam3 = "225"
cam4 = "226"
cam5 = "227"
cam6 = "228"
bg_count = 0

product_list = ["0700", "0701", "0702", "0703", "0704", "0705", "0706", "0707", "0708", "0709", "0710",
                "0720", "0721", "0722", "0723", "0724", "0725", "0726", "0727", "0728", "0729", "0730",]
vid_list = ["vid", "vid1", "vid2", "vid3"]
used_vid = []
cam_list = [cam1, cam2, cam3, cam4, cam5, cam6]
current_time = str(datetime.datetime.now().strftime("%H_%M"))

n_products = input("Tippe die Anzahl an Produkten ein: ")
vid_number = input("Tippe die Anzahl an Videos ein: ")

parent_dir_mp = os.getcwd() + f"\\{dir_tool}" 
create_dir_mp = os.path.join(parent_dir_mp, dir_mp)

# add new videos here and create it 
create_dir_vid = os.path.join(create_dir_mp, dir_vid)
create_dir_vid1 = os.path.join(create_dir_mp, dir_vid1)
create_dir_vid2 = os.path.join(create_dir_mp, dir_vid2)
create_dir_vid3 = os.path.join(create_dir_mp, dir_vid3)

vid_product_number = os.path.join(create_dir_vid, n_products + "_" + current_time)

cam1_vid = os.path.join(vid_product_number, cam1)
cam2_vid = os.path.join(vid_product_number, cam2)
cam3_vid = os.path.join(vid_product_number, cam3)
cam4_vid = os.path.join(vid_product_number, cam4)
cam5_vid = os.path.join(vid_product_number, cam5)
cam6_vid = os.path.join(vid_product_number, cam6)


if os.path.exists(create_dir_mp):
    print(f"\nDirectory '{dir_mp}' exists already.\n")
else:
    os.mkdir(create_dir_mp)
    print(f"\nDirectory '{dir_mp}' created.\n")     

if not os.path.exists(create_dir_vid):
    os.mkdir(create_dir_vid)

if not os.path.exists(create_dir_vid1):
    os.mkdir(create_dir_vid1)

if not os.path.exists(create_dir_vid2):
    os.mkdir(create_dir_vid2)

if not os.path.exists(create_dir_vid3):
    os.mkdir(create_dir_vid3)


if not os.path.exists(vid_product_number):
    os.mkdir(vid_product_number)

if not os.path.exists(cam1_vid):
    os.mkdir(cam1_vid)

if not os.path.exists(cam2_vid):
    os.mkdir(cam2_vid)

if not os.path.exists(cam3_vid):
    os.mkdir(cam3_vid)

if not os.path.exists(cam4_vid):
    os.mkdir(cam4_vid)

if not os.path.exists(cam5_vid):
    os.mkdir(cam5_vid)

if not os.path.exists(cam6_vid):
    os.mkdir(cam6_vid)


for n in range(2):
    random_product = random.choice(product_list)

    product_number = random_product
    count = 0
   
    if n == 0:
        for i in range(int(vid_number)):
            random_video = random.choice(vid_list)

            if random_video in used_vid:
                while random_video in used_vid:
                    random_video = random.choice(vid_list)
                used_vid.append(random_video)
            else:
                used_vid.append(random_video)

            print(random_video)
            BGPath = glob.glob(f'{parent_dir_mp}/{dir_all_vid}/{random_video}/frames/*png')
            sortedBGPath = natsorted(BGPath)
            for video_frame in sortedBGPath:
                
                inPath = f'{parent_dir_mp}/results/{product_number}'
                framePath = video_frame

                for imagePath in os.listdir(inPath):
                    inputPath = os.path.join(inPath, imagePath)
                    cam_nb = imagePath.split(".")

                    img = Image.open(inputPath)
                    imgBG = Image.open(framePath).convert("RGBA")

                    random_rotate = random.randrange(0, 360)
                    random_x = random.randrange(129, 720)
                    if random_x > 500:
                        random_y = random.randrange(510, 720) 
                        if cam_nb[0] == "224" or cam_nb[0] == "225" or cam_nb[0] == "226":
                            random_size = round(random.uniform(0.5, 0.55),2)
                        else:
                            random_size = round(random.uniform(0.3, 0.35),2)
                    else:
                        random_y = random.randrange(400, 720)
                        if cam_nb[0] == "224" or cam_nb[0] == "225" or cam_nb[0] == "226":
                            random_size = round(random.uniform(0.65, 0.7),2)
                        else:
                            random_size = round(random.uniform(0.4, 0.5),2)

                    if cam1 in inputPath:
                        outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam1}'
                    elif cam2 in inputPath:
                        outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam2}'
                    elif cam3 in inputPath:
                        outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam3}'
                    elif cam4 in inputPath:
                        outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam4}'
                    elif cam5 in inputPath:
                        outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam5}'
                    elif cam6 in inputPath:
                        outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam6}'
                    
                    fullOutPath = os.path.join(outPath,f"{n}_%d_{imagePath}" % count)

                    img_resized = img.resize((round(img.size[0]*random_size), round(img.size[1]*random_size))) 
                    img_rotated = img_resized.rotate(random_rotate, expand=True)

                    cropped_img_rotated = img_rotated.crop(img_rotated.getbbox())
                    width, height = cropped_img_rotated.size
                    x_center = (width/2) + random_x
                    y_center = (height/2) + random_y
                    val1 = round(x_center/1920, 4)
                    val2 = round(y_center/1440, 4)
                    val3 = round(width/1920, 4)
                    val4 = round(height/1440, 4)

                    val1 = format(val1, '.4f')
                    val2 = format(val2, '.4f')
                    val3 = format(val3, '.4f')
                    val4 = format(val4, '.4f')

                    cam = imagePath.split(".")

                    with open(f"{outPath}/{n}_%d_{cam[0]}.txt" % count, "a") as f:
                        f.write(f"1 {val1} {val2} {val3} {val4}\n")

                    imgBG.paste(cropped_img_rotated, (random_x,random_y), mask = cropped_img_rotated)

                    imgBG.save(fullOutPath)
                    
                count += 1
    else:
        for cam_number in cam_list:

            BGPath = glob.glob(f'{parent_dir_mp}/{dir_mp}/vid/{n_products}_{current_time}/{cam_number}/*png')

            inPath = f'{parent_dir_mp}/results/{product_number}'

            count = 0
            sortedBGPath = natsorted(BGPath)

            for video_frame in sortedBGPath:
                framePath = video_frame

                for imagePath in os.listdir(inPath):
                    if cam_number in imagePath:
                        
                        for p in range(int(n_products)-1):
                            random_product = random.choice(product_list)

                            product_number = random_product

                            inPath = f'{parent_dir_mp}/results/{product_number}'

                            inputPath = os.path.join(inPath, imagePath)

                            img = Image.open(inputPath)
                            if bg_count == 0:
                                imgBG = Image.open(framePath).convert("RGBA")
                                bg_count += 1
                            cam_nb = imagePath.split(".")

                            random_rotate = random.randrange(0, 360)
                            random_x = random.randrange(129, 720)
                            if random_x > 500:
                                random_y = random.randrange(510, 720) 
                                if cam_nb[0] == "224" or cam_nb[0] == "225" or cam_nb[0] == "226":
                                    random_size = round(random.uniform(0.5, 0.55),2)
                                else:
                                    random_size = round(random.uniform(0.3, 0.35),2)
                            else:
                                random_y = random.randrange(400, 720)
                                if cam_nb[0] == "224" or cam_nb[0] == "225" or cam_nb[0] == "226":
                                    random_size = round(random.uniform(0.65, 0.7),2)
                                else:
                                    random_size = round(random.uniform(0.4, 0.5),2)
                            
                            if cam1 in inputPath:
                                outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam1}'
                            elif cam2 in inputPath:
                                outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam2}'
                            elif cam3 in inputPath:
                                outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam3}'
                            elif cam4 in inputPath:
                                outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam4}'
                            elif cam5 in inputPath:
                                outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam5}'
                            elif cam6 in inputPath:
                                outPath = f'{dir_tool}/{dir_mp}/vid/{n_products + "_" + current_time}/{cam6}'
                            
                            fullOutPath = os.path.join(outPath,f"0_%d_{imagePath}" % count)

                            img_resized = img.resize((round(img.size[0]*random_size), round(img.size[1]*random_size))) 
                            img_rotated = img_resized.rotate(random_rotate, expand=True)

                            cropped_img_rotated = img_rotated.crop(img_rotated.getbbox())
                            width, height = cropped_img_rotated.size
                            x_center = (width/2) + random_x
                            y_center = (height/2) + random_y
                            val1 = round(x_center/1920, 4)
                            val2 = round(y_center/1440, 4)
                            val3 = round(width/1920, 4)
                            val4 = round(height/1440, 4)

                            val1 = format(val1, '.4f')
                            val2 = format(val2, '.4f')
                            val3 = format(val3, '.4f')
                            val4 = format(val4, '.4f')

                            cam = imagePath.split(".")
                            with open(f"{outPath}/0_%d_{cam[0]}.txt" % count, "a") as f:
                                f.write(f"1 {val1} {val2} {val3} {val4}\n")

                            imgBG.paste(cropped_img_rotated, (random_x,random_y), mask = cropped_img_rotated)

                        imgBG.save(fullOutPath)
                        bg_count = 0
                count += 1

