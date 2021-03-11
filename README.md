# ÍNDICE.
 
- [Introducción al pensamiento computacional](#Introducción-al-pensamiento-computacional)
   - [Introducción al cómputo](#Introducción-al-cómputo)
   - [Introducción a lenguajes de programación](#Introducción-a-lenguajes-de-programación)
   - [Elementos Básicos de programación](#Elementos-Básicos-de-programación)
   - [Cadenas y entradas](#Cadenas-y-entradas)
   - [Operadores de comparación](#Operadores-de-comparación)

   - [](#)
   - [](#)
   - [](#)
   - [](#)


____
# Introducción al pensamiento computacional
___
## Introducción al cómputo.
- **Primera computadora:** Creada por los griegos.
El propósito era calcular las posiciones del sol de la luna y unas constelaciones.
- **Telar de Jacquard:** Usaba tarjetas punch cards que representan el resultado de la información.
- **Motor analítico de Babbage:** con el uso de mecanica (engranajes) se logra la separación de instrucciones de cálculo y realizar varios de estos a la vez.
- Finales siglo XIX, ENIAC (Electronic Numerical Integrator and Computer) crea el sistema decimal por Alan Turing y Alonso.
- En 1945 la Arquitectura de Von Neumann, EDVAC (Electronic Discrete Variable Automatic Computer) con el sistema binario aporta como realizar cálculos con nuevos componentes y  almacenar en memoria.
- La revolución de los microchips con el Apple 1 permiten la evolución y transformación de los cálculos que a la fecha conocemos.
- Richard Feynman  brinda las bases del cálculo cuántico.
- Arquitectura de Von Newman Dispositivo entrada (cpu-cómputo) salida
____
## Introducción a lenguajes de programación
- Cómo se dan las instrucciones.
    - **Conocimiento declarativo:** Dice que tipo de relaciones existen entre diversas variables.
    - **Conocimiento imperativo:** Nos dice como llegar a un resultado.
- **Que es un Algoritmo:** una serie de pasos finitos.
- **Sintaxis:** Define la secuencia de símbolos formada
- **Semántica estática:** Define que enunciados con sintaxis correcta tienen significado.
- **Semántica :** Define el significado en los lenguajes de programación.  
____
## Elementos Básicos de programación
- ***Bajo Nivel Vs Alto nivel.***
- ***General Vs dominio específico.***
- ***Interpretado vs compilado.***
- **Objetos:** Es la forma en que se modela el mundo en el lenguaje de programación.
    - Tipos
    - Escalar.
    - No escalares
- **Variables:**
    - Son nombres que apuntan a un espacio en memoria. 
    - Hacen los programas comprensibles
    - El operador (=) asocia una variable con un error
____
## Cadenas y entradas
- Son secuencias de caracteres.
- Se pueden hacer operaciones con las cadenas.
- Se pueden mezclar para hacer diferentes tipos de computo.
- Son inmutables. Una vez declaradas no se puede modificar.

- Ejemplo de operaciones con cadenas y python.
- **input:** Es una entrada por teclado que almacena el valor en formato string.
    ```py
    variable = input('Texto ')
    ```
- para convertir el valor ingresado en input es necesario convertir el tipo de texto es se hace de la siguiente forma.
    ```py
    variable = int(input('1'))
    ```
    ```py
            frase = 'bienvenidos a platzi con el curso pensamiento computacional'
    ```
- Para contar la cantidad usamos len
    ```py
        print(len(frase))
    ```
- para saber cuántas veces aparece un carácter usamos count.
    ```py
    print(frase.count('i')).
    ```
- Para reemplazar un carácter por otro usamos la función replace.
    ```py
    print(frase.replace('i','k'))
    ```
- Para separar el string en una lista con todos los string usamos split.
    ```py
    print(frase.split(' '))
    ```
- Para asignar mayúsculas a la primera letra se usa la función.
    ```py
    print(frase.capitalize()).
    ```
- Para asignar mayúsculas a todas las primeras letras se usa la funcion title.
    ```py
    print(frase.title()).
    ```
- Para concatenar también se puede usar la expresión f´.
    ```py
    f'{"Hip " * 3} Hurra'
    ```
____
## Operadores de comparación
- **(==)** Es un operador de igualdad -- 2 == 3
- **(!=)** Es un operador de No igualdad o desigualdad 2 != 3
- **(<=)(>=)** Otro tipo de operadores de comparación.
- **AND OR NOT** Son operadores lógicos
____
## Iteraciones.

- Es una forma de realizar tareas en forma secuencial.
- Se puede manejar con diferentes ciclos que permiten repetir las tareas 
    - iteraciones con el ciclo for {for <variable> in <iterable>: <expresion>}
    - Iteraciones con el ciclo while {while <expresion> <condicion>:}