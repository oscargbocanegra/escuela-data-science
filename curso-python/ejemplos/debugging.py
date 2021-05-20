def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num %i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num >= 0:
            print(divisors(num))
            print("Termino el programa")
        else:
            print("Debes ingresar un numero positivo")
    except ValueError:
        print("Debes ingresar un numero")

if __name__ == '__main__':
    run()