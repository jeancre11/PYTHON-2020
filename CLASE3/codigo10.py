def logistic(x):
    y1=[]
    for valor in x:
           y1.append(1/(1+(2.17)**(-valor)))

    return y1
def escalon(x):
    y2=[]
    for valor in x:
       if valor<=0:
           y2.append(0)
       else:
           y2.append(1)
    return y2