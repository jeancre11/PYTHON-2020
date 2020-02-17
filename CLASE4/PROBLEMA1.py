""" PROBLEMA NÚMERO 1"""
from matplotlib import pyplot as plt
#COLOCAR LA UBICACIÓN DEL ARCHIVO TEXTO "datos_velocidad.txt"
dat=open("C:\\Users\\LENOVO\\Desktop\\CLASES PYTHON\\clase4\\datos_velocidad.txt","r")
datos=dat.readlines()
dat.close()
#ELIMINAMOS LA PRIMERA LISTA, EL CUAL CONTIENE LAS PALABRAS TIEMPO Y VELOCIDAD
datos1=datos.pop(0)
print("eliminado:",datos1)
A=[]
tiempo=[]
velocidad=[]
#HACEMOS QUE CADA ELEMENTO DE "datos" SEA UNA LISTA SEPARADOS POR ","
for i in datos:
    A.append(i.split(","))
#REALIZAMOS LAS LISTAS DE TIEMPO Y VELOCIDAD
Nf=len(A)
Nc=len(A[0])
for x in range(Nf):
    for y in range(Nc):
        if y==0:
            valor=float(A[x][y])
            tiempo.append(valor)
        else:
            valor=float(A[x][y])
            velocidad.append(valor)
print("LISTA DE TIEMPO: ")
print(tiempo)
print("LISTA DE VELOCIDAD: ")
print(velocidad)
plt.grid()
plt.plot(tiempo,velocidad)
plt.title("VELOCIDAD EN RPM vs TIEMPO")
plt.xlabel("tiempo")
plt.ylabel("velocidad (rpm)")
plt.show()


