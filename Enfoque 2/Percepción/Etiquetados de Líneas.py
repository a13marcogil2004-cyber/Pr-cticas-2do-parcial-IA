import cv2
import numpy as np

img = cv2.imread("imagen.jpg", 0)

edges = cv2.Canny(img, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)

img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_color, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Lineas detectadas", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()