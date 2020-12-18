CURSOS ESCUELA DE CIENCIA DE DATOS PLATZI

# TABLA DE CONTENIDO.

1. [Basic python](#Basic-python)
2. [Introducción al pensamiento computacional](#Introducción-al-pensamiento-computacional)
3. 
---
# Basic python

- **Que es un algoritmo: ** Es una serie de pasos finitos y NO ambiguos para resolver algo.
- **Para qué sirven: ** Para resolver un problema.
- **Características delos algoritmos**
    **- Secuenciales: ** Operan en secuencia uno a la vez.
    **- Precisos: ** No pueden ser ambiguos.
    **- Ordenados: ** Se deben establecer en la secuencia precisa.
    **- Finitos: ** Toda secuencia debe tener un fin.
    **- Concretos: ** Todo algoritmo ofrece un resultado.
    **- Definidos: ** Deben dar el mismo resultado.

- **Que es una variable: ** es una caja donde puedes guardar algo (dato, objeto) y tiene un identificador.
    El identificador NO puede comenzar con numero, debe estar en minusculas y si tiene mas de una palabra se debe separar con guion_bajo.

- **operadores aritméticos. **

    - **Tipos de datos**
        - Números enteros.
        - Números de punto flotante.
        - Texto (cadena de caracteres)
        - Booleanos (Verdadero y falso)
        - Concatenacion es la union de 2 textos y se usa la tecla +.

    - **Convertir de String a Int: ** Para conertir de string a int se antepone la palabra int(string) seguido de la variable.

    - **Convertir de Int a String: ** Para conertir de Int a String se antepone la palabra str(Int) seguido de la variable.

# Introducción al pensamiento computacional

- **Cadenas y entradas. **

    - input es una entrada por teclado que almacena el valor en formato string. 

        ```py
        variable = input('Texto ')
        ```
* para convertir el valor ingresado en input es necesario convertir el tipo de texto es se hace de la siguiente forma. Ej. 
    ```py
    variable = int(input('1'))
    ```
    ```py
    frase = 'bienvenidos a platzi con el curso pensamiento computacional'
    ```
* Para contar la cantidad usamos len
    ```py
        print(len(frase))
    ```
* para saber cuantas veces aparece un carácter usamos count.
    ```py
    print(frase.count('i')).
    ```
* Para remplazar un carácter por otro usamos la función replace.
    ```py
    print(frase.replace('i','k'))
    ```
* Para separar el string en una lista con todos los string usamos split. 
    ```py
    print(frase.split(' '))
    ```

* Para asignar mayúsculas a la primera letra se usa la función.
    ```py
    print(frase.capitalize()).
    ```

* Para asignar mayusculas a todas las primeras letras se usa la funcion title. 
    ```py
    print(frase.title()).
    ```
* Para concatenar también se puede usar la expresión f´. 
    ```py
    f'{"Hip " * 3} Hurra' 
    ```
# Operadores de comparación.

* (==) Es un operador de igualdad -- 2 == 3
* (!=) Es un operador de No igualdad o desigualdad 2 != 3
* (<=)(>=) Otro tipo de operadores de comparación.
* AND OR NOT Son operadores lógicos 

# Iteraciones.

* Nos permiten realizar la tarea en varias iteraciones las veces que sea necesario.
* Se pueden construir iteraciones anidadas estilo un reloj donde el segundo avanza para que el minuto tambien avance.
* BREAK = Es un comando que permite finalizar una iteración.
* CONTINUE = Es un comando que permite saltar una iteración del ciclo.
* Ejemplos de iteraciones en archivo iteraciones.py

# Bucles For.

* Los bucles definidos se implementan a través del keyword for 
* Iterable se entiende como una colección de objetos que se van recorriendo.
* Ej. bucle iterable.
    ```py
    frutas = ["Manzanas","peras","piñas"]
    
    for fruta in frutas:
        print (fruta)
    ```
* Bucles con diccionarios se pueden iterar de la siguiente forma.
    ```py
    estudiantes = {'mexico':10, 'Colombia': 20, 'Argentina:30'}
        for país in estudiantes:
        for país in estudiantes.keys():
        for numero_estudiantes is estudiantes.values():
        for país, numero_estudiantes is estudiantes.items():
    ```
# Enumeración exhaustiva.

* Lo primero que se hace es enumerar todas las posibles opciones.
* Ejemplo en el ejercicion de enumeracion.py donde ingresa un numero y este busca si tiene raiz cuadrada exacta

# Aproximación de soluciones.

* En ocaciones se necesita dar una respuesta, aunque sea aproximada.
* La diferencia entre la realidad y la aproximacion se define como EPSILON
* Epsilon = es la aceptación de un margen de incertidumbre en una respuesta.
* Se debe definir un tradeoff (Canje) que permita negociar la respuesta.
* Ejemplo en el archivo aproximacion.py
* ABS = Es una función que retorna el valor absoluto.

# Búsqueda binaria.

* En este tipo de busqueda se simplifica al cortar la busqueda a la mitad en cada itaracion.
* MAX = es la funcion que nos regresa el numero mas alto del objetivo
* La busque binaria solo funiona cuando esta ordenado nuestro objeto.
* Ejemplo en el archivo busqueda_binaria.py

# Funciones abstracción.

* Que es la abstracción = Es la operacion de un objeto sin necesidar de conocer su función: Ej. una calculadora, un coche.
* Decomposición = Es la divición de objetos en partes, pedasos de codigo que agilizan la programacion.
* para crear una función se realiza con la siguiente estructura.
    ```py
    def <#nombre> (#parámetros):
        <#cuerpo>
        return <#expresión>
    ```
# Scope o Alcance. </h1>

* Scope o Alcance = Es el valor y alcance que puede tener una variable o función al ser invocada en el programa. Ej.
    ```py
    x = 300
    def myfunc():
        global x
        x = 200
    myfunc()
    print(x)
    ```
Para este ejemplo se observa como la variable x contiene 2 valores ya que X fuera de la funcion myfunc no tiene el alcance de la x = 200.

# Especificaciones del codigo """ docstring """.

* La """ triple commilla """ valor """ es una convencion que permite comunicar que hace el codigo.
* Para consultar la descripción se usa help(función).
* Esto permite documentar y leer funciones en python.

# Recursividad.

* Algoritmica = Es una forma de crear soluciones utilizando el principio de divide y venceras.
* Programatica = Una tecnica mediante una funcion se llame asi misma otra vez.
* Ejemplo de recursividad en el programa factoriales.py

# Tuplas.

* Las tuplas son secuencias, al igual que las listas la diferencia esta en que las tuplas son inmutables es decir no se pueden modificar.
* Las tupas se escriben entre paréntesis (tupla)
El contenido de una tupla puede ser de tipo String, int, float.
* Cuando una tupla tiene un solo valor se debe asignar una coma al final para que no pierda el formato de tupla. Ej. tupla = (3) se debe asignar la (,) al final Ej. tupla = (3,)
* Las tuplas se pueden acceder por el índice.
    * tupla = (1,2,'hola') accediendo por el índice tupla [0]
* Desempaquetar = Las tuplas se pueden desempaquetar y asignar a variables.
    ```py
    tupla = (1,2,'hola')
    x,y,z = tupla   
    ```
# Rangos.

* Representan una sección de enteros con un inicio y fin.
* Los rangos también son inmutables no se pueden modificar.
* Ventajas que se puede conocer el uso de memoria ya que se pueden limitar.
* Ejemplo = range (comienzo, fin, pasos)

# Pruebas de caja negra.

* Se basan en la especificacion de la función o el programa.
* Prueba inputs y valida outputs
* Unit testing o Integration testing
* Ejemplo prueba de caja negra.
    * Importar la libreria unittest
        ```py
        import unittest
        ```
    * Generacion del codigo test que describe los casos posibles a probar.
        ```py
        class CajaNegraTest(unittest.TestCase):

            def test_suma_dos_positivos(self):
                num_1 = 10
                num_2 = 5

                resultado = suma(num_1, num_2)

                self.assertEqual(resultado, 15)
        ```
    *  Se crea la funcion que contiene los pasos a ejecutar.
        ```py
        def suma(num_1, num_2):
            return num_1 + num_2 
        ```
    * Comando para ejecutar el archivo.
        ```bash
        $ py caja_negra.py  
        ```
    * Resultado de la ejecución.
        ```bash
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK
        ```

# Pruebas de caja de cristal

* Se basan en el flujo del programa.
* Prueban todos los caminos posibles de una función. (Ramificaciones, bucles for, while, recursión).
* Regression testing o mocks.
* Ejemplo prueba caja de cristal.
    * Importar la libreria unittest
        ```py
        import unittest
        ```
    * Generacion del codigo test que describe los casos posibles a probar.
        ```py
         class PruebaDeCristalTest(unittest.TestCase):
                def test_es_mayor_de_edad(self):
                    edad = 20
                    resultado = es_mayor_de_edad(edad)
                    self.assertEqual(resultado, True)

        if __name__ == "__main__":
            unittest.main()
        ```
    * Comando para ejecutar el archivo.
            ```bash
            $ py  prueba_caja_cristal.py
            ```
    * Resultado de la ejecución.
        ```bash
                .
            ----------------------------------------------------------------------
            Ran 1 test in 0.000s

            OK
        ```

# Debugging.

* Aprender a usar el print statement.
* Estudia los datos disponibles.
* Usa los datos para crear hipotesis y experimientos **Metodo Cientifico**
