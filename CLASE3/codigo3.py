"""USO DE ARCHIVOS DE TEXTO, STRINGS Y LISTAS"""
#built-in function open() en modo append
archivo=open("datos.txt", "a")
archivo.write("PYTHON 2020"+"\n")
#cerrar recurso de texto
archivo.close()
with open("datitos.txt","a") as archi:
    archi.write("Python 2020\n")