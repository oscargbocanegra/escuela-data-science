def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es string'
        assert len(palabra) > 0, 'No se permiten vacios'
        primeras_letras.append(palabra[0])
    return print(primeras_letras)


primera_letra('uno')
