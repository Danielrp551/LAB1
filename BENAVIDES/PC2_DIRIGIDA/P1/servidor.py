import socket
import time

#Configura el servidor 
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

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

        #Recepcion numero de empleados
        raw = client_socket.recv(BUFFER_SIZE)
        n = int(raw.decode())
        #Lectura
        start = time.perf_counter()
        data = ''
        with open(FILE_NAME,'r') as f:
            for i in range(n+1):
                data += f.readline()     
        stop = time.perf_counter()
        t = (stop- start)*1000
        print(f"Tiempo de lectura {t:.3f}")  
        #Envio
        start = time.perf_counter()
        client_socket.sendall(data.encode())
        stop = time.perf_counter()
        t = (stop- start)*1000
        print(f"Tiempo de envio {t:.3f}")    
        #Cierra la conexion con el cliente
        print("Archivo enviado, cerrando conexion")
        client_socket.close()
except KeyboardInterrupt:
    print("\nCerrando server")
    # Cierra el socket del servidor
    server_socket.close()