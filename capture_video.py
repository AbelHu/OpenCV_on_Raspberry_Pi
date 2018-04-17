import cv2

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')

success, image = cameraCapture.read()
while success:
    success, image = cameraCapture.read()
    cv2.imshow('MyWindow', image)
    ch = cv2.waitKey(1)
    if ch == 27:
        break

cv2.destroyWindow('MyWindow')
cameraCapture.release()
