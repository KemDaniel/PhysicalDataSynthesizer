import os,os.path
import shutil
import glob
from natsort import natsorted
import random

dir_tool = os.getcwd() + f"\\recording_tool" 
dir_mm = "multiple_manipulated"
dir_mp = "manipulated_images"
choice = ""

multiple = input('Type "m" for multiple: ') == "m"
product = input ('Type the product number: ')
vid = input('Type which video: ')
if multiple:
    recording_tool = glob.glob(f'{dir_tool}\\{dir_mm}\\{vid}\\{product}\\**\\')
    choice = "multi"
else:
    recording_tool = glob.glob(f'{dir_tool}\\{dir_mp}\\{vid}\\{product}\\**\\')
    choice = "single"

destination_folder = f'{dir_tool}\\'
png = 'png'
txt = 'txt'
images = 'images\\'
labels = 'labels\\'
dataset = 'datasets\\'
dataset_path = destination_folder + dataset + product + "_" + vid + "_" + choice

train = 'train\\'
val = 'val\\'
test = 'test\\'

if not os.path.exists(destination_folder + dataset):
    os.mkdir(destination_folder + dataset)

os.mkdir(dataset_path)

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
        if png_or_txt > 0:
            source = folder + file

            if png in source:
                if os.path.isfile(source):
                    destination = destination_folder + train + images + file
                    shutil.copy(source, destination)
                                      
            if txt in source:
                if os.path.isfile(source):
                    destination = destination_folder + train + labels + file
                    shutil.copy(source, destination)
                    png_or_txt -= 1
                    count += 1

while  val_percentage > 0: 
    for file in os.listdir(destination_folder + train + images):
        rand_int = random.randint(0, 9)
        filename = file.split(".")

        source_img = destination_folder + train + images + file
        source_labels = destination_folder + train + labels + filename[0] + ".txt"

        destination_img = destination_folder + val + images + file          
        destination_labels = destination_folder + val + labels + filename[0] + ".txt"

        if rand_int == 9:
            if png in source_img:
                if os.path.isfile(source_img):
                    shutil.copy(source_img, destination_img)
                    os.remove(destination_folder + train + images + file)
                    val_percentage -= 1
            
            for txt_file in os.listdir(destination_folder + train + labels):
                if txt_file == filename[0] + ".txt":
                        shutil.copy(source_labels, destination_labels)
                        os.remove(destination_folder + train + labels + filename[0] + ".txt")
        
        if val_percentage == 0:
            break

while test_percentage > 0:
    for file in os.listdir(destination_folder + train + images):
        rand_int = random.randint(0, 10)
        filename = file.split(".")

        source_img = destination_folder + train + images + file
        source_labels = destination_folder + train + labels + filename[0] + ".txt"

        destination_img = destination_folder + test + images + file
        destination_labels = destination_folder + test + labels + filename[0] + ".txt"

        if rand_int == 10:
            if png in source_img:
                if os.path.isfile(source_img):
                    shutil.copy(source_img, destination_img)
                    os.remove(destination_folder + train + images + file)
                    test_percentage -= 1
                
            for txt_file in os.listdir(destination_folder + train + labels):
                if txt_file == filename[0] + ".txt":
                    shutil.copy(source_labels, destination_labels)
                    os.remove(destination_folder + train + labels + filename[0] + ".txt")

        if test_percentage == 0:
            break


shutil.move(destination_folder + train, dataset_path)
shutil.move(destination_folder + val, dataset_path)
shutil.move(destination_folder + test, dataset_path)