import cv2

img = cv2.imread('C:\\Users\\Raldiland C\\OneDrive\\Desktop\\VisaoRLK\\QUESTAO 5\\images5.jpg')
negativo = 255 - img

cv2.imshow("Original", img)
cv2.imshow("Negativo", negativo)
cv2.waitKey(0)
cv2.destroyAllWindows()
