import cv2

img = cv2.imread("images/koala.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Koala:gray", gray_img)
cv2.imshow("Koala:rgb", rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()