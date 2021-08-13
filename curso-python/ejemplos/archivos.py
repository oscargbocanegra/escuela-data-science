def run():
    read()
    #write()

def read():
    numbers = []
    with open("/home/giovanni/repositorios/escuela-data-science/curso-python/ejemplos/archivos/archivos.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(line)
    print(numbers[0])
    

def write():
    names = ["Oscar","Camilo","David","Monica","Luis","Carmen","Jorge"]
    with open("/home/giovanni/repositorios/escuela-data-science/curso-python/ejemplos/archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

if __name__ == "__main__":
    run()