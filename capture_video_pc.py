# import the necessary packages
import time
import cv2 as cv
import dlib
from utils import apply_offsets
from utils import draw_bounding_box
from utils import draw_str
from utils import rect_to_bb


# initialize the camera and grab a reference to the raw camera capture
cap = cv.VideoCapture('udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264  ! videoconvert  ! queue ! appsink sync=false ', cv.CAP_GSTREAMER)
detector = dlib.get_frontal_face_detector()

start = time.time()
frame_id = 0
# capture frames from the camera
while True:
    ret, frame = cap.read()
    faces = detector(frame, 1)

    for rect in faces:
        (x, y, w, h) = rect_to_bb(rect)
        x1, x2, y1, y2 = apply_offsets((x, y, w, h), (20, 40))
        color = (0, 255, 0)
        draw_bounding_box(image=frame, coordinates=(x1, y1, x2 - x1, y2 - y1), color=color)

    num_faces = len(faces)
    end = time.time()
    seconds = end - start
    fps = 1.0 / seconds
    draw_str(frame, (20, 20), 'fps: %d' % (fps))

    # show the frame
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF

    start = time.time()
    frame_id += 1

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
