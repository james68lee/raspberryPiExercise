import cv2, imutils

url = "https://fchart.github.io/img/koala.png"
img = imutils.url_to_image(url)
cv2.imshow("Koala", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
