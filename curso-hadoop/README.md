# INDICE.

- 
- [Introducción al pensamiento computacional](#Introducción-al-pensamiento-computacional)

# Curso Hadoop.

1. HADOOP.
   
    - HDFS = Sistema de archivos distribuidos.
    - Job Node => Es el job que se encarga de realizar los trabajos.
    - Name Node => Es el registro donde esta la ubicacion de los datos
    - Data Node => Es donde se encuentran registrado los datos
___
1. YARN
   
   <p align="center"> <img src ="./images/yarn-arquiteture.png"></p>

   - Manejador y negoiador de recursos.
   - Su objeto es negoiar los reursos con las diferentes herramientas.
   





## Configuración.
1. Clonar repositorio => git clone https://github.com/terranigmark/curso-hadoop-platzi.git
2. Crear una red sudo docker network create --driver=bridge hadoop
3. Inicializar contenedores con archivo start-container.sh => sudo ./start-container.sh
4. Levantar servicio hadoop.
    - Ingresar al contenedor master. => docker exec -it {id} /bin/bash
    - ejecutar => ./start-hadoop.sh

## Tipos de  compresion.
- Parquet formato.
- Avro formato.



## COMANDOS HADOOP.
- Crer carpetas => hdfs dfs -p {carpeta}
- Consultar directorio => hdfs dfs -ls
- Trasladar archivos => hdfs dfs -put {archivo} {carpeta/}



## RECURSOS.

The Project Gutenberg EBook of La Odisea, by Homer
- https://www.gutenberg.org/files/58221/58221-0.txt
