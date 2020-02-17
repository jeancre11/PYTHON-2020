#PROBLEMA 1
base=int(input('INGRESAR BASE='))
altura=int(input('INGRESAR ALTURA='))
#uso del range y el for

for y in range(altura+1):
     if y==0 or y==altura:
          print(base*'*')
     else:
          print(1*'*'+(base-2)*' '+1*'*')


