import cv2


#------------------------VİDEO KAYIT ALMA-------------------------

camera = cv2.VideoCapture(0)

codec = cv2.VideoWriter_fourcc(*'XVID')
bosSablon = cv2.VideoWriter("denemeKayit.mp4", codec, 30.0, (640,480))

while camera.isOpened():
    deger, goruntu = camera.read()

    if not deger:
        print("görüntü alınamıyor")
        break
    bosSablon.write(goruntu)

    cv2.imshow("VideoKayit", goruntu)
    if cv2.waitKey(1) == ord("q"):
        print("kapatıldı")
        break
camera.release()
bosSablon.release()
cv2.destroyAllWindows()


"""
#------------VİDEODAN GÖRÜNTÜ ALMA----------------------

vid = cv2.VideoCapture("3_(Python)_giris.mp4")

while vid.isOpened():
    deger, goruntu = vid.read()
    goruntu = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    if not deger:
        print("görüntü alınamıyor")
        break

    cv2.imshow("Video Penceresi", goruntu)
    if cv2.waitKey(1) == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()
"""




"""
-------------------KAMERADAN GÖRÜNTÜ ALMA-------------------
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("görüntü alınamıyor")
    exit()

print(camera.get(3))
print(camera.get(4))
camera.set(3, 320)
camera.set(4, 240)
print(camera.get(3))
print(camera.get(4))


while True:
    deger, goruntu = camera.read()
    #goruntu = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    if not deger:
        print("görüntü yok")
        break
    cv2.imshow("Goruntu", goruntu)

    if cv2.waitKey(1) == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()"""