import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("ang.jpg")
blue = [255, 0, 0] #rgb formatınaa göre
#opencv bgr matplotlib rgb formatına göre çalıştığı için kırmızılar mavi maviler kırmızı olarak algılanır
"""
kirp = resim[500:800,500:800] #x=500ile 800 arası, y=500ile 800 arasını kırp

resim[682:982, 257:557] = kirp #kirptiğim nesneyi resmin üstüne yerleştirmiş oldum

b = resim[:,:,0] #burda resmin 0ıncı kanalını al anlamına geliyo yani b g r daki byi al diyo :,: yerleri x y ler oluyo
resim[:,:,2] = 0 #tüm kanalları al 2. kanalı 0 yap yani siyah

plt.subplot(121) #bir satır 2 sütundan oluşan yerin 1incisi oraya altındaki resim kısmını koy diyo
plt.imshow(resim)
plt.subplot(122) #bir satır 2 sütundan oluşan yerin 2incisi oraya altındaki kirp kısmını koy diyo yani tek ekranda hem eskisi hem yenisini görüntüledik
plt.imshow(kirp)
plt.show()"""

#--------------------------çerçeve ekleme------------------------

replicate = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_REPLICATE) #ilki hangi resim onu diyo diğerleri sağdan soldan vs kap piksel olcak onu diyo
reflect = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(resim, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=blue)

plt.subplot(231), plt.imshow(resim), plt.title("ORGINAL")
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()
