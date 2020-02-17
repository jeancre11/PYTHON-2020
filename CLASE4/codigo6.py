"""metodo especial __add___"""
#hemos visto metodos mágicos
a=10
b=20
c=a+b
class punto():
    #se inicio apenas corre el programa
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        a=self.x+other.x
        b=self.y+other.y
        return (a,b)
t1=punto(3,5)
t2=punto(1,5)
s1=t1+t2
print(s1)
