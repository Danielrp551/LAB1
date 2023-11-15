import time

if __name__ == '__main__':
    inicio = time.perf_counter()
    with open("archivo_codigos.txt",'r', encoding="utf-8") as f:
        contenido = f.read()
    fin = time.perf_counter()

    print(contenido)
    print(f"tiempo de ejecucion: {fin - inicio} segundos")