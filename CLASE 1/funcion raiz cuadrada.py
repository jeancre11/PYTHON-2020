def lista_cuadrada(x,n):
#uso del bucle for
    lista2=[]
    for val in x:
        #agregar cada valor
       lista2.append(val**(1/n))
    #retornar la nueva lista2, cada elemento al cuadrado
    return lista2
#AÑADIR lista2, n (TE DA DOS RESPUESTAS)
#---------------------------------------#
lista1=[8, 1000, 64]
#usar la funcion lista_nueva()
#invocar funcion
list=lista_cuadrada(lista1,3)
#AQUI PONES list, exponente (las dos funciones)
print('lista1 es:',lista1)
print('lista nueva:', list)