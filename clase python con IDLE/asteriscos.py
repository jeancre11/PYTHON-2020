#Uso de bucle for ejemplo gg
#convertir str a string
altura=int(input('ingresa el nivel='))
#uso del range y el for
for nivel in range(altura):
    print( (altura-nivel-1)*' '+(2*(nivel+1)-1)*'*'+(altura-nivel-1)*' ')
