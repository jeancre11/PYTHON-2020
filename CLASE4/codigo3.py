"""uso de clases para realizar operaciones sobre matrices"""
class Array():
    def __init__(self,M1,M2):
        #creando atributos
        self.Nf1=len(M1)
        self.Nf2=len(M2)
        self.Nc1=len(M1[0])
        self.Nc2=len(M2[0])
        #definiendo atributo matriz1, matriz2
        self.matriz1=M1
        self.matriz2=M2
    def binarizar(self, umbral1):
        L=[]
        #agregando Nf1 filas a la lista L
        for valor in range(self.Nf1):
            L.append([])
        #para cada fila
        for x in range(self.Nf1):
            for y in range(self.Nc1):
                if self.matriz1[x][y]>=umbral1:
                    L[x].append(1)
                else:
                    L[x].append(0)
        return L
    def multiplicacion(self):
        #crear una lista vacia
        m3=[]
        if self.Nc1==self.Nc2 and self.Nf1==self.Nf2:
            for a in range(self.Nf1):
                m3.append([])
            for r in range(self.Nf1):
                for c in range(self.Nc1):
                    m3[r].append(self.matriz1[r][c]*self.matriz2[r][c])
            return m3
        else:
            print("error de dimensiones")
            return none


m1=[[30, 5],
    [20, 1]]
m2=[[10, 5],
    [2, 10]]
#crear objeto
dat=Array(m1,m2)
#uso del metodo binarizar del objeto dat
m3=dat.binarizar(18)
print(m3)
m4=dat.multiplicacion()
print(m4)
    #def multiplicacion(self):
        #pass
