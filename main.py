from picamera2 import Picamera2
import cv2

def main():
    picam2 = Picamera2()
    picam2.start()
    frame = picam2.capture_array()
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
