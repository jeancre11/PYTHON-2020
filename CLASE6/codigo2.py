"""lectura de imagen"""
import  numpy as np
import cv2
"realizar la lectura de una imagen"
#------BGR---------
img=cv2.imread("C:\\Users\\LENOVO\\Desktop\\CLASES PYTHON\\clase3\\IMAGENGG.jpg")
#determinar dimensiones
dimen=img.ndim
#determinar la forma
forma=img.shape
print("dimensiones:", dimen)
print("forma:", forma)
#matrices de las capas, a
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
cv2.imshow("imagen1", img)
#eliminar capa rojo
img[:,:,2]=0 #revisar
cv2.imshow("imagen sin rojo", img)
#combinacion de  capas
ig=0.29*r+0.58*g+0.114*b
#convertir a entero
i2=np.uint8(ig)
#ECUALIZAR EL HISTOGRAMA
i2e=cv2.equalizeHist(i2)
cv2.imshow("imagen en escala grises", i2)
cv2.imshow("imagen equalizada", i2e)
#calcular el histograma a escala de grises
#histograma muestra los niveles de intensidad vs cantidad de pixeles
#pixel elemento de la matriz Intensidad
#[i2] es la imagen, [0] es valor escala gris, None,
histo=cv2.calcHist([i2],[0],None, [256],[0,256])
histoe=cv2.calcHist([i2e],[0],None, [256],[0,256])
cv2.waitKey(0)
from  matplotlib import pyplot as plt
plt.subplot(121)
plt.plot(histo)
plt.title("HISTOGRAMA")
plt.xlabel("nivel de intensidad")
plt.ylabel("numero de pixeles")
plt.grid()

plt.subplot(122)
plt.plot(histoe)
plt.title("HISTOGRAMA equalizado")
plt.xlabel("nivel de intensidad")
plt.ylabel("numero de pixeles")
plt.grid()
plt.show()


