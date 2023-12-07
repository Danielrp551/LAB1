import time
import random
from statistics import mean
from statistics import median

def hallarMinimo(A, B):
    vectorMinimo = []
    for i in range(4096):
        if(A[i]>B[i]):
            vectorMinimo.append(B[i])
        else:
            vectorMinimo.append(A[i])
    return vectorMinimo

if __name__ == "__main__":
    #Creamos dos vectores
    A = []
    B = []
    #Los llenamos de valores aleatorios 
    for i in range(4096):
        A.append(random.randint(1,9))
        B.append(random.randint(1,9))
    
    print("VECTOR A:")
    print(A)
    print("VECTOR B:")
    print(B)
    #Los tiempos de ejecucion seran solo de la funcion que nos da el minimo entre dos vectores
    #La funcion sera llamada 10 veces, por lo que obtendremos 10 tiempos de ejecucion para poder usar las medidas de tendencia central
    tiemposEjecucion=[]
    for i in range(10):
        inicio = time.perf_counter() 
        vectorMinimo=hallarMinimo(A,B)
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