import cv2
img = cv2.imread('Resources/lambo.png')


print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]  # height first, then width

cv2.imshow("Image", img)
cv2.imshow("Resized image", imgResize)
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)
