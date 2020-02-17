from PROBLEMA1 import linspace
from matplotlib import pyplot as plt
def funcion3(x):
    def media(v):
        u=sum(x)/len(x)
        def desviacion(i):
            sumas = 0
            for valor in x:
                 sumar=(valor-u)**2+sumas
                 sumas = sumar
            desv = (sumar / len(x)) ** (1 / 2)
            y=[]
            for val in x:
                a=2.71**(-(val-u)**2/(2*desv**2))/((2*3.14)**(1/2)*desv)
                y.append(a)
            return y
        return desviacion
    return media
x=linspace(-10,20,100)
y=funcion3(x)
print("dimensiones X e Y")
a=len(y(0)(0))
print(a, len(x))
plt.plot(x,y(0)(0))
plt.title("GAUSS problema 3")
plt.xlabel("variable x")
plt.ylabel("variable y")
plt.show()