#----Importar numpy como np
#sys.path se tiene una lista de todas las rutas
#donde se importa un modulo o paquete
import numpy as np
#crear arreglos escalar 1D
a1=np.array(0,dtype=float)
#crea una matriz 1D una lista []
a2=np.array([1,2.0])
s2=a2.shape #filas colummnas
print(type(a1),type(a2))
print("dimension de a1", a1.ndim)
print("dimension de a2", a2.ndim)
#matriz 2D doble lista [[]]
a3=np.array( [[1,2,3],
             [3,5,3],
             [5,8,4],
              [2,4,5]] )
#atributo shape muestra los elementos filas columnas
s3=a3.shape
m3=a3.size
print("dimension de a3", a3.ndim)
print("filas y columnas", s3)
print("total de elementos", m3)
