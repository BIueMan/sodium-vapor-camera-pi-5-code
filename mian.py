import cv2

# Open the camera (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

# Capture a single frame
ret, frame = cap.read()
cap.release()

if not ret:
    print("❌ Failed to grab frame")
    exit()

# Save the image (optional)
cv2.imwrite("photo.jpg", frame)

# Show the image
cv2.imshow("Captured Image", frame)

# Wait until you press a key or close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
