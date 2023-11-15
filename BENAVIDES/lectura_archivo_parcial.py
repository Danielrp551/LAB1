import time

if __name__ == '__main__':
    ini = time.perf_counter()
    contenido =""
    with open("archivo_codigos.txt","r",encoding="utf-8") as f:
        for i in range (50):
            contenido += f.readline()
    fin = time.perf_counter()
    print(contenido)
    print(f"tiempo de ejecucion: {fin - ini} segundos")
