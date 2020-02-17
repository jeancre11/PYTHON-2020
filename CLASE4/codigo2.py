"""definir un clase circulo y el metodo construccion"""
class circulo():
    #con init incia instantaneamente al correr el programa
    #atributos name y radio
    def __init__(self, nombre, radio):
        print("objeto creado 2020: ", nombre)
        #definir atributo de instancia llamado name
        self.name=nombre
        self.radius=radio
        #creando metodos
    def __str__(self):
        return "SOY UN OBJETO Y ME LLAMO"+self.name
    def area_circulo(self):
        #3.14*(r)**2
        return 3.14*(self.radius**2)
    def mitad_area(self):
        return self.area_circulo()/2
c1=circulo("jorgue",5)
#c2=circulo("python")
#accediendo al atributo name del objeto c2
dato=c1.name
print(dato)
area=c1.area_circulo()
print("area es:", area)
mitad=c1.mitad_area()
print(mitad)