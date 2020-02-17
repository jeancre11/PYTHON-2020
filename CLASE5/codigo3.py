"""PROCESAMIENTO DE IMAGENES"""
#CADA UNIDAD DE LA IMAGEN PIXEL
#CADA PIXEL TIENE 8 BYTES #2^8-1
import  numpy as np
import cv2
img=cv2.imread("C:\\Users\\LENOVO\\Desktop\\CLASES PYTHON\\clase3\\IMAGENGG.jpg")
print(type(img))
#REALIZAR EL CAMBIO DE ESCALA DE COLOR
grises=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#---Operacion para elevar el brillo de una imagen---
grises2=grises+50
print("forma de la imagen:", np.shape(img))
print("forma imagen gris:", np.shape(grises))
#filas, columnas, capas el numpy array python
#capa, fila, columna en otros sofware
#img[:][:][0] accediendo a la capa0
cv2.imshow("imagen en la escala rgb", img)
cv2.imshow("imagen en escala gris:", grises)
cv2.imshow("imagen en escala gris:", grises2)

cv2.waitKey(0) # se deja en la ventana hasta presionar un boton
print("fin del programa")

cv2.destroyAllWindows()