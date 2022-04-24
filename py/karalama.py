import cv2
import numpy as np

"""resim = cv2.imread("12.jpg")    ------------------- RESME EŞİK UYGULAMA RENKLİ KISIMLARI BEYAZ KALANI SİYAHLAMA -------------------
resim_gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(resim_gray, 5, 255, cv2.THRESH_BINARY)
cv2.imshow("resim", mask)"""

camera = cv2.VideoCapture(0)        #------------------- KEMERADAN GELEN CANLI GÖRÜNTÜYE RENK FİLTRELEME -------------------
def nothing(x):
    pass
cv2.namedWindow("resim1")
cv2.createTrackbar("H1", "resim1", 0, 359, nothing)
cv2.createTrackbar("H2", "resim1", 0, 359, nothing)
cv2.createTrackbar("S1", "resim1", 0, 255, nothing)
cv2.createTrackbar("S2", "resim1", 0, 255, nothing)
cv2.createTrackbar("V1", "resim1", 0, 255, nothing)
cv2.createTrackbar("V2", "resim1", 0, 255, nothing)

while(1):
    _, frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h1 = int(cv2.getTrackbarPos("H1", "resim1") / 2)
    h2 = int(cv2.getTrackbarPos("H2", "resim1") / 2)
    s1 = cv2.getTrackbarPos("S1", "resim1")
    s2 = cv2.getTrackbarPos("S2", "resim1")
    v1 = cv2.getTrackbarPos("V1", "resim1")
    v2 = cv2.getTrackbarPos("V2", "resim1")

    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])

    mask = cv2.inRange(hsv, lower, upper)
    sonuc = cv2.bitwise_and(frame, frame, mask=mask)
    #sonuc2 = cv2.flip(sonuc,)

    cv2.imshow("resim", sonuc)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
"""def nothing(x):          ------------------- DÜZ EKRANA RGB UYGULAMA -------------------
    pass
bosEkran = np.zeros([512, 512, 3], np.uint8)
cv2.namedWindow("resim")
cv2.createTrackbar("R", "resim", 0, 255, nothing)
cv2.createTrackbar("G", "resim", 0, 255, nothing)
cv2.createTrackbar("B", "resim", 0, 255, nothing)
cv2.createTrackbar("ON/OFF", "resim", 0, 1, nothing)
while(1):
    cv2.imshow("resim", bosEkran)
    r = cv2.getTrackbarPos("R", "resim")
    g = cv2.getTrackbarPos("G", "resim")
    b = cv2.getTrackbarPos("B", "resim")
    switch = cv2.getTrackbarPos("ON/OFF", "resim")

    if switch:
        bosEkran[:] = [b, g, r]
    else:
        bosEkran[:] = 0

    #bosEkran[:] = [b, g, r]
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break"""

"""def nothing(x):             #------------------- RESME HSV RENK FİLTRESİ UYGULAMA -------------------
    pass

#resim = resim.shape
#print(resim)
cv2.namedWindow("resim")
cv2.createTrackbar("H1", "resim", 0, 359, nothing)
cv2.createTrackbar("H2", "resim", 0, 359, nothing)
cv2.createTrackbar("S1", "resim", 0, 255, nothing)
cv2.createTrackbar("S2", "resim", 0, 255, nothing)
cv2.createTrackbar("V1", "resim", 0, 255, nothing)
cv2.createTrackbar("V2", "resim", 0, 255, nothing)

while(1):
    resim = cv2.imread("12.jpg")
    hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    h1 = int(cv2.getTrackbarPos("H1", "resim") / 2)
    h2 = int(cv2.getTrackbarPos("H2", "resim") / 2)
    s1 = cv2.getTrackbarPos("S1", "resim")
    s2 = cv2.getTrackbarPos("S2", "resim")
    v1 = cv2.getTrackbarPos("V1", "resim")
    v2 = cv2.getTrackbarPos("V2", "resim")

    lower = np.array([h1, s1, v1])
    upper = np.array([h2, s2, v2])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(resim, resim, mask=mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    cv2.imshow("resim1", res)


cv2.destroyAllWindows()"""