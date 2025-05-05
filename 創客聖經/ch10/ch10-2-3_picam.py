import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()
while True:
    image = picam2.capture_array()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
    cv2.imshow("Frame", image)
    if(cv2.waitKey(1) == ord("q")):
        cv2.imwrite("test_frame.png", image)
        break

cv2.destroyAllWindows()

