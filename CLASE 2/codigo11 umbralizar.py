def umbralizar(M1, umbra1):
    #conseguir filas
    Nf=len(M1)
    #conseguir columnas
    Nc=len(M1[0])
    Mv=[]
    #listas vacias
    for filas in range(Nf):
        Mv.append([])
    for x in range(Nf):
        for y in range(Nc):
           if M1[x][y]>=umbra1:
               Mv[x].append(1)
           else:
               Mv[x].append(0)
    return Mv
#definir una matriz M
M=[[200, 10, 30], [10, 80, 0], [1, 20 ,50]]
#invocando la funcion
My=umbralizar(M, 50)
print("MATRIZ INICIAL")
print(M)
print("MATRIZ UMBRALIZADA")
print(My)