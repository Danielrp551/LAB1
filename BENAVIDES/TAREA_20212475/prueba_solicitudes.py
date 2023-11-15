import asyncio
import socket
import time

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

async def envio_solicitudes(num):
    print(f"Enviando solicitud de alumno {num}")
    recibo, envio = await asyncio.open_connection(HOST, PORT)
    envio.write(num.encode())
    data = await recibo.read(BUFFER_SIZE)
    print(f"Nota de alumno {num}: {data.decode()}")
    envio.close()

async def main():
    tasks = []
    codigos = ['20230010','20230011','20230012','20230013']
    for i in range(len(codigos)):
        task = asyncio.create_task(envio_solicitudes(codigos[i]))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()
    tiempoProm = (fin-start)*100/4
    print(f"Tiempo promedio por solicitud : {tiempoProm:.3f} ms")