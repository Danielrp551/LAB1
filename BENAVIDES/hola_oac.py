
if __name__ == '__main__':
    frase  = "Hola OAC mulas"

    with open ("archivo.txt","w+", encoding="utf-8") as f:
            f.write(frase)