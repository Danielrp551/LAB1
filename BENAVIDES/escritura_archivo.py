
if __name__ == '__main__':
    with open("archivo_codigos.txt","w+",encoding="utf-8") as f:
        cod_ini = 20230001

        for i in range(50):
            print(f"Escribiendo indice {i+1} / 50")
            f.write(f"{cod_ini+i}\n")