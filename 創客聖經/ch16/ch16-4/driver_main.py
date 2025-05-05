import cv2
import logging
import sys

cap = cv2.VideoCapture(8)  # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0
if cap.isOpened():
    from deep_pi_car import DeepPiCar
else:
    from deep_pi_car_picam import DeepPiCar
cap.release()

def main():
    # print system info
    logging.info('Starting DeepPiCar, system info: ' + sys.version)
    
    with DeepPiCar() as car:
        car.drive(30)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
