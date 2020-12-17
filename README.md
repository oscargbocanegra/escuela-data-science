CURSOS ESCUELA DE CIENCIA DE DATOS PLATZI

1. Basic python
2. Introducción al pensamiento computacional.



<h1>1. BASIC PYTHON.</h1>

**Que es un algoritmo:** Es una serie de pasos finitos y NO ambiguos para resolver algo.</br>
**Para que sirven:** Para resolver un problema.</br></br>
*Caracteristicas delos algoritmos*</br>
**- Secuenciales:** Operan en secuencia uno a la vez.</br>
**- Precisos:** No pueden ser ambiguos.</br>
**- Ordenados:** Se deben establecer en la secuencia precisa.</br>
**- Finitos:** Toda secuencia debe tener un fin.</br>
**- Concretos:** Todo algoritmo ofrece un resultado.</br>
**- Definidos:** Deben dar el mismo resultado.</br>

Que es una variable: es una caja donde puedes guardar algo (dato, objeto) y tiene un identificador.</br>
    El identificador NO puede comenzar con numero, debe estar en minusculas y si tiene mas de una palabra se debe separar con guion_bajo </br>

operadores aritmeticos.

Tipos de datos </br>
Numeros enteros.
Numeros de punto flotante.
Texto (cadena de caracteres)
Booleanos (Verdadero y falso)
Concatenacion es la union de 2 textos y se usa la tecla +.
</br>
Convertir de String a Int. </br>
Para conertir de string a int se antepone la palabra int(string) seguido de la variable.</br>

Convertir de Int a String </br>
Para conertir de Int a String se antepone la palabra str(Int) seguido de la variable. </br>

Programa conversor que pide el valor y tipo de moneda 
Programa de condicionales donde se aprende como funciona if


<h1>2. INTRODUCCIÓN AL PENSAMIENTO COMPUTACIONAL CON PYTHON.</h1>

<h2>Clase 1 - Introducción Bienvenida.</h2>
<h2>Clase 2 - Introducción al computo.</h2>

* Historia de la computación

<h2>Clase 7 - Cadenas y entradas.</h2>

*   input es una entrada por teclado que almacena el valor en formato string. 

```
variable = input('Texto ')
```

* para convertir el valor ingresado en input es necesario convertir el tipo de texto es se hace de la siguiente forma. Ej. 
    ```
    variable = int(input('1'))
    ```
    ```
    frase = 'bienvenidos a platzi con el curso pensamiento computacional'
    ```
* Para contar la cantidad usamos len
    ```
        print(len(frase))
    ```
* para saber cuantas veces aparece un caracter usamos count.
    ```
    print(frase.count('i')).
    ```
* Para remplazar un caracter por otro usamos la función replace.
    ```
    Ej. print(frase.replace('i','k'))
    ```
* Para separar el string en una lista con todos los string usamos split. 
    ```
    print(frase.split(' '))
    ```

* Para asignar mayusculas a la primera letra se usa la funcion .
    ```
    print(frase.capitalize()).
    ```

* Para asignar mayusculas a todas las primera letras se usa la funcion title. 
    ```
    print(frase.title()).
    ```
* Para concatenar tambien se puede usar la expresion f´ . 
    ```
    f'{"Hip " * 3} Hurra' 
    ```
<h1>Clase 8 - Programas Ramificados.</h1>
<h2> Operadores de comparacion.</h2>

* (==) Es un operador de igualdad -- 2 == 3
* (!=) Es un operador de No igualdad o desigualdad 2 != 3
* (<=)(>=) Otro tipo de operadores de comparación.
* AND OR NOT Son operadores logicos 

<h1>Clase 9 - Iteraciones.</h1>

* Nos permiten realizar la tarea en varias iteraciones las veces que sea necesario.
* Se pueden construir iteraciones anidadas estilo un reloj donde el segundo avanza para que el minuto tambien avance.
* BREAK = Es un comando que permite finalizar una iteración.
* CONTINUE = Es un comando que permite saltar una iteración del ciclo.
* Ejamplos de iteraciones en archivo iteraciones.py

<h1>Clase 10 - Bucles For.</h1>

