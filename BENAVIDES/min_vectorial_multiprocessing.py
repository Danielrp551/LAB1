import time
import random
import multiprocessing
from multiprocessing import Process, Manager
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

def hallarMinimoParalelo(A,B,numeroProcesos):
    pool = multiprocessing.Pool(processes=numeroProcesos)
    segmentos = []
    tamanhoChunk = 4096 // numeroProcesos
    for i in range(numeroProcesos):        
        inicio=i*tamanhoChunk+1
        fin=(i+1)*tamanhoChunk
        segmentos.append((inicio,fin))

    resultados=[pool.apply_async(hallarMinimo,segmento)for segmento in segmentos]
    pool.close()
    pool.join()
    vectorMinimo = []
    vectorMinimo.append(resultado.get() for resultado in resultados)
    
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
    #AQUI EL USUARIO REGISTRA LOS NUMEROS DE PROCESOS QUE DESEA UTILIZAR
    numeroProcesos = 2
    for i in range(10):
        inicio = time.perf_counter() 
        vectorMinimo = hallarMinimoParalelo(A,B,numeroProcesos)
        fin = time.perf_counter()
        tiempo=fin-inicio
        tiemposEjecucion.append(tiempo)
        print(f"Tiempo de ejecucion {i}: {tiempo} segundos")

print(tiemposEjecucion)
print("MEDIDAS DE TENDENCIA CENTRAL")
#MEDIANA
print(f"Mediana: {median(tiemposEjecucion)}")
#MEDIA
print(f"Media: {mean(tiemposEjecucion)}")
