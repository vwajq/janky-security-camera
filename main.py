import cv2
from cvzone.FaceDetectionModule import FaceDetector

captured = cv2.VideoCapture(0)

detector = FaceDetector() 

while True:
    _, frame = captured.read()

    frame, boxes = detector.findFaces(frame)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

captured.release()
cv2.destroyAllWindows()