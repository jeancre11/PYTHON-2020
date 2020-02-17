import numpy as np
a1=np.array([[200,30],[50,100]])
b1=np.array([[10,10],[1,1]])
#multiplicación elemento a elemento
c1=a1*b1
#multiplicación matricial
d1=np.matmul(a1,b1)
print(c1)
print(d1)
#la función where
a2=np.where(a1>=60,255,0)
print("MATRIZ a1 es : \n",a1)
print("MATRIZ a2 es ; \n ",a2)