"""USO DEL ITERABLE range"""
#range(valor_inicial, limite_superior.paso)
import  time 
r1=range(0,10,1) #10 9 8 7 ... 1
r2=range(15, 20, 2)
print(r2)
r3=range(1,90, 30) #1, 31, 60
#uso del bucle for
for val in r3:
    print('valor es:', val)
    time.sleep(1.5)
print('fin de codigo')
#librerias
#clase, bool (buleano), int, str (caracteres),float(numeros), list( numeros, string)
#range( limites)
