import time
import random
import multiprocessing
from multiprocessing import Process, Manager
from statistics import mean
from statistics import median

def hallarMinimo(A, B, resultado_compartido):
    vectorMinimo = []
    for i in range(4096):
        if A[i] > B[i]:
            vectorMinimo.append(B[i])
        else:
            vectorMinimo.append(A[i])
    resultado_compartido.extend(vectorMinimo)

def hallarMinimoParalelo(A, B, numeroProcesos):
    with Manager() as manager:
        resultado_compartido = manager.list()  # Lista compartida entre procesos
        procesos = []  # Lista para almacenar los procesos

        tamanhoChunk = 4096 // numeroProcesos  # Tamaño del "chunk" para cada proceso

        # Bucle para crear y lanzar los procesos
        for i in range(numeroProcesos):
            inicio = i * tamanhoChunk
            final = inicio + tamanhoChunk

            # Ajustar el valor final del último proceso
            if i == numeroProcesos - 1:
                final = 4096

            # Crear un nuevo proceso y pasarlo a la función hallarMinimo
            proceso = Process(target=hallarMinimo, args=(A[inicio:final], B[inicio:final], resultado_compartido))
            proceso.start()
            procesos.append(proceso)

        # Esperar a que todos los procesos completen su ejecución
        for proceso in procesos:
            proceso.join()

        # Convertir la lista compartida en una lista normal
        vectorMinimo = list(resultado_compartido)
    
    return vectorMinimo

if __name__ == "__main__":
    # Crear dos vectores llenos de valores aleatorios
    A = [random.randint(1, 9) for _ in range(4096)]
    B = [random.randint(1, 9) for _ in range(4096)]

    print("VECTOR A:")
    print(A)
    print("VECTOR B:")
    print(B)

    # Medir el tiempo de ejecución de hallarMinimoParalelo
    tiemposEjecucion = []
    # El usuario registra el número de procesos que desea utilizar
    numeroProcesos = 2
    for i in range(10):
        inicio = time.perf_counter() 
        vectorMinimo = hallarMinimoParalelo(A, B, numeroProcesos)
        fin = time.perf_counter()
        tiempo = fin - inicio
        tiemposEjecucion.append(tiempo)
        print(f"Tiempo de ejecucion {i}: {tiempo} segundos")

    print(tiemposEjecucion)
    print("MEDIDAS DE TENDENCIA CENTRAL")
    # MEDIANA
    print(f"Mediana: {median(tiemposEjecucion)}")
    # MEDIA
    print(f"Media: {mean(tiemposEjecucion)}")
