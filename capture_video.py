# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from common import draw_str
#from kafka import KafkaProducer
from time import gmtime, strftime

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
#producer = KafkaProducer(bootstrap_servers=['10.156.91.65:9092'], api_version=(0, 10))
#num_faces = 0

# allow the camera to warmup
time.sleep(0.1)

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_alt.xml')

start = time.time()
frame_id = 0
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    image = cv2.flip(image, 0)

    #if frame_id % 30 == 0:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    #cur_num_faces = len(faces)

    if faces is not None and len(faces) > 0:
        for (x, y, w, h) in faces:
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # if cur_num_faces > num_faces:
    #     message = "[{}] Detected {} face(s).".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), cur_num_faces)
    #     b_msg = bytearray()
    #     b_msg.extend(map(ord, message))
    #     producer.send('test', b_msg)
    #     producer.flush()

    #num_faces = cur_num_faces
    end = time.time()
    seconds = end - start
    fps = 1.0 / seconds
    draw_str(image, (20, 20), 'fps: %d' % (fps))

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    start = time.time()
    frame_id += 1

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
