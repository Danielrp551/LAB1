import socket
import time

#Configura el cliente
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

# Crea un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Se conecta al servidor 
client_socket.connect((HOST,PORT))

#Envia el codigo del alumno
n = input("Ingrese el codigo del alumno: ")
msg = n.encode()

start = time.perf_counter()
client_socket.send(msg)

#Recibe la nota

data = client_socket.recv(BUFFER_SIZE).decode()
stop = time.perf_counter()
t = (stop - start)*1000
print(f"Tiempo de transaccion : {t:.3f} ms")

print(f"Nota final del alumno {n} es "+ data +"\n")

# Cierra el socket del cliente
print('Nota recibida, cerrando conexion')
client_socket.close()
