import cv2

# Carregar imagem
img = cv2.imread("C:\\Users\\Raldiland C\\OneDrive\\Desktop\\VisaoRLK\\QUESTAO 1\\images1.jpg")

# Exibir imagem em uma janela
cv2.imshow("images1.jpg", img)

# Espera até pressionar uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
