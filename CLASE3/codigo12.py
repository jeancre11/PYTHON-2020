"""" uso basico de numpy y funciones anidadas"""
import numpy as np
#crear un arreglo del tipo numpy.ndarray de 1 dimension
a1=np.array([1,2,3])
b1=np.array([2,4,6])
c1=a1+b1
c2=5*b1
print("suma:",c1, "producto:", c2)
#EL PRODUCTO INTERNO ES
producto=np.dot(a1,b1)
print(producto)
#crear un arreglo del tipo numpy.ndarray de 2 dimensiones
