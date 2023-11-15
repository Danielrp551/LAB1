import socket
import time
import asyncio
import aiofiles

#Configura el servidor 
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

FILE_NAME = 'notas.csv'

async def main():
    #Crea un socket al servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Enlaza el socket al host y puerto
    server_socket.bind((HOST,PORT))

    #Escucha hasta 5 conexiones entrantes
    server_socket.listen(5)



    print(f"Servidor de transferencia de notas escuchando en {HOST}:{PORT}")
    
    while True:
        #Espera a que un ciente se conecte
        client_socket, client_address = await asyncio.get_event_loop().sock_accept(server_socket)
        print(f"Conexion entrante desde {client_address}")

        #Recepcion de codigo de alumno
        raw = await asyncio.get_event_loop().sock_recv(client_socket,BUFFER_SIZE)
        start = time.perf_counter()
        codigo = raw.decode()
        #Lectura
        
        data = ''
        async with aiofiles.open(FILE_NAME,'r+') as f:
            data = await f.read()     


        #Calcula nota final
        lineas = []
        lineas = data.split('\n') #Cada linea del csv
        for linea in lineas:
            notas = []
            notas = linea.split(',')
            if notas[0] == codigo:
                #print(notas[0])
                break
        
        #promedio de pcs
        notas_pcs = list(map(int,notas[1:5]))
        #print(notas_pcs)
        notas_pcs.sort()
        promPC = 0
        #print(len(notas_pcs))
        for i in range(3):
            #print(notas_pcs[len(notas_pcs)-1-i])
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

        await asyncio.get_event_loop().sock_sendall(client_socket,nota_final.encode())
        stop = time.perf_counter()
        t = (stop- start)*1000
        print(f"Tiempo de ejecucion de solicitud  {t:.3f} ms")    
        #Cierra la conexion con el cliente
        print("Archivo enviado, cerrando conexion")
        client_socket.close()

    
try:
    asyncio.get_event_loop().run_until_complete(main())
except KeyboardInterrupt:
        print("\nCerrando server")
        # Cierra el socket del servidor
        asyncio.get_event_loop().close()