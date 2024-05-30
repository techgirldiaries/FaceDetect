import cv2, numpy as np

# Load the pre-trained face classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return image
    
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y), (x+w,y+h), (255, 0, 0), 2)
    return image

capture = cv2.VideoCapture(0)

while True: 
    ret, frame = capture.read()
    frame = detect_faces(frame)

    cv2.imshow("Video Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


capture.release()
cv2.destroyAllWindows()