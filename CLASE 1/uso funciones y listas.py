#se crea la funcion
#----------------------------------------#
def lista_cuadrada(x):
#uso del bucle for
    lista2=[]
    for val in x:
        #agregar cada valor
       lista2.append(val**2)
    #retornar la nueva lista2, cada elemento al cuadrado
    return lista2
#---------------------------------------#
lista1=[10, 5, 20]
#usar la funcion lista_nueva()
#invocar funcion
list=lista_cuadrada(lista1)
print('lista1 es:',lista1)
print('lista nueva:', list)