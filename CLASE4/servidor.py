"""codigo de parte del servidor"""
#importamos el modulo socket
import  socket, pickle
#crear un objeto
#----IPv4, TCP (protocolo de transporte),
servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#UTILIZAR EL METODO bind
#IP de mi ordenador
#IP="127.0.0.1"
IP="192.168.0.101"
PUERTO=5000
#bind solo para servidor
servidor.bind((IP, PUERTO))
print("SERVIDOR A LA ESPERA DE CONEXIONES")
#escuchar conexiones
servidor.listen()
#aceptar la conexion de un cliente
cliente, direccion=servidor.accept()
#leer datos del cliente
with cliente:
    #leer datos, la cantidad que quieres 1000
    datos=cliente.recv(10000)
    #convertir de flujo de bytes al objeto original
    msje=pickle.loads(datos)
    print(msje)
    #enviar respuesta del servidor al cliente
    cliente.sendall(pickle.dumps("--servidor respondiendo"))

