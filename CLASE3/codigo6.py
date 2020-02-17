"""FUNCIONES EN PYTHON"""
val=20.2022
val2=format(val,".2f")
print(val2)

def area_circulo(radio):
    area=3.14*radio**2
    return format(area,".2f")
area=area_circulo(5)
print("EL AREA ES: ", area, "m")
def perimetro_circulo(radio):
    perimetro=2*3.14*radio
    return format(perimetro, ".2f")
peri=perimetro_circulo(5)
print(peri, "m")
def ari(radio):
    a=area_circulo(radio)
    b=perimetro_circulo(radio)
    return a,b
area, perimetro=ari(5)
print("EL AREA: ",area)
print("EL PERIMETRO: ", perimetro)

