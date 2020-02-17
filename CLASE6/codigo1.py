""" RELACION ARDUINO Y PYTHON"""
""" WITH PYSERIAL AND NUMPY"""
#INSTALAR DESDE CMD "pip install pyserial"
import numpy as np
a1=np.array([[1,2],
    [3,4]])
print("dimensiones de a1 es:", a1.ndim )
print("forma de a1 es:", a1.shape)
a2=np.array([[10,20],
             [1,0]])
print(a2)
print("dimensiones de a2:", a2.ndim)
#orden mxn 2D para 3D con capas
print("forma de a2 es:", a2.shape)
#accediendo a todos los elementos de la primera fila
c1=a2[0,:]
print("la primera fila es:",c1)
#accediendo a la columna
c2=a2[:,0]
print("la primera columna:",c2)
#PARA EL CASO DE 3D a3.shape (capas, filas, columnas)
