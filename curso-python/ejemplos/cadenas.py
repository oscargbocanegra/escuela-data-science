def run():
    frase = 'bienvenidos a platzi con el curso pensamiento computacional'
    #Para contar la cantidad usamos len
    print(len(frase))
    # para saber cuantas veces aparece un caracter usamos count
    print(frase.count('i'))
    # Para remplazar un caracter por otro usamos la función replace
    print(frase.replace('i','k'))
    # Para separar el string en una lista con todos los string usamos split
    print(frase.split(' '))
    #Para asignar mayusculas a la primera letra se usa la funcion capitalize
    print(frase.capitalize())
    #Para asignar mayusculas a todas las primera letras se usa la funcion title
    print(frase.title())
    #Para concatenar tambien se puede usar la expresion f´
    concatenar = f'{"Hip " * 3} Hurra'
    print(concatenar)


if __name__ == "__main__":
    run()