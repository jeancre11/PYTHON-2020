def linspace(to, tf, N):
    razon=(tf-to)/N
    #primera forma
    lv=[]
    for val in range(N):
        lv.append(to+val*razon)
    lv.append(tf)
    return lv
def cuadratica(x,xo):
    y=[]
    for valor in x:
        y.append((valor-xo)**2)
    return y
#------------------#


