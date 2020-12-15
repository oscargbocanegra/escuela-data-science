def comparar (persona1, persona2):
    persona1_edad = int(input(f'{persona1} Que edad Tiene: '))
    persona2_edad = int(input(f'{persona2} Que edad Tiene: '))

    if persona1_edad > persona2_edad:
        return print(f'{persona1} es mayor que {persona2}')
    elif persona2_edad > persona1_edad:
        return print(f'{persona2} es mayor que {persona1}')

def run():
    persona1_nombre = input('Cual es su Nombre: ')
    persona2_nombre = input('Cual es su Nombre: ')
    comparar(persona1_nombre,persona2_nombre)

if __name__ == "__main__":
    run()