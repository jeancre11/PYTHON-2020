"""CREANDO CLASES"""

class clasegg():
    def __init__(self,x):
        self.long=len(x)
        self.equis=x
    def calcular_promedio(self):
        #hallamos la media
        suma=0
        for i in self.equis:
            self.summa=i+suma
            suma=self.summa
        return self.summa/self.long
    def normalizar(self):
        #hallamos la desviación estandar
        suma=0
        for y in self.equis:
            self.summa=(y-self.calcular_promedio())**2+suma
            suma=self.summa
        self.desv=(self.summa/self.long)**(1/2)
        print("desviacion estandar de x:", self.desv)
        #HALLAMOS LA TIPIFICACIÓN DE VARIABLES N(0,1) "Normalización"
        self.A=[]
        for val in self.equis:
            self.A.append((val-self.calcular_promedio())/self.desv)
        return self.A
    def crear_archivo(self):
        self.dat=open("clasegg.txt","w")
        #convertimos los datos numéricos a clase string
        a=str(self.normalizar())
        self.datos=self.dat.write(a)
        #se guarda los datos normalizados
        self.dat.close()
        return self.datos
#------------------------------------------------#
x=[3, 5, 2, 6]
dat=clasegg(x)
u=dat.calcular_promedio()
print("La media de x es:",u)
dess=dat.normalizar()
print("la nueva lista con media cero y desviacion 1:",dess)
archivo=dat.crear_archivo()



