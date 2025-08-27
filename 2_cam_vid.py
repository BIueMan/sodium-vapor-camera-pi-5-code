## Capture 2 pics
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time

# Create Picamera2 instances for each camera


cam0 = Picamera2(0)  # First camera
cam1 = Picamera2(1)  # Second camera

# Configure both for video recording
config0 = cam0.create_video_configuration()
config1 = cam1.create_video_configuration()

cam0.configure(config0)
cam1.configure(config1)

cam0.start_preview(Preview.QTGL)
cam1.start_preview(Preview.QTGL)
# Start both cameras
cam0.start()
cam1.start()

# Start recording

encodera = H264Encoder(1000000)
encoderb = H264Encoder(1000000)

cam0.start_recording(encodera,"/home/dan/Desktop/SV_camera_progect/cam0 record.h264")
cam1.start_recording(encoderb,"/home/dan/Desktop/SV_camera_progect/cam1 record.h264")

time.sleep(10)  # Record for 10 seconds

# Stop recording
cam0.stop_recording()
cam1.stop_recording()

cam0.stop_preview()
cam1.stop_preview()

# Stop cameras
cam0.stop()
cam1.stop()
