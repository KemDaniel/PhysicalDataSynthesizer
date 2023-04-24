from rembg import remove
from PIL import Image
import cv2
import numpy as np
import os
import shutil

pn = input('Type the productnumber: ')
cam = input('Type the cam: ')

rt = "recording_tool"
results = "results"

def crop_again():
    #inputPath = (f'C:\\Users\\dankem\\Documents\\Research and Tools\\recording_tool\\results\{pn}\\{cam}.png')
    #oldImage = (f'C:\\Users\\dankem\\Documents\\Research and Tools\\recording_tool\\results\{pn}\\{cam}_old.png')
    
    inputPath = os.getcwd() + f'\\{rt}\\{results}\{pn}\\{cam}.png'
    oldImage = os.getcwd() + f'\\{rt}\\{results}\{pn}\\{cam}_old.png'
    
    shutil.copyfile(inputPath, oldImage)

    path = inputPath
    outputPath = inputPath

    input = Image.open(path)

    output = remove(input)

    op = output.crop(output.getbbox())

    op.save(outputPath)

def set_pixel_value_to_0():
    #inputPath = (f'C:\\Users\\dankem\\Documents\\Research and Tools\\recording_tool\\results\{pn}\\{cam}.png')
    #oldImage = (f'C:\\Users\\dankem\\Documents\\Research and Tools\\recording_tool\\results\{pn}\\{cam}_old.png')
    
    inputPath = os.getcwd() + f'\\{rt}\\{results}\{pn}\\{cam}.png'
    oldImage = os.getcwd() + f'\\{rt}\\{results}\{pn}\\{cam}_old.png'
    
    shutil.copyfile(inputPath, oldImage)

    img = np.asarray(cv2.imread(inputPath))
    img[img < 10] = 0
    cv2.imwrite(inputPath, img) #+ "new.png"

    path = inputPath #+ "new.png"
    outputPath = inputPath #+ "removed.png"

    input = Image.open(path)

    output = remove(input)

    op = output.crop(output.getbbox())

    op.save(outputPath)

crop_again()
#set_pixel_value_to_0()