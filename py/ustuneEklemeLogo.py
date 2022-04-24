import cv2

img = cv2.imread("cv2.png")
img2 = cv2.imread("asel1.jpg")

x, y, z = img.shape
roi = img2[0:x, 0:y]

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_bg = cv2.bitwise_and(img, img, mask=mask)
img_fg = cv2.bitwise_and(roi, roi, mask=mask_inv)


toplam = cv2.add(img_fg, img_bg)

img2[0:x, 0:y] = toplam

cv2.namedWindow("resim1",cv2.WINDOW_NORMAL)
cv2.imshow("resim1", img2)
cv2.imshow("resimBG", img_bg)
cv2.imshow("resimFG", img_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()