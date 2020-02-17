"""sentencia if"""
a=float(input('ingresa dato 1='))
b=float(input('ingresa dato 2='))

#comparaciones
if a>b:
    print('a es mayor de b')
else:
    print('a es menor o igual que b')
#determinar si es multiplo de 2
if a%2==0 and a>30:
    print('la variable a es multiplo de 2 y mayor que 30')
else:
    print('la variable es impar')
if a!=10:
    print('a es diferente de 10')
else:
    print('mentira, es igual a 10')
