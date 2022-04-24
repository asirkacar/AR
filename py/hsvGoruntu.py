import cv2
import numpy as np
import tkinter

def nothing(x):
    pass

camera = cv2.VideoCapture(0)

cv2.namedWindow("Ekran", cv2.WINDOW_NORMAL)

cv2.createTrackbar("H1", "Ekran", 0, 359, nothing)
cv2.createTrackbar("H2", "Ekran", 0, 359, nothing)
cv2.createTrackbar("S1", "Ekran", 0, 255, nothing)
cv2.createTrackbar("S2", "Ekran", 0, 255, nothing)
cv2.createTrackbar("V1", "Ekran", 0, 255, nothing)
cv2.createTrackbar("V2", "Ekran", 0, 255, nothing)

while camera.isOpened():
    _, goruntu = camera.read()

    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

    h1 = int(cv2.getTrackbarPos("H1", "Ekran") / 2)
    h2 = int(cv2.getTrackbarPos("H2", "Ekran") / 2)
    s1 = cv2.getTrackbarPos("S1", "Ekran")
    s2 = cv2.getTrackbarPos("S2", "Ekran")
    v1 = cv2.getTrackbarPos("V1", "Ekran")
    v2 = cv2.getTrackbarPos("V2", "Ekran")

    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])

    mask = cv2.inRange(hsv, lower, upper)

    sonuc = cv2.bitwise_and(goruntu, goruntu, mask=mask)

    cv2.imshow("Ekran", goruntu)
    cv2.imshow("Maske", mask)
    cv2.imshow("Sonuc", sonuc)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()

