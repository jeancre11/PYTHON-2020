def transpuesta(M):
   Nf=len(M)
   Nc=len(M[0])
   N=[]
   for columa in range(Nc):
    N.append([])
   for y in range(Nc):
        for x in range(Nf):
            a=M[x][y]
            #agregamos append
            N[y].append(a)
   return(N)
#-----------#
A=[[1,2,3], [50, 51, 52],[6,4,5]]
print("La matriz es=")
for i in A:
    print(i)
B=transpuesta(A)
print("La transpuesta es=")
for j in B:
     print(j)