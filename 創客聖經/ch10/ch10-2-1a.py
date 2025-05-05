import cv2

img = cv2.imread("images/koala.jpg")
img2 = cv2.imread("images/koala.jpg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(img2.shape)
h, w, c = img.shape
print("圖片高:", h)
print("圖片寬:", w)

