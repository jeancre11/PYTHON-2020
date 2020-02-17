lista=[100, 20, 21, 23, 24]
#lista_impar 21 23
#lista_para 10 20 24
cond=23 in lista
lista_par=[]
lista_impar=[]
#devuelve true o false para el elemento
print(cond)
print(lista)
for  val in lista:
    #print(val, end=" ")
    if val%2!=0:
        break
    print(val, end=" ")
print("")
    #print("AHORA TENEMOS")
#lista=[100, 20, 21, 23, 24]
for val in lista:
    if val%2==0:
        lista_par.append(val)
    else:
        lista_impar.append(val)
print(lista_par)
print(lista_impar)

