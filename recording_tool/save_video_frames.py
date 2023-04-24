import cv2
import os


vid_number = input("Type the name of the video: ")

frames = os.getcwd() + f"\\recording_tool\\manipulated_images\\{vid_number}" 
create_frames = os.path.join(frames, "frames")

if os.path.exists(create_frames):
     ""
else:
     os.mkdir(create_frames)

vidcap = cv2.VideoCapture(f"C:/Users/dankem/Pictures/Videos/{vid_number}.mp4")
success,image = vidcap.read()
count = 0
frame_count = 0
while success:
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    if count % 25==0:
        saved= cv2.imwrite(f"recording_tool/manipulated_images/{vid_number}/frames/frame%d.png" % frame_count, image) 
        print('frame saved')
        frame_count += 1
    count += 1
        