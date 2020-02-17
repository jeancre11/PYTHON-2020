"""EJEMPLO DE DICCIONARIO"""
import time
t1=(20, 30, 40, 25) #Clase tupla
h1=(70, 65, 50, 75)
print(type(t1))
print(t1[0])
dic={"temperatura":[], "humedad":[]}
for elemento in dic:
    for valor in range(len(t1)):
        if elemento=="temperatura":
             dic[elemento].append(t1[valor])
             print(dic[elemento])
             time.sleep(2)
        else:
             print(dic[elemento].append(h1[valor]))
             print(dic[elemento])
             time.sleep(2)
print(dic)