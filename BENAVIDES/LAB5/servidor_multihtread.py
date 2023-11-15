import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024 * 8

def escribeArch(raw):
    with open('Reporte_File.txt','a+') as f:
        f.write(raw)


def manejar_cliente(client_socket, client_address):
    print(f"Conexión entrante desde {client_address}")

    # Recibe el archivo en fragmentos y guarda en el sistema local

   
    while True:
        raw = client_socket.recv(BUFFER_SIZE)
        if raw:
            escribir_hilo = threading.Thread(target=escribeArch,args=(raw.decode(),))
            escribir_hilo.start()
        if not raw:
            break
    

    print(f"Archivo recibido de {client_address}, cerrando conexión")
    client_socket.close()

def recibir_archivos_con_multihilo():
    # Crea un socket del servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Enlaza el socket al host y puerto
        server_socket.bind((HOST, PORT))
        # Escucha hasta 5 conexiones entrantes
        server_socket.listen(5)

        print(f"Servidor de transferencia de archivos escuchando en {HOST}:{PORT}")

        while True:
            # Espera a que un cliente se conecte
            client_socket, client_address = server_socket.accept()

            # Inicia un hilo para manejar la conexión del cliente
            client_thread = threading.Thread(target=manejar_cliente, args=(client_socket, client_address))
            client_thread.start()

if __name__ == "__main__":
    recibir_archivos_con_multihilo()
