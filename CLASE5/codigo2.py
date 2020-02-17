"""crear arreglo de 3 dimensiones"""
import numpy as np
a2d=np.array([ [3,4],
               [5 ,6] ])
s2=a2d.shape
#numero de fila
nf=s2[0]
#numero de columnas
nc=s2[1]
#acceder a la posicion 1,1
a11=a2d[1][1]
#acceder a toda la primera fila
af1=a2d[0][:]
print("matriz 2d",a2d)
print("toda fila", af1)
a3d=np.array([  [[5,6],[7,8]], [[1,2],[4,5]]  ])
print(a3d)
print("numero de dimensiones:", a3d.ndim)
#acceder a la primera capa del arreglo a3d
capa1=a3d[0][:][:]
capa2=a3d[1][:][:]
print(capa1+capa2)