import random
import os

filepath = "/home/giovanni/repositorios/escuela-data-science/curso-python/retos_datacademy/data.txt"
dic={"Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U"}

# Funcion que importa un archivo de una ruta especifica y almacena el contenido usando List comprehensions
def read_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        words = [line.strip().upper() for line in f]
    return words

# Funcion que quita tildes a vocales.
def normalize(cadena, dic):
    for k,v in dic.items():
        cadena=cadena.replace(k, v)
    return cadena

# Funcion que ejecuta el programa invocando read_data para leer el archivo de datos.
# Luego escoge una palabra aleatoria para presentar
def run():
    data = read_data(filepath)
    chosen_word = normalize(random.choice(data), dic)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    
    while True:
        os.system("clear")
        print("adivina la palabra")
        for element in chosen_word_list_underscores:
            print(element + " ", end ="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter, "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        
        if "_" not in chosen_word_list_underscores:
            os.system("clear")
            print("¡Ganaste! La palabra era", chosen_word)
            break


if __name__ == '__main__':
    run()