import cv2
import numpy as np

img = cv2.imread("imagen.jpg")

kernel = np.ones((3,3), np.float32) / 9

filtro = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Filtrada", filtro)
cv2.waitKey(0)
cv2.destroyAllWindows()