import random
import time


def genera_notas():
    with open("notas.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,p1,p2,p3,p4,l1,l2,l3,l4,l5,ex1,ex2\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            p1 = random.randint(0, 20)
            p2 = random.randint(0, 20)
            p3 = random.randint(0, 20)
            p4 = random.randint(0, 20)
            l1 = random.randint(0, 20)
            l2 = random.randint(0, 20)
            l3 = random.randint(0, 20)
            l4 = random.randint(0, 20)
            l5 = random.randint(0, 20)
            ex1 = random.randint(0,20)
            ex2 = random.randint(0,20)
            linea = f"{codigo},{p1},{p2},{p3},{p4},{l1},{l2},{l3},{l4},{l5},{ex1},{ex2}\n"
            f.write(linea)       

def main():
    genera_notas()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Tiempo de ejecución: {end - start} segundos")