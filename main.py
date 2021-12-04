import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

captured = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.8) 
arduino = SerialObject("COM6", 9600, 1)

while True:
    _, frame = captured.read()

    frame, boxes = detector.findFaces(frame)

    if boxes:
        arduino.sendData([1, 0])
    else:
        arduino.sendData([0, 1])

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

captured.release()
cv2.destroyAllWindows()