#!/usr/bin/python3

import time

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

camera_a = Picamera2(0)
camera_a.configure(camera_a.create_preview_configuration())
camera_a.start_preview(Preview.QTGL, x=100,y=300,width=400,height=300)

camera_b = Picamera2(1)
camera_b.configure(camera_b.create_preview_configuration())
camera_b.start_preview(Preview.QT, x=500,y=300,width=400,height=300)

camera_a.start()
camera_b.start()

time.sleep(2)

encodera = H264Encoder(1000000)
encoderb = H264Encoder(1000000)

camera_a.start_recording(encodera,"cam a record.h264")
camera_b.start_recording(encoderb,"cam b record.h264")

time.sleep(1000)

camera_a.stop_recording()
camera_b.stop_recording()

camera_a.stop_preview()
camera_b.stop_preview()


