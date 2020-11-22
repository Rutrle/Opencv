import cv2

''' open a picture
img = cv2.imread('Resources/lena.png')

cv2.imshow("Output", img)
cv2.waitKey(0)
'''

cap = cv2.VideoCapture('Resources/test_video.mp4')


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
