import cv2

img = cv2.imread("images/koala.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("result_gray.jpg", gray_img)
cv2.imwrite("result.png", img)