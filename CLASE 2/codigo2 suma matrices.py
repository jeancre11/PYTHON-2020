#MATRIZ 2X2
l1=[[10,0],
    [20,15]]
l2=[[3,2],
    [5,10]]
Nf=len(l1)
Nc=len(l1[0])
suma=0
S=[]
"""suma de matrices"""
for fila in range(Nf):
    S.append([])
for x in range(Nf):
    print(l1[x], end=" ")
    print(l2[x])
    for y in range(Nc):
       sumaa=l1[x][y]+l2[x][y]
       S[x].append(sumaa)
print("La suma es=",S)


