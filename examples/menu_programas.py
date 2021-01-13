def aproximacion(objetivo, epsilon, respuesta, paso):
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo, epsilon,respuesta,bajo,alto):
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2

def iteraciones():
    contador =0
    contador_externo = 0
    contador_interno = 0
    while contador_externo < 5:
        while contador_interno < 6:
            print(contador_externo, contador_interno)
            contador_interno +=1
        
        contador_externo +=1
        contador_interno = 0

def comparar (persona1, persona2):
    persona1_edad = int(input(f'{persona1} Que edad Tiene: '))
    persona2_edad = int(input(f'{persona2} Que edad Tiene: '))

    if persona1_edad > persona2_edad:
        return print(f'{persona1} es mayor que {persona2}')
    elif persona2_edad > persona1_edad:
        return print(f'{persona2} es mayor que {persona1}')


def run():
    menu = input("""
    Bienvenido al menu de programas escoja la opcion a ejecutar:
    1. Programa de aproximacion.
    2. Programa de busqueda binaria.
    3. Programa Iteraciones.
    4. Programa reto edades.
    Escoja una opción: 
    """)
    opcion = int(menu)
    if opcion == 1:
        objetivo = int(input('Escoge un numero: '))
        epsilon = 0.001
        paso = epsilon**2 
        respuesta = 0.0
        aproximacion(objetivo, epsilon,respuesta,paso)
    
    elif opcion == 2:
        objetivo = int(input('Escoge un numero: '))
        epsilon = 0.001
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo) / 2
        busqueda_binaria(objetivo, epsilon,respuesta,bajo,alto)

    elif opcion == 3:
        iteraciones()

    elif opcion == 4:
        persona1_nombre = input('Cual es su Nombre: ')
        persona2_nombre = input('Cual es su Nombre: ')
        comparar(persona1_nombre,persona2_nombre)


if __name__ == "__main__":
    run()