import time
import random
import threading
from threading import Thread
from statistics import mean
from statistics import median

def hallarMinimo(A, B):
    vectorMinimo = []
    for i in range(4096):
        if A[i] > B[i]:
            vectorMinimo.append(B[i])
        else:
            vectorMinimo.append(A[i])
    return vectorMinimo

def hallarMinimoHilos(A, B):
    vectorMinimo = []
    hilos = []  # Lista para almacenar los hilos
    numHilos = 2  # Número de hilos que se utilizarán
    tamanhoChunk = 4096 // numHilos  # Tamaño del "chunk" para cada hilo

    # Bucle para crear y lanzar los hilos
    for i in range(numHilos):
        inicio = i * tamanhoChunk
        final = inicio + tamanhoChunk

        # Ajustar el valor final del último hilo
        if i == numHilos - 1:
            final = 4096

        # Crear un nuevo hilo y pasarlo a la función hallarMinimo
        hilo = threading.Thread(target=hallarMinimo, args=(A[inicio:final], B[inicio:final], vectorMinimo))
        hilo.start()
        hilos.append(hilo)

    # Esperar a que todos los hilos completen su ejecución
    for hilo in hilos:
        hilo.join()

    return vectorMinimo

if __name__ == "__main__":
    # Crear dos vectores llenos de valores aleatorios
    A = [random.randint(1, 9) for _ in range(4096)]
    B = [random.randint(1, 9) for _ in range(4096)]

    print("VECTOR A:")
    print(A)
    print("VECTOR B:")
    print(B)

    # Medir el tiempo de ejecución de hallarMinimoHilos
    tiemposEjecucion = []
    for i in range(10):
        inicio = time.perf_counter() 
        vectorMinimo = hallarMinimoHilos(A, B)
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
