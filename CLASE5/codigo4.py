"""proc. de imagenes"""
import  numpy as np
from matplotlib import pyplot as plt
import cv2
img=cv2.imread("C:\\Users\\LENOVO\\Desktop\\CLASES PYTHON\\clase3\\IMAGENGG.jpg")
#convertir a escala grises
grises=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#determinar su histograma
histo=cv2.calcHist([grises],[0],None,[256],[0,256])
grises2=grises+50
histo2=cv2.calcHist([grises],[0],None,[256],[0,256])
cv2.imshow("imagen gray1:", grises)
cv2.imshow("imagen gray 2", grises2)
cv2.waitKey(0)
#PLOTEAT HISTOGRAMA
plt.subplot(121)
plt.plot(histo)
plt.title("histograma 1")
plt.xlabel("nivel de intensidad")
plt.ylabel("numero de pixeles")
#------------
plt.subplot(122)
plt.plot(histo2)
plt.title("histograma 2")
plt.plot(histo2)
plt.title("histograma 2")
plt.xlabel("inten")
plt.ylabel("pixeles")
plt.show()

















