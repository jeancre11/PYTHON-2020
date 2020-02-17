"""UTILIZAR STRING Y SUS METODOS"""
texto="voltaje, corriente, temperatura, humedad"
print(texto)
#separar cada elemento del texto, con el separador() y devuelve una lista
lista=texto.split(sep=",")
print("LOS ELEMETOS SON: ",lista)
#built-in function
N=len(lista)
print((N))
#------USO DEL MÉTODO JOIN-------#
#metodo string.join
#creacion de una lista con elementos string
lista2=["voltaje", "temperatura", "humedad"]
texto2=",".join(lista2)
print(texto2)
