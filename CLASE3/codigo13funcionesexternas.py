"""Funciones anidadas NESTED FUNCTIONS"""
def funcion_externa():
    print("INICIO DE FUNCION EXTERNA")
    def funcion_interna():
        print("FUNCION INTERNA LLAMADA")
    #llamar  ala funcion_interna
    funcion_interna()
    print("fin de funcion externa")
#invocando a la funcion funcion_externa
funcion_externa()
def polinomio(a,b,c):
    def interna(x):
        valor=a*(x**2)+b*x+c
        return valor
    return interna
#p es una copia de la funcion interna de polinomio
p=polinomio(1,1,1)
print(p(2))
#valores del polinomio de 0 a 10
for val in range(11):
    print(p(val), end=" ")

