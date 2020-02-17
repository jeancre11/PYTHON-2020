"""uso del bucle for"""
lista1=[10, 20 ,30, 40]
#uso del bucle for
#IMPORTAR LA LIBRERIA TIME
import time
for var in lista1:
    if var>20:
        break
    #espaciado IMPORTANTE
    print(var)
#añadimos un temporisador
    time.sleep(2)
    
    #el tiempo en procesar dato
print('fin del codigo')
