import os, time

for i in range(1, 6):
    action = "fswebcam -d /dev/video8 -r 640x480 image" + str(i) + ".jpg"  
    os.system(action)
    time.sleep(5)
