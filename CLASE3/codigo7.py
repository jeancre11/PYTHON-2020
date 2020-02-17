"""LINSPACE"""
def linspace(to, tf, N):
    razon=(tf-to)/N
    #primera forma
    lv=[]
    for val in range(N):
        lv.append(to+val*razon)
    lv.append(tf)
    return lv
#creando una lista desde el valor to hasta tf con N valores
#linspace(to, tf, N)
l1=linspace(0, 20, 4)
print(l1)