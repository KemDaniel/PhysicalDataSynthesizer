import cv2
import numpy as np
from PIL import Image
import shutil
from rembg import remove
import os


pn = input('Type the productnumber: ')
cam = input('Type the cam: ')

positions=[] 
positions2=[]
count=0
rt = "recording_tool"
results = "results"

img_path = os.getcwd() + f'\\{rt}\\{results}\{pn}\\{cam}.png'

def draw_circle(event,x,y,flags,param):
    global positions,count
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),2,(0,0,0),-1)
        positions.append([x,y])
        if(count!=3):
            positions2.append([x,y])
        elif(count==3):
            positions2.insert(2,[x,y])
        count+=1
        
img = cv2.imread(img_path)

cv2.namedWindow('image')

cv2.setMouseCallback('image',draw_circle)


while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


pts2=np.float32(positions)

x_lowest_value = pts2[0][0]
x_highest_value = pts2[1][0]

y_lowest_value = pts2[0][1]
y_highest_value = pts2[1][1]


print(x_lowest_value , x_highest_value)

print(y_lowest_value, y_highest_value)

x_area = x_highest_value - x_lowest_value
y_area = y_highest_value - y_lowest_value
x_val = 0
y_val = 0

img = Image.open(img_path)
old_img = os.getcwd() + f'\\{rt}\\{results}\{pn}\\{cam}_old.png'

shutil.copyfile(img_path, old_img)


while x_area != 0:
    while y_area != 0:
        img.putpixel( (int(x_val + x_lowest_value),int(y_val + y_lowest_value)), 0 )
        y_area -= 1
        y_val += 1

    x_area -= 1
    y_area = y_highest_value - y_lowest_value

    x_val += 1
    y_val = 0

outputPath = img_path

img.save(outputPath)
