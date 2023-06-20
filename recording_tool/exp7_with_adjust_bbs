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


def calculate_product_mask(img_list):
    numpy_list = []

    for x in img_list:
        x = x.convert("L")
        pix = np.array(x)
        for h in range(pix.shape[0]):
            for w in range(pix.shape[1]):
                if pix[h][w] > 0:
                    pix[h][w] = 255
                else:
                    pix[h][w] = 0
        numpy_list.append(pix)
    
    return numpy_list

def calculate_overlapping(product_mask, x_coord, y_coord, size):

    x_bg, y_bg = size
    mask = np.zeros(shape=(y_bg, x_bg))
    length = len(product_mask)
    test = 0
    bg_list = []
    changed_masks = []
    orig_mask = copy.deepcopy(product_mask)

    for x in reversed(product_mask):

        product_img = np.zeros(shape=(y_bg, x_bg))
        mask_x = x_coord[length-1]
        mask_y = y_coord[length-1]
        product_img[mask_y:mask_y+x.shape[0], mask_x:mask_x+x.shape[1]] = x

        for h in range(product_img.shape[0]):
            for w in range(product_img.shape[1]):
                               
                if product_img[h][w] == 255 and mask[h][w] == 255:
                    test += 1
                    x[h-mask_y][w-mask_x] = 0

                if product_img[h][w] == 255 and mask[h][w] == 0:
                    mask[h][w] = 255
        
        bg_list.append(product_img)
        changed_masks.append(x)

        length -= 1
    
    return changed_masks, orig_mask
        
def calculate_new_bb(changed_masks, orig_masks, x_coord, y_coord):
    from matplotlib import pyplot as plt
    height_list = []
    width_list = []
    i = 0
    bb_changed = 0
    for x in reversed(changed_masks):
        old_x = orig_masks[i]
        x_temp = x_coord[i]
        y_temp = y_coord[i]

        if not (x == old_x).all():                                        
            pix = np.argwhere(x == 255)

            if pix.shape[0] != 0:

                min_x = min(pix[:, 1])                                     
                max_x = max(pix[:, 1])
                min_y = min(pix[:, 0])
                max_y = max(pix[:, 0])                                         

                padding = 5

                if min_x < 10:
                    min_x = 0
                else:
                    min_x = min_x - padding

                if min_y < 10:
                    min_y = 0
                else:
                    min_y = min_y - padding

                if x.shape[1] - max_x < 10:
                    max_x = x.shape[1]
                else:
                    max_x = max_x + padding

                if x.shape[0] - max_y < 10:
                    max_y = x.shape[0]
                else:
                    max_y = max_y + padding

                new_x_coord = x_temp + min_x
                new_y_coord = y_temp + min_y 

                x_coord[i] = new_x_coord
                y_coord[i] = new_y_coord

                height = (max_y-min_y)
                width = (max_x-min_x)

                height_list.append(height)
                width_list.append(width)

                bb_changed += 1
            else:
                # object is fully overlapped, set values to 0 to skip product in write label
                x_coord[i] = 0
                y_coord[i] = 0
                zero_height = 0
                zero_width = 0
                height_list.append(zero_height)
                width_list.append(zero_width)

        else:
            height, width = x.shape

            height_list.append(height)
            width_list.append(width)

        i += 1

    return height_list, width_list, x_coord, y_coord


def blur(blurred_list):
    if random.randint(0,100) > 80:
        blurredImage = cropped_img_rotated.filter(ImageFilter.GaussianBlur(random.randint(1,3)))
    else: 
        blurredImage = cropped_img_rotated

    blurred_list.append(blurredImage)

    return blurred_list


def noise_injection(noise_list):
    noiseImage = cropped_img_rotated.copy()
    noise_img = cropped_img_rotated.convert("RGB")
    if random.randint(0,100) > 80: 
        k = 0
        q = 0
        for i in range(round(noiseImage.size[0]*noiseImage.size[1]) ):
            if q == noiseImage.size[1]:
                q = 0
                k += 1
            if k == noiseImage.size[0]:
                k = 0
            r, g, b = noise_img.getpixel((k,q))

            putpixel = random.randint(0,15)
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
    if random.randint(0,100) > 80: 

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
    if random.randint(0,100) > 80:
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

            product_mask = calculate_product_mask(img_list)

            orig_x_list = copy.deepcopy(random_x_list)
            orig_y_list = copy.deepcopy(random_y_list)

            changed_masks, orig_masks = calculate_overlapping(product_mask, random_x_list, random_y_list, imgBG.size)

            height_list, width_list, random_x_list, random_y_list = calculate_new_bb(changed_masks, orig_masks, random_x_list, random_y_list)

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
                        
                    write_to_label_file(outPath, width_list, height_list, random_x_list, random_y_list)             
            else:
                outPath = set_outPath("origin")
                imgPath = os.path.join(outPath,f"0_%d_{imagePath}" % count)
                save_image(img_list, imgPath)

        count += 1

