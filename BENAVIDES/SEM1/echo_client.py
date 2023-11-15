import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ('localhost',5001)

    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        msg = "Hola carajo"
        print(f"Enviando mensaje: {msg}")
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
        print(f"Recibido: {data}")
    finally:
        print("Cerrando socket")
        sock.close()