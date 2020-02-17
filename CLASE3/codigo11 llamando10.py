"""FUNCIONES GRAFICOS"""
import codigo10 as fn
from matplotlib import  pyplot as plt
from codigo8 import linspace
x=linspace(-10,10,100)
print(x)
y1=fn.logistic(x)
y2=fn.escalon(x)
plt.plot(x,y1)
plt.title("FUNCION RELU")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
#------------------------------#
plt.plot(x,y2)
plt.title("FUNCION RELU")
plt.xlabel("x")
plt.ylabel("y")
plt.show()