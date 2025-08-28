from picamera2 import Picamera2, Preview
from time import sleep
import datetime

picam0 = Picamera2(0)
picam1 = Picamera2(1)

# Start cameras once
picam0.start_preview(Preview.QTGL)
picam1.start_preview(Preview.QTGL)
picam0.start()
picam1.start()

print("Cameras started. Press Enter to capture, or type 'q' then Enter to quit.")

counter = 1
while True:
    user_input = input("Press Enter to take a photo (or 'q' to quit): ")
    if user_input.strip().lower() == "q":
        break

    # Generate unique filenames (using counter or timestamp)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file0 = f"cam0_capture_{counter}_{timestamp}.jpg"
    file1 = f"cam1_capture_{counter}_{timestamp}.jpg"

    # Capture from both cameras
    picam0.capture_file(file0)
    picam1.capture_file(file1)
    print(f"Captured {file0} and {file1}")

    counter += 1

# Cleanup
picam0.stop()
picam1.stop()
picam0.stop_preview()
picam1.stop_preview()
print("Done.")

