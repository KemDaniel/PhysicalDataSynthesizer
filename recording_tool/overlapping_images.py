from PIL import Image
import random
import os
import re
import glob
from natsort import natsorted

product_number = input("Type the product number: ")
while not (re.search("^([1-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][1-9])$", str(product_number))):
        product_number = input("   >>> Please type a 4 digit number without 0000: ")


vid_number = input("vid, vid1, vid2 or vid3: ")

random_rotate = random.randrange(0, 360)
random_x = random.randrange(129, 720)
if random_x > 500:
    random_y = random.randrange(510, 720) 
    random_size = round(random.uniform(0.3, 0.35),2)
else:
    random_y = random.randrange(400, 720) 
    random_size = round(random.uniform(0.4, 0.5),2)
print("size: ", random_size)
print("rotate: ", random_rotate)
print("x: ", random_x)
print("y: ", random_y)

dir_tool = "recording_tool"
dir_mp = "manipulated_images"
dir_frames = "video_frames"
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

parent_dir_mp = os.getcwd() + f"\\{dir_tool}" 
create_dir_mp = os.path.join(parent_dir_mp, dir_mp)

create_dir_vid = os.path.join(create_dir_mp, dir_vid)
create_dir_vid1 = os.path.join(create_dir_mp, dir_vid1)
create_dir_vid2 = os.path.join(create_dir_mp, dir_vid2)
create_dir_vid3 = os.path.join(create_dir_mp, dir_vid3)

vid_product_number = os.path.join(create_dir_vid, product_number)
vid1_product_number = os.path.join(create_dir_vid1, product_number)
vid2_product_number = os.path.join(create_dir_vid2, product_number)
vid3_product_number = os.path.join(create_dir_vid3, product_number)

cam1_vid = os.path.join(vid_product_number, cam1)
cam2_vid = os.path.join(vid_product_number, cam2)
cam3_vid = os.path.join(vid_product_number, cam3)
cam4_vid = os.path.join(vid_product_number, cam4)
cam5_vid = os.path.join(vid_product_number, cam5)
cam6_vid = os.path.join(vid_product_number, cam6)

cam1_vid1 = os.path.join(vid1_product_number, cam1)
cam2_vid1 = os.path.join(vid1_product_number, cam2)
cam3_vid1 = os.path.join(vid1_product_number, cam3)
cam4_vid1 = os.path.join(vid1_product_number, cam4)
cam5_vid1 = os.path.join(vid1_product_number, cam5)
cam6_vid1 = os.path.join(vid1_product_number, cam6)

cam1_vid2 = os.path.join(vid2_product_number, cam1)
cam2_vid2 = os.path.join(vid2_product_number, cam2)
cam3_vid2 = os.path.join(vid2_product_number, cam3)
cam4_vid2 = os.path.join(vid2_product_number, cam4)
cam5_vid2 = os.path.join(vid2_product_number, cam5)
cam6_vid2 = os.path.join(vid2_product_number, cam6)

cam1_vid3 = os.path.join(vid3_product_number, cam1)
cam2_vid3 = os.path.join(vid3_product_number, cam2)
cam3_vid3 = os.path.join(vid3_product_number, cam3)
cam4_vid3 = os.path.join(vid3_product_number, cam4)
cam5_vid3 = os.path.join(vid3_product_number, cam5)
cam6_vid3 = os.path.join(vid3_product_number, cam6)

if os.path.exists(create_dir_mp):
    print(f"\nDirectory '{dir_mp}' exists already.\n")
else:
    os.mkdir(create_dir_mp)
    print(f"\nDirectory '{dir_mp}' created.\n")     

if os.path.exists(create_dir_vid):
     ""
else:
     os.mkdir(create_dir_vid)

if os.path.exists(create_dir_vid1):
     ""
else:
     os.mkdir(create_dir_vid1)

if os.path.exists(create_dir_vid2):
     ""
else:
     os.mkdir(create_dir_vid2)

if os.path.exists(create_dir_vid3):
     ""
else:
     os.mkdir(create_dir_vid3)

