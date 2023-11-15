import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ('localhost', 5001)
    
    print(f"Iniciando servidor en {server_adress[0]}:{server_adress[1]}")

    sock.bind(server_adress)

    print("Empezando a escuchar clientes...")
    sock.listen(1)
    
    while True:
        conn, client_adress = sock.accept()
        print(f"Cliente conectado desde {client_adress[0]}:{client_adress[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)
                
                if data:
                    print(f"Recibi {data}")
                    conn.sendall(data)
                else:
                    print(f"No hay mas datos de {client_adress[0]}:{client_adress[1]}")
                    break
        except ConnectionResetError:
            print(f"Cliente {client_adress[0]}:{client_adress[1]} desconectado abruptamente")
        finally:
            conn.close()
            print(f"Conexion con {client_adress[0]}:{client_adress[1]} cerrada")
            

