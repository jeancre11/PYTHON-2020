#IMPORTAR NUESTRO MODULO codigo8 con fn
import codigo8 as fn
from matplotlib import  pyplot as plt
x=fn.linspace(-10, 10, 200)
#utilizar la funcion relu
y=fn.relu(x)
#graficar resultados
plt.plot(x,y)
plt.title("FUNCION RELU")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

