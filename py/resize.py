import cv2
import numpy as np
img = cv2.imread("21.jpg")

res = cv2.resize(img, (300, 300)) #300e 300 boyutlandırdık dsize bizim vermek istediğimiz boyut
res2 = cv2.resize(img, None, fx=1.5, fy=1.5)   #resmin x ve y sini 1.5 ile çarparak buyutunu büyüttük
res3 = cv2.resize(img, None, fx=1.5, fy=1, interpolation=cv2.INTER_CUBIC) #matris çarpımlarına göre işlem ayarlayabiliyon
                                                                          #en düzgün sonuc cubicteymiş
                                                                          #bir iteresyon yöntemi yani çarpım yöntemiymiş

"""------------------------TAŞIMA YER DEĞİŞTİRME İŞİ TRANSLATION XY KOORDİNATLARI ÜZERİNDE------------------------"""""

#X DE XDE KAYMASI GEREKEN PİKSEL SAYISINI Y DE YDE KAYMASI GEREKEN PİKSEL SAYISINI YAZIYOZ
#BUNLAR MATRİSLER ÜZERİNDE GERÇEKLEŞTİĞİ İÇİN NUMPY KULLANCAZ
#M=[1 0 tx]
#  [0 1 ty] bu m matrisindeki çarpmaya göre resmi taşıma yapcaz

row, cols = img.shape[:2] #yani ilk ikisini al 512 512 sini al 3ü alma yani kaç resim kanallı olduğunu

transaction_matrix = np.float32([[1, 0, 50],
                                [0, 1, 50]]) #resmi x ve y de 50 piksel kaydırdık
#BU MATRİSİ AŞŞAĞIDAKİ FONKSİYON YARDIMIYLA ÇARPIM YAPCAZ yani ana resimle çarpacaz TAŞIMIŞ OLCAZ

transaction_img = cv2.warpAffine(img, transaction_matrix, (cols, row)) #bide iterasyon alıyo cubic şeklindemi çarpacan başka türlü diyemi yapmadık
transaction_img1 = cv2.warpAffine(img, transaction_matrix, (cols+50, row+50)) #bunu yapınca kırpılmadan resim görünür

transaction_matrix1 = np.float32([[1, 0, 25],
                                [0, 1, 25]])  #burda 25e 25 kaydırdık aşşağıda da çerçeveyi 50 piksel büyütünce ortalanmış oldu
                                            #eğer matriste -50 yazarsan sola 50 kayar
transaction_img2 = cv2.warpAffine(img, transaction_matrix1, (cols+50, row+50)) #bunla resim ortalanmış oldu

"""------------------------DÖNDÜRME İŞLEMİ------------------------"""

rotation_matrix = cv2.getRotationMatrix2D((cols/2, row/2), 50, 0.7) #ilk döndürme merkezimizi yazıyoz yani hangi noktadan döndürecez sonra kaç derece
                                                                #son değer ise ne kadarlık küçültme uygulayacağımız giriyoz 0.7 yazarsak yüzde 30 küçülmiş olcaz
rotation_img = cv2.warpAffine(img, rotation_matrix, (int(cols*1.2), int(row*1.2)))

"""------------------------ ÇARPITMA getaffinetransform İŞLEMİ"""

"""
değerleri alırken şu şekil düşün resmi köşelerini [y,x] cols row olarak
                                                  [y,x]

3NOKTA SEÇİYORUZ BUNLARI MATRİSE ATIYORUZ
SONRADA BU SEÇTİĞİMİZ 3 NOKTAYA İŞLME YAPACAĞIMIZ MATRİSİ OLUŞTURUYORUZ

resmin matrisleri şu şekil [ 0123456]
                           [0.......]
                           [1.......]
                           [2.......]
                           [3.......]
                           [4.......]
                           [5.......]
                           [6.......] resmin matris tablosu bu şekilde noktaların olduğu taraflar piksellerin koordinatları oluyo 
                                      soldan sağa x yukardan aşağı y ---bu normalde (7,7lik bi resim olur bir eksiği alınır )
"""

src_points = np.float32([[0, 0],
                         [cols-1, 0],
                         [0, row-1]])
dst_points = np.float32([[0, 0],
                         [int(0.6*(cols-1)), 0],
                         [int(0.4*(cols-1)), row-1]])
affine_matris = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matris, (cols, row))

"""------------------------ ÇARPITMA getaffinetransform İŞLEMİ 2-----------------------"""
src_points1 =np.float32([[0, 0],  #sol üst köşe
                         [cols-1, 0], #sağ üst köşe
                         [0, row-1],  #sol alt köşe
                         [cols-1, row-1]])  #sağ alt köşe
dst_points1 = np.float32([[0, 0],
                         [cols-1, 0],
                         [int(0.33*(cols-1)), row-1],
                         [int(0.66*(cols-1)), row-1]])
gettransform_matris = cv2.getPerspectiveTransform(src_points1, dst_points1)
output_img1 = cv2.warpPerspective(img, gettransform_matris, (cols, row))


"""-------------------------UYGULAMA--------------------------"""
img1 = cv2.imread("sw.jpg")
row1, cols1 = img1.shape[:2]
src_points2 =np.float32([[146, 74],         #bu kısımda önc noktaları seçiyoz
                         [430, 76],
                         [107, 317],
                         [478, 315]])
dst_points2 = np.float32([[0, 0],       #Bu kısımda üstteki seçtiğimiz noktaların yeni yerlerini seçiyoz yani nere gelecekelrini
                         [cols1-1, 0],
                         [0, row1-1],
                         [cols1-1, row1-1]])
gettransform_matris1 = cv2.getPerspectiveTransform(src_points2, dst_points2)
output_img2 = cv2.warpPerspective(img1, gettransform_matris1, (cols1, row1))

#cv2.imshow("resim", res)
#cv2.imshow("resim2", res2)
#cv2.imshow("resim3", res3)
#cv2.imshow("resim4", transaction_img)
#cv2.imshow("resim5", transaction_img1)
#cv2.imshow("resim6", transaction_img2)
#cv2.imshow("resim7", rotation_img)
#cv2.imshow("resim8", output_img2)
cv2.waitKey()
cv2.destroyAllWindows()
"""--------------------UYGULAMA2---------------------------"""

img2 = cv2.imread("sw.jpg")
row2, cols2 = img2.shape[:2]
click_count = 0
a = []
dst_points2 = np.float32([[0, 0],
                         [cols2-1, 0],
                         [0, row2-1],
                         [cols2-1, row2-1]])
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
def draw(event, x, y, flags, param):
    global click_count, a

    if click_count < 4:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            click_count += 1
            a.append((x,y))
    else:
        src = np.float32([
            [a[0][0], a[0][1]],   #a nın ilk tıklamasının xinin 0ıncısı ve ilk tıklamasının ysinin 0ıncısı
            [a[1][0], a[1][1]],   #a nın ikinci tıklamasının xinin ikinicisi ve ikinici tıklamasının ysinin ikinicisi
            [a[2][0], a[2][1]],   #a nın soldakileri tıklanma sayısını sağdakilerde x ve ysini belirtiyo x=0 y=1 anlamında
            [a[3][0], a[3][1]]])
        click_count = 0
        a = []

        M = cv2.getPerspectiveTransform(src, dst_points2)
        output1 = cv2.warpPerspective(img2, M, (cols2, row2))
        cv2.imshow("output", output1)
cv2.setMouseCallback("img",draw)

while(1):
    cv2.imshow("img", img2)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()