if vid_number == dir_vid:

    if os.path.exists(vid_product_number):
        ""
    else:
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

if vid_number == dir_vid:

    if os.path.exists(vid1_product_number):
        ""
    else:
        os.mkdir(vid1_product_number)
    
    if not os.path.exists(cam1_vid1):
        os.mkdir(cam1_vid1)

    if not os.path.exists(cam2_vid1):
        os.mkdir(cam2_vid1)

    if not os.path.exists(cam3_vid1):
        os.mkdir(cam3_vid1)
    
    if not os.path.exists(cam4_vid1):
        os.mkdir(cam4_vid1)

    if not os.path.exists(cam5_vid1):
        os.mkdir(cam5_vid1)

    if not os.path.exists(cam6_vid1):
        os.mkdir(cam6_vid1)

if vid_number == dir_vid2:

    if os.path.exists(vid2_product_number):
        ""
    else:
        os.mkdir(vid2_product_number)

    if not os.path.exists(cam1_vid2):
        os.mkdir(cam1_vid2)

    if not os.path.exists(cam2_vid2):
        os.mkdir(cam2_vid2)

    if not os.path.exists(cam3_vid2):
        os.mkdir(cam3_vid2)

    if not os.path.exists(cam4_vid2):
        os.mkdir(cam4_vid2)

    if not os.path.exists(cam5_vid2):
        os.mkdir(cam5_vid2)

    if not os.path.exists(cam6_vid2):
        os.mkdir(cam6_vid2)

if vid_number == dir_vid3:

    if os.path.exists(vid3_product_number):
        ""
    else:
        os.mkdir(vid3_product_number)

    if not os.path.exists(cam1_vid3):
        os.mkdir(cam1_vid3)

    if not os.path.exists(cam2_vid3):
        os.mkdir(cam2_vid3)

    if not os.path.exists(cam3_vid3):
        os.mkdir(cam3_vid3)

    if not os.path.exists(cam4_vid3):
        os.mkdir(cam4_vid3)

    if not os.path.exists(cam5_vid3):
        os.mkdir(cam5_vid3)

    if not os.path.exists(cam6_vid3):
        os.mkdir(cam6_vid3)


BGPath = glob.glob(f'{parent_dir_mp}/{dir_mp}/{vid_number}/frames/*png')

inPath = f'{parent_dir_mp}/results/{product_number}'

count = 0
sortedBGPath = natsorted(BGPath)

for video_frame in sortedBGPath:
    #framePath = os.path.join(sortedBGPath, video_frame)
    framePath = video_frame

    for imagePath in os.listdir(inPath):
        inputPath = os.path.join(inPath, imagePath)

        img = Image.open(inputPath)
        imgBG = Image.open(framePath).convert("RGBA")
        

        if cam1 in inputPath:
            outPath = f'{dir_tool}/{dir_mp}/{vid_number}/{product_number}/{cam1}'
        elif cam2 in inputPath:
            outPath = f'{dir_tool}/{dir_mp}/{vid_number}/{product_number}/{cam2}'
        elif cam3 in inputPath:
            outPath = f'{dir_tool}/{dir_mp}/{vid_number}/{product_number}/{cam3}'
        elif cam4 in inputPath:
            outPath = f'{dir_tool}/{dir_mp}/{vid_number}/{product_number}/{cam4}'
        elif cam5 in inputPath:
            outPath = f'{dir_tool}/{dir_mp}/{vid_number}/{product_number}/{cam5}'
        elif cam6 in inputPath:
            outPath = f'{dir_tool}/{dir_mp}/{vid_number}/{product_number}/{cam6}'
        
        fullOutPath = os.path.join(outPath,f"{product_number}_%d_{imagePath}" % count)

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

        with open(f"{outPath}/{product_number}_%d_{cam[0]}.txt" % count, "w") as f:
            f.write(f"1 {val1} {val2} {val3} {val4}\n")

        imgBG.paste(cropped_img_rotated, (random_x,random_y), mask = cropped_img_rotated)

        imgBG.save(fullOutPath)
        
    count += 1
