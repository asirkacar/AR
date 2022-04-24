import cv2, numpy as np

def nothing():
    pass

bosEkran = np.zeros((512,512,3), np.uint8)

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

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()