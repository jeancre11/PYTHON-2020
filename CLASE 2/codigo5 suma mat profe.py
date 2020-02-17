#matriz 2x2
l1=[[10,50,3],
    [1, 2, 3]]
l2=[[12,50,5],
    [0,1,1]]
#realizar suma elementos
suma=0
Nf=len(l1)
print(Nf)
Nc=len(l1[0])
print(Nc)
import time
M3=[]
#print(range(Nf))
#añadir la misma cantidad de filas a la matriz M3
for fila in range(Nf):
    M3.append([])
#para cada fila
for x in range(Nf):
    #cada columna
    for y in range(Nc):
        #multiplicar elemento a elemento L1 y L2
        multi=l1[x][y]*l2[x][y]
        #agregar a la matrzi m3 el valor encontrado
        M3[x].append(multi)
        print(multi, end=" ")
        time.sleep(1.5)
    print("")
print(M3)
