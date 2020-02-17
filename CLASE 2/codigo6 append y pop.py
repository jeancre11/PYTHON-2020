lista1=[30, 40, 50,100,200,30]
var1=int(input("ingresar un dato"))
#objeto.metodo(argumento)
lista1.append(var1)
lista1.append(var1+100)
print("LISTA ACTUALIZADA=", lista1)

#--------------------------------------------#
print(lista1[2])
#COMIENZA DE CERO HASTA (N-1)
print(lista1[1:4:1])
#UTILIZAR EL METODO POP, QUITA ELEMENTOS
indice=int(input("POSICION A QUITAR="))
valor=lista1.pop(indice)
print("valor es=",valor)
print("Lista Actual=", lista1)
l1=[10, 20.5, "hola", [1,2,3]]
l2=[10, 20,30]
