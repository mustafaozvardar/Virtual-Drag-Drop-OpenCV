import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=1)
colorR = (255, 0, 255)

cx, cy, w, h = 100,100,200,200

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:

        l,_,_ = detector.findDistance(8, 12, img)
        print(l)
        if l<30:
            cursor = lmList[8]
            if cx-w//2 <cursor[0] <cx+w//2 and cy-h//2<cursor[1]<cy+h//2:
                colorR = 0,255,0
                cx, cy = cursor
            else:
                colorR = (255, 0, 255)

    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()