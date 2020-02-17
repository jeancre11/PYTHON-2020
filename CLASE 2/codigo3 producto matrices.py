def productomatriz(A,B):
   Nfa=len(A)
   Nca=len(A[0])
   Nfb= len(B)
   Ncb= len(B[0])
   C=[]
   if Nca==Nfb:
       for elemento in range(Nfa):
           C.append([])
       for x in range(Nfa):
              for y in range(Ncb):
                  suma=0
                  for xpory in range(Nca):
                     suma=suma + A[x][xpory]*B[xpory][y]
                     #suma=d
                     #agregamos append
                  C[x].append(suma)
       return(C)
   else:
       print("NO SE PUEDE REALIZAR EL PRODUCTO")
#-----------#
A=[[1,2,3],
   [0,2,1],
   [0,0,2]]
B=[[1,0,3],
   [1,4,2],
   [4,0,0]]
M=productomatriz(A,B)
print("El producto es=")
for i in M:
    print(i)