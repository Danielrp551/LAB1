import time 


def sumaImpar():
    



if __name__ == '__main__':
    n = 10**9
    ini = time.perf_counter()
    suma = sumaImpar(n)
    fin = time.perf_counter()
    t = (fin-ini)*100
    print(f"Tiempo de ejecucion : {t} ms")