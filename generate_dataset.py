import os,os.path
import shutil
import glob
from natsort import natsorted

dir_tool = os.getcwd() + f"\\recording_tool" 
dir_mm = "multiple_manipulated"
dir_mp = "manipulated_images"

multiple = input('Type "m" for multiple: ') == "m"
vid = input('Type which video: ')
product = input ('Type the product number: ')
if multiple:
    recording_tool = glob.glob(f'{dir_tool}\\{dir_mm}\\{vid}\\{product}\\**\\')
else:
    recording_tool = glob.glob(f'{dir_tool}\\{dir_mp}\\{vid}\\{product}\\**\\')

destination_folder = f'{dir_tool}\\'
png = 'png'
txt = 'txt'
images = 'images\\'
labels = 'labels\\'

train = 'train\\'
val = 'val\\'
test = 'test\\'

if os.path.exists(destination_folder + train):
    ""
else:
    os.mkdir(destination_folder + train)
    os.mkdir(destination_folder + train + images)
    os.mkdir(destination_folder + train + labels)

    os.mkdir(destination_folder + val)
    os.mkdir(destination_folder + val + images)
    os.mkdir(destination_folder + val + labels)

    os.mkdir(destination_folder + test)
    os.mkdir(destination_folder + test + images)
    os.mkdir(destination_folder + test + labels)

file_number = 0
for folder in recording_tool:
    for x in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, x)):
            file_number += 1

png_or_txt = (file_number/2)

train_percentage = png_or_txt * 0.8
val_percentage = png_or_txt * 0.1
test_percentage = png_or_txt * 0.1

count = 0
for folder in recording_tool:
    natsorted(folder)
    for file in os.listdir(folder):
        if train_percentage > 0:
        #if train_percentage > 0 and count%10 != 0 and count%11 != 0: 
            source = folder + file

            if png in source:
                if os.path.isfile(source):
                    destination = destination_folder + train + images + file
                    shutil.copy(source, destination)
                                      
            if txt in source:
                if os.path.isfile(source):
                    destination = destination_folder + train + labels + file
                    shutil.copy(source, destination)
                    train_percentage = train_percentage - 1
                    count += 1

        elif val_percentage > 0: 
        #elif count%10 == 0 and val_percentage > 0:
            source = folder + file

            if png in source:
                if os.path.isfile(source):
                    destination = destination_folder + val + images + file
                    shutil.copy(source, destination)
                                       
            if txt in source:
                if os.path.isfile(source):
                    destination = destination_folder + val + labels + file
                    shutil.copy(source, destination)
                    val_percentage = val_percentage - 1
                    count += 1

        elif test_percentage > 0:
        #elif count%11 == 0 and test_percentage > 0: 
            source = folder + file

            if png in source:
                if os.path.isfile(source):
                    destination = destination_folder + test + images + file
                    shutil.copy(source, destination)
                    
            if txt in source:
                if os.path.isfile(source):
                    destination = destination_folder + test + labels + file
                    shutil.copy(source, destination)
                    test_percentage = test_percentage - 1
                    count += 1
