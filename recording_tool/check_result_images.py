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

product_list = ["0740", "0741", "0742", "0743", "0744", "0745", "0746", "0747", "0748", "0749", "0750", "0751", "0752",
                "0753", "0754", "0755", "0756", "0757", "0758", "0759", "0760", "0761", "0762", "0763", "0764", "0765", "0766",
                "0767", "0768", "0769", "0770", "0771", "0772", "0773", "0774", "0775", "0776"]
#product_number = input("Tippe die Produktennummer ein: ")

parent_dir_mp = os.getcwd() + f"\\{dir_tool}" 
create_dir_mp = os.path.join(parent_dir_mp, dir_mp)

dir_1000 = parent_dir_mp + "/results/1000"
if not os.path.exists(dir_1000):
    os.mkdir(dir_1000)

BGPath = f'{parent_dir_mp}/{dir_all_vid}/vid/frames/frame1.png'
                
inPath = glob.glob(f'{parent_dir_mp}/results/**/*png')

k = 0

for i in range(len(product_list)):

    inPath = glob.glob(f'{parent_dir_mp}/results/{product_list[k]}/*png')
    k += 1

    for image in inPath:

        cam = image.replace('\\', '/')
        cam = cam.replace('.', '/')
        cam = cam.split('/')

        if cam[9] != "1000":

            img = Image.open(image)
            imgBG = Image.open(BGPath).convert("RGBA")

            random_rotate = random.randrange(0, 360)
            random_x = random.randrange(129, 720)
            if random_x > 500:
                random_y = random.randrange(510, 720) 
                random_size = round(random.uniform(0.5, 0.55),2)
            else:
                random_y = random.randrange(400, 720)
                random_size = round(random.uniform(0.65, 0.7),2)

            outPath = f'{dir_tool}/results/1000'
            n = 1
            fullOutPath = outPath + f"/{cam[9]}_{cam[10]}.png" 

                                
            img_resized = img.resize((round(img.size[0]*random_size), round(img.size[1]*random_size))) 
            img_rotated = img_resized.rotate(random_rotate, expand=True)

            cropped_img_rotated = img_rotated.crop(img_rotated.getbbox())
            width, height = cropped_img_rotated.size
            x_center = (width/2) + random_x
            y_center = (height/2) + random_y


            imgBG.paste(cropped_img_rotated, (random_x,random_y), mask = cropped_img_rotated)

            imgBG.save(fullOutPath)
                            
