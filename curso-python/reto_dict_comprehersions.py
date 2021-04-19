def run():
    """Reto dict comprehension
    Crear, con un dictoniary comprehension cuyas llaves son los 100 nros y los valores son el 
    numero de la llave elevado al cubo.
    """
    dictionary = {i: i ** 3 for i in range (1,101) if i %3 != 0}
    print(dictionary)

    # for key, value in super_dict.items():
    #     print(key, "-", value)
if __name__ == '__main__':
    run()