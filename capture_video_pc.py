# import the necessary packages
import time
import cv2 as cv
from common import draw_str
from kafka import KafkaProducer
from time import gmtime, strftime

# initialize the camera and grab a reference to the raw camera capture
cap = cv.VideoCapture(0)
producer = KafkaProducer(bootstrap_servers=['10.156.91.65:9092'], api_version=(0, 10))
num_faces = 0

face_cascade = cv.CascadeClassifier(
    r'C:\Users\foamliu.FAREAST\code\3rd-party\opencv\data\haarcascades\haarcascade_frontalface_alt.xml')

start = time.time()
frame_id = 0
# capture frames from the camera
while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    cur_num_faces = len(faces)
    if faces is not None and cur_num_faces > 0:
        for (x, y, w, h) in faces:
            image = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if cur_num_faces > num_faces:
        message = "[{}] Detected {} face(s).".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), cur_num_faces)
        b_msg = bytearray()
        b_msg.extend(map(ord, message))
        producer.send('test', b_msg)
        producer.flush()

    num_faces = cur_num_faces

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
