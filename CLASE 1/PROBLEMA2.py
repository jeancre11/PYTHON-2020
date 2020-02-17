#PROBLEMA 2
base=int(input('INGRESAR BASE='))
altura=int(input('INGRESAR ALTURA='))
if base==altura:
    print("Perfecto los valores coinciden")
    for x in range(altura):
        print((x+1)*'*'+(base-x-1)*' ')
else:
    print("Los valores no son iguales, intentar de nuevo")
