"""codigo de parte del servidor"""
#importamos el modulo socket
import  socket, pickle, numpy
#crear un objeto
#----IPv4, TCP (protocolo de transporte),
cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#UTILIZAR EL METODO bind
#IP del servidor
#IP="192.168.0.119"
IP="127.0.0.1" #local host
PUERTO=5000
#bind solo para servidor
cliente.connect((IP, PUERTO))
print("cliente conectandose")
#enviar mensaje al servidor
cliente.sendall(pickle.dumps("hola mundo servidor"))
info=cliente.recv(1000)
print(pickle.loads(info))