#CLASE CONTIENE OBJETOS
#METODOS: SON FUNCIONES, ATRIBUTOS: CARACTERISTICAS DE UAN CLASE
"""CREACION DE CLASES EN PYTHON"""
if __name__=="__main__":
    print("CODIGO EJECUTADO DE FORMA DIRECTA")
    class rectangulo():
        def area(self,n):
            #estamos creando un atributo de instancia
            #Area
            self.Area=n
            def mostras_area(self):
               print("area es:",n)
    #crwado una instancia, no cuenta argumento
    r1=rectangulo()
    #acceder al metodo instancia del objeto r1
    r1.area()
    #crear otro objeto
    r2=rectangulo()
    #acceder al metodo de instancia del objeto r2
    r2.area()
else:
    print("no se ejecuta en forma directa")