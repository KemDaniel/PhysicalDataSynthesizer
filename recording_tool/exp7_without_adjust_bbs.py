from PIL import Image, ImageFilter, ImageEnhance
import random
import os
import glob
from natsort import natsorted
import datetime
import numpy as np
import copy
from timm.data.random_erasing import RandomErasing
from torchvision import transforms

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
count = 0
dataset = "origin"

# real products
#product_list = ["0700", "0701", "0702", "0703", "0704", "0705", "0706", "0707", "0708", "0709", "0710",
#                "0720", "0721", "0722", "0723", "0724", "0725", "0726", "0727", "0728", "0729", "0730",
#                "0740", "0741", "0742", "0743", "0744", "0745", "0746", "0747", "0748", "0749",
#                "0750", "0751", "0752", "0753", "0754", "0755", "0756", "0757", "0758", "0759", 
#                "0760", "0761", "0762", "0763", "0764", "0765", "0766", "0767", "0768", "0769",
#                "0770", "0771", "0772", "0773", "0774", "0775", "0776"]
# euroshop products
product_list = ["0600", "0601", "0602", "0603", "0604", "0605", "0606", "0607", "0608", "0609", "0610", 
                "0611", "0612", "0613", "0614", "0615", "0616", "0617", "0618", "0619", "0620", "0621", "0622"]

vid_list = ["vid", "vid1", "vid2", "vid3"] 
used_vid = []
current_time = str(datetime.datetime.now().strftime("%H_%M"))

vid_number = input("Tippe die Anzahl an Videos ein: ")
img_manipulation = True
manipulation = ["origin", "blurred", "noise", "brightness", "colorSpace", "erase"]                                                                                       ## add new manipulation

parent_dir_mp = os.getcwd() + f"\\{dir_tool}" 
create_dir_mp = os.path.join(parent_dir_mp, dir_mp)

def create_directories():
    # add new videos here and create it 
    create_dir_vid = os.path.join(create_dir_mp, dir_vid)
    create_dir_vid1 = os.path.join(create_dir_mp, dir_vid1)
    create_dir_vid2 = os.path.join(create_dir_mp, dir_vid2)
    create_dir_vid3 = os.path.join(create_dir_mp, dir_vid3)

    for x in manipulation:
        if not img_manipulation:
            x = "origin"
        dataset_name = os.path.join(create_dir_vid, x + "_" + current_time)

        cam1_vid = os.path.join(dataset_name, cam1)
        cam2_vid = os.path.join(dataset_name, cam2)
        cam3_vid = os.path.join(dataset_name, cam3)
        cam4_vid = os.path.join(dataset_name, cam4)
        cam5_vid = os.path.join(dataset_name, cam5)
        cam6_vid = os.path.join(dataset_name, cam6)

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

        if not os.path.exists(dataset_name):
            os.mkdir(dataset_name)

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
        

def product_rotation():
    random_rotate = random.randrange(0, 360)
    random_x = random.randrange(129, 720)
    if random_x > 500:
        random_y = random.randrange(510, 720) 
        if cam_nb[0] == "224" or cam_nb[0] == "225" or cam_nb[0] == "226":
            random_size = round(random.uniform(0.5, 0.55),2)
        else:
            random_size = round(random.uniform(0.35, 0.4),2)
    else:
        random_y = random.randrange(400, 720)
        if cam_nb[0] == "224" or cam_nb[0] == "225" or cam_nb[0] == "226":
            random_size = round(random.uniform(0.65, 0.7),2)
        else:
            random_size = round(random.uniform(0.4, 0.5),2)
        
    img_resized = img.resize((round(img.size[0]*random_size), round(img.size[1]*random_size))) 
    img_rotated = img_resized.rotate(random_rotate, expand=True)

    cropped_img_rotated = img_rotated.crop(img_rotated.getbbox())

    return cropped_img_rotated, random_x, random_y


