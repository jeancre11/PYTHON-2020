"""mqnejo de errores en python"""
import  sys
try:
    a=float(input("dato 1:" ))
    b=float(input("dato 2"))
    c=a/b
    print("division es:", c)
except:
    print("se encontro un error en el try")
    print(sys.exc_info())
finally:
    print("bloque finally ejecutandose")