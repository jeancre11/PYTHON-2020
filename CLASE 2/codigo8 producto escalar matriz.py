#MATRIZ 2X2
lis=[[10, 50], [20, 15]]
#realizamos el producto
pro=1
for val1 in lis:
    print(val1)
    for val2 in val1:
       multipli=pro*val2
       pro=multipli
print("RESPUESTA ES=")
print(multipli)