import PROBLEMA1
from matplotlib import pyplot as plt
x=PROBLEMA1.linspace(-10,20,100) #aumenta de 5 en 5
y=PROBLEMA1.cuadratica(x,5)
plt.plot(x,y)
plt.title("y=(x-xo)^2")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()
