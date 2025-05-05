import os, time

for i in range(1, 6):
    dt = time.strftime("%Y_%m_%d-%H_%M_%S") 
    action = "fswebcam -d /dev/video8 -r 640x480 image" + str(dt) + ".jpg"  
    os.system(action)
    time.sleep(5)
