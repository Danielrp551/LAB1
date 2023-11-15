import socket
import time

#Configura el servidor 
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024*8

FILE_NAME = 'empleados.csv'

#Crea un socket al servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Enlaza el socket al host y puerto
server_socket.bind((HOST,PORT))

#Escucha hasta 5 conexiones entrantes
server_socket.listen(5)

print(f"Servidor de transferencia de archivos escuchando en {HOST}:{PORT}")
try:
    while True:
        #Espera a que un ciente se conecte
        client_socket, client_address = server_socket.accept()
        print(f"Conexion entrante desde {client_address}")

        #recibe por fragmentos
        data = ''
        while True:
            raw = client_socket.recv(BUFFER_SIZE)
            if not raw:
                break
            data += raw.decode()
        #guardo lo recibido en un archivo local
        with open("BIG_FILE_LOCAL.txt",'w+') as file:
            file.write(data)
  
        #Cierra la conexion con el cliente
        print("Archivo enviado, cerrando conexion")
        client_socket.close()
except KeyboardInterrupt:
    print("\nCerrando server")
    # Cierra el socket del servidor
    server_socket.close()