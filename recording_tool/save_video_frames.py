import cv2
import os


vid_number = input("Type the name of the video: ")
vid_path = os.getcwd() + f"\\recording_tool\\videos\\"

all_vid = vid_path + f"all_vid\\"

frames = os.getcwd() + f"\\recording_tool\\videos\\{vid_number}" 
create_frames = os.path.join(frames, "frames")

if not os.path.exists(vid_path):
     os.mkdir(vid_path)
if not os.path.exists(all_vid):
     os.mkdir(all_vid)   
if not os.path.exists(frames):
     os.mkdir(frames)
if not os.path.exists(create_frames):
     os.mkdir(create_frames)
     
vidcap = cv2.VideoCapture(all_vid + f"{vid_number}.mp4")
success,image = vidcap.read()
count = 0
frame_count = 0
if image is not None:
     while success:
          success,image = vidcap.read()
          #print('Read a new frame: ', success)
          if count % 25==0:
               saved= cv2.imwrite(f"recording_tool/videos/{vid_number}/frames/frame%d.png" % frame_count, image) 
               print('frame saved')
               frame_count += 1
          count += 1
     