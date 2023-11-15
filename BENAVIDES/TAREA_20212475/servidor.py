import socket
import time

#Configura el servidor 
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

FILE_NAME = 'notas.csv'

#Crea un socket al servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Enlaza el socket al host y puerto
server_socket.bind((HOST,PORT))

#Escucha hasta 5 conexiones entrantes
server_socket.listen(5)

print(f"Servidor de transferencia de notas escuchando en {HOST}:{PORT}")
try:
    while True:
        #Espera a que un ciente se conecte
        client_socket, client_address = server_socket.accept()
        print(f"Conexion entrante desde {client_address}")

        #Recepcion de codigo de alumno
        raw = client_socket.recv(BUFFER_SIZE)
        start = time.perf_counter()
        codigo = raw.decode()
        #Lectura
        
        data = ''
        with open(FILE_NAME,'r+') as f:
            data = f.read()     


        #Calcula nota final
        lineas = []
        lineas = data.split('\n') #Cada linea del csv
        for linea in lineas:
            notas = []
            notas = linea.split(',')
            if notas[0] == codigo:
                break
        
        #promedio de pcs
        notas_pcs = list(map(int,notas[1:5]))
        #print(notas_pcs)
        notas_pcs.sort()
        promPC = 0
        for i in range(3):
            promPC += notas_pcs[len(notas_pcs)-1-i]
        promPC = promPC/3
        #print(promPC)

        #promedio de labs
        notas_labs = list(map(int,notas[5:10]))
        #print(notas_labs)
        promLab = 0
        for i in range(5):
            promLab += notas_labs[i]
        promLab = promLab/5
        #print(promLab)

        ex1 = int(notas[10])
        ex2 = int(notas[11])
        nota_f = promPC*3 + promLab*3 + ex1*2 + ex2*2
        nota_f /=10

        nota_f = round(nota_f)
        nota_final = str(nota_f)
        #Envio

        client_socket.sendall(nota_final.encode())
        stop = time.perf_counter()
        t = (stop- start)*1000
        print(f"Tiempo de ejecucion de solicitud  {t:.3f} ms")    
        #Cierra la conexion con el cliente
        print("Archivo enviado, cerrando conexion")
        client_socket.close()



except KeyboardInterrupt:
    print("\nCerrando server")
    # Cierra el socket del servidor
    server_socket.close()