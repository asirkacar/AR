import cv2
import numpy as np

blackImage = np.zeros((512,512,3),np.uint8)


cv2.line(blackImage,(0,0),(511,511),(140,0,0),5)
cv2.line(blackImage,(511,0),(0,511),(0,140,0),5)
cv2.imshow("Siyah Ekran",blackImage)
cv2.waitKey(0)
cv2.destroyAllWindows()