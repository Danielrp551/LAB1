import time
import random
import threading
from threading import Thread
from statistics import mean
from statistics import median
from memory_profiler import profile


def hallarMinimo(A, B,inicio,final,vectorMinimo):
    vectorMinimo = []
    for i in range(4096):
        if(A[i]>B[i]):
            vectorMinimo.append(B[i])
        else:
            vectorMinimo.append(A[i])

@profile
def hallarMinimoHilos(A,B):
    vectorMinimo = []
    hilos = []
    numHilos = 2
    tamanhoChunk = 4096 // numHilos
    hilo = []
    for i in range(numHilos):
        inicio = i * tamanhoChunk
        final = inicio + tamanhoChunk

        if(i == numHilos-1):
            final = 4096

        hilo = threading.Thread(target=hallarMinimo, args=(A,B,inicio,final,vectorMinimo))
        hilo.start()
        hilos.append(hilo)
    
    for hilo in hilos:
        hilo.join()
    
    return vectorMinimo

if __name__ == "__main__":
    #Creamos dos vectores
    A = []
    B = []
    #Los llenamos de valores aleatorios 
    for i in range(4096):
        A.append(random.randint(1,9))
        B.append(random.randint(1,9))
    
    #print("VECTOR A:")
    #print(A)
    #print("VECTOR B:")
    #print(B)
    #Los tiempos de ejecucion seran solo de la funcion que nos da el minimo entre dos vectores
    #La funcion sera llamada 10 veces, por lo que obtendremos 10 tiempos de ejecucion para poder usar las medidas de tendencia central
    tiemposEjecucion=[]
    vectorMinimo = []
    for i in range(10):
 
        inicio = time.perf_counter() 
        hallarMinimoHilos(A,B)
        fin = time.perf_counter()
        tiempo=fin-inicio
        tiemposEjecucion.append(fin-inicio)
        print(f"Tiempo de ejecucion {i}: {tiempo} segundos")

print(tiemposEjecucion)
print("MEDIDAS DE TENDENCIA CENTRAL")
#MEDIANA
print(f"Mediana: {median(tiemposEjecucion)}")
#MEDIA
print(f"Media: {mean(tiemposEjecucion)}")