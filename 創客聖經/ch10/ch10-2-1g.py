import cv2

img = cv2.imread("images/koala.jpg")

cv2.line(img, (0,0), (200,200), (0,0,255), 5)
cv2.rectangle(img, (20,70), (120,160), (0,255,0), 2)
cv2.rectangle(img, (40,80), (100,140), (255,0,0), -1)
cv2.circle(img,(90,210), 30, (0,255,255), 3)
cv2.circle(img,(140,170), 15, (255,0,0), -1)
cv2.putText(img, 'OpenCV', (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,255,255), 5, cv2.LINE_AA)

cv2.imshow("Koala", img)

cv2.waitKey(0)
cv2.destroyAllWindows()