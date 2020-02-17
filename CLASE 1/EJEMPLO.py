#SE CREA LA LISTA

def promedios(list):

    suma=0
    n=len(list)
    for val in list:
        su=val+suma
        suma=su
    prom=su/n
    return prom
#----------------------------------#
lista=[10, -2, 4,5,6]
print(lista)
promed=promedios(lista)
print('el promedio es=',promed)
list2=[]
for i in lista:
    list2.append(i-promed)

print('LA NUEVA LISTA=',list2)

