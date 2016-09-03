import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

capture = cv2.VideoCapture(0)

while capture.isOpened():
    r, frame = capture.read()
    if r:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.1, 4)
        # face = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in face:
            cv2.circle(frame, ((x+w/2), (y+h/2)), 100, (0, 255, 0), 2)
    cv2.imshow("ObjectDetection", frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyWindow("ObjectDetection")
capture.release()

