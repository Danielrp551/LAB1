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

#Envia el numero de empleados
n = input("Ingrese el número de empleados que desea obtener: ")
msg = n.encode()
client_socket.send(msg)

#Recibe el archivo
start = time.perf_counter()
data = ''
while True:
    raw = client_socket.recv(BUFFER_SIZE)
    if not raw:
        break
    data += raw.decode()
stop = time.perf_counter()
t = (stop - start)*1000
print(f"Tiempo de recepcion : {t:.3f}")

# Escribe el archivo en disco
start = time.perf_counter()
with open('descarga.csv', 'w', encoding="utf-8") as file:
    file.write(data)
stop = time.perf_counter()
t = (stop - start)*1000
print(f"Tiempo de escritura : {t:.3f}")

# Cierra el socket del cliente
print('Archivo recibido, cerrando conexion')
client_socket.close()