def blur(blurred_list):
    
    ## 80% blurred products

    if random.randint(1,100) > 20:
        blurredImage = cropped_img_rotated.filter(ImageFilter.GaussianBlur(random.randint(1,3)))
    else: 
        blurredImage = cropped_img_rotated

    blurred_list.append(blurredImage)

    return blurred_list


def noise_injection(noise_list):
    noiseImage = cropped_img_rotated.copy()
    noise_img = cropped_img_rotated.convert("RGB")

    ## % of products with noise injection

    if random.randint(1,100) > 20: 
        k = 0
        q = 0
        for i in range(round(noiseImage.size[0]*noiseImage.size[1]) ):
            if q == noiseImage.size[1]:
                q = 0
                k += 1
            if k == noiseImage.size[0]:
                k = 0
            r, g, b = noise_img.getpixel((k,q))

            putpixel = random.randint(0,10)
            if r + g + b > 50:
                if putpixel == 5:
                    noiseImage.putpixel(
                        (k, q),
                        (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    )
            q += 1

    noise_list.append(noiseImage)

    return noise_list


def brightness(brightness_list):
    brightImage = cropped_img_rotated.copy()

    enhancer = ImageEnhance.Brightness(brightImage)

    brightness = round(random.uniform(0.5, 1.5),1)

    brightImage = enhancer.enhance(brightness)

    brightness_list.append(brightImage)        

    return brightness_list


def colorSpace(colorSpace_list):
    colorSpaceImage = cropped_img_rotated.copy()
    if random.randint(1,100) > 20: 

        r_value = random.randint(-100, 100)
        g_value = random.randint(-100, 100)
        b_value = random.randint(-100, 100)

        for h in range(colorSpaceImage.size[0]):
            for w in range(colorSpaceImage.size[1]):
                r, g, b, a = colorSpaceImage.getpixel((h, w))
                if r + g + b > 50:
                    colorSpaceImage.putpixel((h,w),(r + r_value, g + g_value , b + b_value))

    colorSpace_list.append(colorSpaceImage)

    return colorSpace_list


def erase(erase_list):
    orig_img = cropped_img_rotated.copy()
    if random.randint(1,100) > 20:
        erasedImage = transforms.ToTensor()(orig_img)
        random_erase = RandomErasing(probability=1, mode='rand', device='cpu')
        tensor_img = random_erase(erasedImage)
        erasedImage = transforms.ToPILImage()(tensor_img)

        erase_list.append(erasedImage)

    else:
        erase_list.append(orig_img)
    
    return erase_list


def write_to_label_file(outPath, width, height, x_coord, y_coord):
    i = 0
    
    for i in range(len(x_coord)):
        if x_coord[i] != 0 and y_coord[i] != 0:
            x_center = (width[i]/2) + x_coord[i]
            y_center = (height[i]/2) + y_coord[i]
                
            val1 = round(x_center/1920, 4)
            val2 = round(y_center/1440, 4)
            val3 = round(width[i]/1920, 4)
            val4 = round(height[i]/1440, 4)

            val1 = format(val1, '.4f')
            val2 = format(val2, '.4f')
            val3 = format(val3, '.4f')
            val4 = format(val4, '.4f')

            cam = imagePath.split(".")

            with open(f"{outPath}/0_%d_{cam[0]}.txt" % count, "a") as f:
                f.write(f"1 {val1} {val2} {val3} {val4}\n")


def set_outPath(dataset):
    if cam1 in inputPath:
        outPath = f'{dir_tool}/{dir_mp}/vid/{dataset + "_" + current_time}/{cam1}'
    elif cam2 in inputPath:
        outPath = f'{dir_tool}/{dir_mp}/vid/{dataset + "_" + current_time}/{cam2}'
    elif cam3 in inputPath:
        outPath = f'{dir_tool}/{dir_mp}/vid/{dataset + "_" + current_time}/{cam3}'
    elif cam4 in inputPath:
        outPath = f'{dir_tool}/{dir_mp}/vid/{dataset + "_" + current_time}/{cam4}'
    elif cam5 in inputPath:
        outPath = f'{dir_tool}/{dir_mp}/vid/{dataset + "_" + current_time}/{cam5}'
    elif cam6 in inputPath:
        outPath = f'{dir_tool}/{dir_mp}/vid/{dataset + "_" + current_time}/{cam6}'

    return outPath


def save_image(list, imgPath, random_x_list, random_y_list):
    manipulatedBG = imgBG.copy()
    i = 0
    for img in list:
        manipulatedBG.paste(img, (random_x_list[i],random_y_list[i]), mask = img)
        i += 1
    manipulatedBG.save(imgPath)


create_directories()

for i in range(int(vid_number)):
    random_video = random.choice(vid_list)

    # selects random_video but not double
    if random_video in used_vid:
        while random_video in used_vid:
            random_video = random.choice(vid_list)
        used_vid.append(random_video)
    else:
        used_vid.append(random_video)

    print(random_video)
    BGPath = glob.glob(f'{parent_dir_mp}/{dir_all_vid}/{random_video}/frames/*png')
    sortedBGPath = natsorted(BGPath)

    # each frame of the random video
    for video_frame in sortedBGPath:
        inPath = f'{parent_dir_mp}/results/0600'

        # saves frame in 223, than 224, than 225 ...
        for imagePath in os.listdir(inPath):
            imgBG = Image.open(video_frame).convert("RGBA")                                                                           

            img_list = []
            blurred_list = []
            noise_list = []    
            brightness_list = []
            colorSpace_list = []       
            erase_list = []                                                                                                  ## add new list
            random_x_list = []
            random_y_list = []

            orig_height_list = []
            orig_width_list = []

            # puts random amount of products between 4 and 8 into the image  
            for p in range(random.randint(4,8)):                                                                            
                random_product = random.choice(product_list)
                inPath = f'{parent_dir_mp}/results/{random_product}'

                inputPath = os.path.join(inPath, imagePath)
                cam_nb = imagePath.split(".")
                img = Image.open(inputPath)

                # function to rotate the product
                cropped_img_rotated, random_x, random_y = product_rotation()

                img_list.append(cropped_img_rotated)
                random_x_list.append(random_x)
                random_y_list.append(random_y)

                if img_manipulation:                                                                                                    ## add new function
                    blur(blurred_list)
                    noise_injection(noise_list)
                    brightness(brightness_list)
                    colorSpace(colorSpace_list)
                    erase(erase_list)


            for x in img_list:
                orig_width, orig_height = x.size
                orig_width_list.append(orig_width)
                orig_height_list.append(orig_height)
            

            orig_x_list = copy.deepcopy(random_x_list)
            orig_y_list = copy.deepcopy(random_y_list)


            if img_manipulation:
                for x in manipulation:
                    outPath = set_outPath(x)
                    imgPath = os.path.join(outPath,f"0_%d_{imagePath}" % count)
                    match x:                                                                                                                ## add case
                        case "origin":
                            save_image(img_list, imgPath, orig_x_list, orig_y_list)
                        case "blurred":
                            save_image(blurred_list, imgPath, orig_x_list, orig_y_list)
                        case "noise":
                            save_image(noise_list, imgPath, orig_x_list, orig_y_list)
                        case "brightness":
                            save_image(brightness_list, imgPath, orig_x_list, orig_y_list)
                        case "colorSpace":
                            save_image(colorSpace_list, imgPath, orig_x_list, orig_y_list)
                        case "erase":
                            save_image(erase_list, imgPath, orig_x_list, orig_y_list)
                        
                    write_to_label_file(outPath, orig_width_list, orig_height_list, orig_x_list, orig_y_list) 
            else:
                outPath = set_outPath("origin")
                imgPath = os.path.join(outPath,f"0_%d_{imagePath}" % count)
                save_image(img_list, imgPath, orig_x_list, orig_y_list)

        count += 1

