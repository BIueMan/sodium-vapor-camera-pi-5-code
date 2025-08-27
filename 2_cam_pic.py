
from picamera2 import Picamera2, Preview
from time import sleep

picam0 = Picamera2(0)
picam1 = Picamera2(1)

## Capture 2 pics
picam0.start_preview(Preview.QTGL)
picam1.start_preview(Preview.QTGL)
picam0.start()
picam1.start()
sleep(10)
picam0.capture_file("cam0_me_lowlight.jpg")
picam1.capture_file("cam1_me_lowlight.jpg")
picam0.stop()
picam1.stop()
picam0.stop_preview()
picam1.stop_preview()

## Capture 2 videos