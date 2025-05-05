import cv2

img = cv2.imread("images/koala.jpg")
cv2.imshow("Koala", img)

gray_img = cv2.imread("images/koala.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Koala:gray", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

