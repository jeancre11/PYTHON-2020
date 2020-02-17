from PROBLEMA1 import linspace
from matplotlib import pyplot as plt
def funcion2(x):
    y=[]
    for valor in x:
        if valor>=0:
            y.append(1/(1+2.71**(-valor)))
        elif valor>=-2 and valor<0:
            y.append(0.1*valor)
        else:
            y.append(0)
    return  y
#-------------------------#
x=linspace(-4,4,100)
y=funcion2(x)
plt.plot(x,y)
plt.title("Función problema 2")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

