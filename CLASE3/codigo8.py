"""FUNCION RECTA"""
def linspace(to, tf, N):
    razon=(tf-to)/N
    #primera forma
    lv=[]
    for val in range(N):
        lv.append(to+val*razon)
    lv.append(float(tf))
    return lv
def relu(x):
    l2=[]
    for val in x:
        if val>=0:
            l2.append(val)
        else:
            l2.append(0)
    return  l2
lista=linspace(-20,20,10)
lista2=relu(lista)
print("LA LISTA CON LINSPACE: ", lista)
print("LA MODIFICACION ES: ", lista2)