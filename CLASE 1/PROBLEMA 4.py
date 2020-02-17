#PROBLEMA 4
archivo=open("temperatura_humedad.txt", "w")
archivo.write("20,80\n30,60\n35,50\n48,49\n30,55\n35,56\n26,63\n38,51\n68,40\n")
archivo.close()
#-----------------------------------#
dat=open("temperatura_humedad.txt",'r')
#se crea una lista por cada fila del archivo.txt
datos=dat.readlines()
dat.close()
print("OBSERVACIONES")
print(datos)
taki=[]
temperatura=[]
humedad=[]
#En cada elemento de la lista, se crea otra nueva lista separada por la coma
for i in datos:
    taki.append(i.split(","))
print(taki)
Nf=len(taki)
Nc=len(taki[0])
for x in range(Nf):
    for y in range(Nc):
        if y==0:
            valor=float(taki[x][y])
            temperatura.append(valor)
        else:
            valor=float(taki[x][y])
            humedad.append(valor)
print("LISTA DE TEMPERATURA: ")
print(temperatura)
print("LISTA DE HUMEDAD: ")
print(humedad)
contador=0
for i in temperatura:
    if i>=30 and i<=50:
        contador+=1
print("MUESTRAS DE TEMPERATURA >=30 Y <=50 ES: ", contador)