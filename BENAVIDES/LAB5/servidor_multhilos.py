import socket
import time
from threading import Thread
from threading import Lock

#Configura el servidor 
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024*8

FILE_NAME = 'empleados.csv'
data = ''

def client_handler(client_socket, client_address):
    print(f"Conexion entrante desde {client_address}")

    try:
        #recibe por fragmentos
        global data 
        lock = Lock()
        
        with lock:
            while True:
                raw = client_socket.recv(BUFFER_SIZE)
                if not raw:
                    break
                data += raw.decode()
                
        #guardo lo recibido en un archivo local
        with open("BIG_FILE_LOCAL.txt",'w+') as file:
            file.write(data)

    
    except ConnectionResetError:
        print(f"Cliente {client_address} desconectado abruptamente")
    finally:
        #Cierra la conexion con el cliente
        client_socket.close()  
        print(f"Conexion con {client_address} cerrada")
        


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = (HOST,PORT)

    print(f"Iniciando servidor en {server_address}")

    sock.bind(server_address)

    print("Empezando a escuchar clientes . . .")
    sock.listen(1)

    while True:
        connection, c_addres = sock.accept()

        t = Thread(target=client_handler,args = (connection,c_addres))
        t.start()