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

*   input es una entrada por teclado que almacena el valor en formato string. Ej. variable = input('Texto ').

* para convertir el valor ingresado en input es necesario convertir el tipo de texto es se hace de la siguiente forma. Ej. variable = int(input('1')).

<br><h3>frase = 'bienvenidos a platzi con el curso pensamiento computacional'</h3>

* Para contar la cantidad usamos len
    print(len(frase)).

* para saber cuantas veces aparece un caracter usamos count. Ej. print(frase.count('i')).

* Para remplazar un caracter por otro usamos la función replace. Ej. print(frase.replace('i','k')).

* Para separar el string en una lista con todos los string usamos split. Ej. print(frase.split(' ')).

* Para asignar mayusculas a la primera letra se usa la funcion . Ej. print(frase.capitalize()).

* Para asignar mayusculas a todas las primera letras se usa la funcion title. Ej. print(frase.title()).

* Para concatenar tambien se puede usar la expresion f´ . Ej. f'{"Hip " * 3} Hurra' 

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
* Ej. bucle iterable.  frutas = ["Manzanas","peras","piñas"]  >>>>  for fruta in frutas:
* Bucles con diccionarios se pueden iterar de la siguiente forma.
    * Ej. estudiantes = {'mexico':10, 'colombia': 20, 'Argentina:30'}.
        * for pais in estudiantes:
        * for pais in estudiantes.keys():
        * for numero_estudiantes is estudiantes.values():
        * for pais, numero_estudiantes is estudiantes.items():

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
