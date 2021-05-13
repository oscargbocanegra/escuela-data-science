# Funcion que recibe un numero como argumento y procesa la funcion para validar si es primo.
def es_primo(numero):
    contador = 0
    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

# Funcion que pide un numero por consola y ejecuta la funciono numero par validar el numero.
def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No Es primo')


if __name__ == '__main__':
    run()
