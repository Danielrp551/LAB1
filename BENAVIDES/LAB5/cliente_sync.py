import time 
#from threading import Thread
import socket

#Configura el cliente
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024*8

# Crea un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Se conecta al servidor 
client_socket.connect((HOST,PORT))

#Envia el numero de empleados
data = ''
with open('big_file.txt', 'r', encoding="utf-8") as file:
    data = file.read()            

data = data.encode()
 

client_socket.sendall(data)


# Cierra el socket del cliente
print('Archivo recibido, cerrando conexion')
client_socket.close()



