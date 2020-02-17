""" COMUNICACION SERIAL PYTHON Y ARDUINO"""
#tener instalado pip install pyserial
#importar modulo serial
import serial
#crear un objeto de la clase Serial del modulo serial
arduino=serial.Serial()
#configurar los atributos de nuestro ordenador para la comunicacion seral
#velocidad transmicion de datos
arduino.baudrate=9600
arduino.port="COM8"
#8,N,I (8 bits, pariedad, stop)
#1 byte= conjunto de bits, baudios=Nbits/segundos (velocidad)
#INICIAR EL PUERTO COM
arduino.open()
import time
#LEER LOS QUE ARDUINO ESTA ENVIANDO EL EL PUERTO COM
while True:
    #detectar si al caracteres para leer dentro de buffer de recepcion Tx--->Rx
    if arduino.inWaiting()>0:
        while arduino.inWaiting()>0:
            #leer todos los datos
            #datos en bytes
            dato=arduino.read()
            #DECODIFICAR BYTES A VERSION STRING
            dato=dato.decode()
            print(dato, end=" ")
            time.sleep(1)
#cerrar el recurso de la comunicacion serial
arduino.close()