* Los bucles definidos se implementan a través del keyword for 
* Iterable se entiende como una colección de objetos que se van recorriendo.
* Ej. bucle iterable.
    ```
    frutas = ["Manzanas","peras","piñas"]
    
    for fruta in frutas:
        print (fruta)
    ```
* Bucles con diccionarios se pueden iterar de la siguiente forma.
```
estudiantes = {'mexico':10, 'colombia': 20, 'Argentina:30'}
    for pais in estudiantes:
    for pais in estudiantes.keys():
    for numero_estudiantes is estudiantes.values():
    for pais, numero_estudiantes is estudiantes.items():
```
<h1>Clase 12 - Enumeración exhaustiva.</h1>

* Lo primero que se hace es enumerar todas las posibles opciones.
* Ejemplo en el ejercicion de enumeracion.py donde ingresa un numero y este busca si tiene raiz cuadrada exacta

<h1>Clase 13 - Aproximacion de soluciones.</h1>

* En ocaciones se necesita dar una respuesta aunque sea aproximada.
* La diferencia entre la realidad y la aproximacion se define como EPSILON
* Epsilon = es la aceptación de un margen de incertidumbre en una respuesta.
* Se debe definir un tradeoff (Canje) que permita negociar la respuesta.
* Ejemplo en el arhivo aproximacion.py
* ABS = Es una función que retorna el valor absoluto.

<h1>Clase 14 - Busqueda binaria.</h1>

* En este tipo de busqueda se simplifica al cortar la busqueda a la mitad en cada itaracion.
* MAX = es la funcion que nos regresa el numero mas alto del objetivo
* La busque binaria solo funiona cuando esta ordenado nuestro objeto.
* Ejemplo en el erchivo busqueda_binaria.py

<h1>Clase 15 - Funciones abstraccion.</h1>

* Que es la abstracción = Es la operacion de un objeto sin necesidar de conocer su función: Ej. una calculadora, un coche.
* Decomposición = Es la divición de objetos en partes, pedasos de codigo que agilizan la programacion.
* para crear una función se realiza con la siguiente estructura.
    ```
    def <#nombre> (#parametros):
        <#cuerpo>
        return <#expresion>
    ```
<h1>Clase 16 - Scope o Alcance.</h1>

* Scope o Alcance = Es el valor y alcance que puede tener una variable o función al ser invocada en el programa. Ej.
    ```
    x = 300
    def myfunc():
        global x
        x = 200
    myfunc()
    print(x)
    ```
Para este ejemplo se observa como la variable x contiene 2 valores ya que X fuera de la funcion myfunc no tiene el alcance de la x = 200.

<h1>Clase 17 - Especificaciones del codigo """ docstring """.</h1>

* La """ triple commilla """ valor """ es una convencion que permite comunicar que hace el codigo.
* Para consultar la descripcion se usa help(funcion).
* Esto permite documentar y leer funciones en python.

<h1>Clase 18 - Recursividad.</h1>

* Algoritmica = Es una forma de crear soluciones utilizando el principio de divide y venceras.
* Programatica = Una tecnica mediante una funcion se llame asi misma otra vez.
* Ejemplo de recursividad en el programa factoriales.py

<h1>Clase 21 - Tuplas.</h1>

* Las tuplas son secuencias, al igual que las listas la diferencia esta en que las tuplas son inmutables es decir no se pueden modificar.
* Las tupas se escriben entre parentesis (tupla)
El contenido de una tupla puede ser de tipo String, int, float.
* Cuando una tupla tiene un solo valor se debe asignar una coma al final para que no pierda el formato de tupla. Ej. tupla = (3) se debe asignar la (,) al final Ej. tupla = (3,)
* Las tuplas se pueden acceder por el indice.
    * tupla = (1,2,'hola') accediendo por el indice tupla[0]
* Desempaquetar = Las tuplas se pueden desempaquetar y asignar a variables.
    ```
    tupla = (1,2,'hola')
    x,y,z = tupla   
    ```
<h1>Clase 22 - Rangos.</h1>

* Representan una seccion de enteros con un inicio y fin.
* Los rangos tambien son inmutables no se pueden modificar.
* Ventajas que se puede conocer el uso de memoria ya que se pueden limitar.
* Ejemplo = range(comienzo, fin, pasos)

<h1>Clase 25 - Pruebas de caja negra.</h1>

