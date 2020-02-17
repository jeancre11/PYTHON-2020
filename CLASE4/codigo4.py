"""uso del modulo tkinder"""
#importar todo el modulo tkinder
from tkinter import  *
aplicacion=Tk()
#metodo title
aplicacion.title("interfaz grafica con tkinter")
#metodo geometry
aplicacion.geometry("600x600")
def encender():
    print("boton encendido")
#button
boton1=Button(aplicacion,text="Boton encender", command=encender)
boton1.place(x=100, y=50)
import  time
while True:
    #actualizar interfaz grafica
    aplicacion.update()
    print("hola mundo")
    time.sleep(0.5)

#metodo mainloop
aplicacion.mainloop()
print("----fin del programa----")