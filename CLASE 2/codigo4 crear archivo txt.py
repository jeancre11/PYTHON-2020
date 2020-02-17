import os
import time
#crear un archivo de texto
#archivo=open("sensor.txt", "w")
archivo=open("dat.txt", "w")
#se crea contenido en el archivo.txt
archivo.write("1 2 3 4 5\n2 1 4 5 7 \n")
archivo.close()
#cierras archivo
time.sleep(2)
os.system("dat.txt")
contenido=os.listdir()
print(contenido)
if "carpeta" in contenido:
    print("esta carpeta ya existe")
else:
    print("No esta carpeta")


