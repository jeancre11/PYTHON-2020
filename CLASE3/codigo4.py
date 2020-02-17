"""USO DE DICCIONARIOS"""
dic1={"x":"HOLA MUNDO" , "y":100, "z":200}
print(type(dic1))
print("DICCIONARIO ES: ", dic1)
#ACCEDER AL VALOR DEL CAMPO "x"
di=dic1["x"]
lista1=[1, 20, 30]
v1=lista1[0]
print(di,v1)
#agregar un nuevo campo o llave
dic1["temperatura"]=35
print("DICCIONARIO NUEVO ES: ",dic1)
#accediendo a cada campo del diccionarios
for llave in dic1:
    print(llave)
#accediendo a cada elemento del diccionarios
for llave in dic1:
    print(dic1[llave])