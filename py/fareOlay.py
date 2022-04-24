import cv2
import numpy as np

mod = True
cizim = False
xi, yi = -1, -1

def draw(event, x, y, flags, param):
    global xi, yi, mod, cizim

    if event == cv2.EVENT_LBUTTONDOWN:
        cizim = True
        xi, yi = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim == True:
            if mod:
                cv2.circle(bosEkran, (x,y) , 10, (255,0,0), -1)
            else:
                cv2.rectangle(bosEkran, (xi, yi), (x,y), (255,140,0), -1)
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP:
        cizim = False

bosEkran = np.ones((1024,1024,3),np.uint8)

cv2.namedWindow("Boş Ekran")
cv2.setMouseCallback("Boş Ekran", draw)

while (1):
    cv2.imshow("Boş Ekran", bosEkran)
    if cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()