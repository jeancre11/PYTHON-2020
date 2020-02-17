def umbralizar(M1, umbra1):
    #conseguir filas
    Nf=len(M1)
    print(Nf)
    #conseguir columnas
    Nc=len(M1[0])
    print(Nc)
    Mv=[]
    for filas in range(Nf):
        Mv.append([])
    for x in range(Nf):
        for y in range(Nc):
           if M1[x][y]>=umbra1:

               Mv[x].append(1)
           else:
               Mv[x].append(0)
    return Mv
M=[[1,2,4],[1,3,55]]
x=umbralizar(M,50)
print(x)
