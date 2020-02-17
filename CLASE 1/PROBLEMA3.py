#PROBLEMA 3
texto="Python 2020"
n=len(texto)
#print(texto.count(texto[7]))
M=[]
for i in range(n):
    a=texto[i]
    valor=texto.count(a)
    M.append(valor)
N=list(texto)
#eliminamos repiticiones de las 2 últimas cifras
for j in range(2):
    M.pop(n-j-1)
    N.pop(n-j-1)
print("LA CANTIDAD DE REPITICIONES POR LETRA ESPECIFICA ES: ")
print(M)
print("LA LISTA CON LAS LETRAS SIN REPITICION ES: ")
print(N)
