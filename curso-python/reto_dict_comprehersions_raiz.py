from math import sqrt

def run():
    """Reto dict comprehension
    Crear, con un dictoniary comprehension cuyas llaves son los 100 nros y los valores son el 
    numero de la llave elevado al cubo.
    """
    dictionary = {i: round(sqrt(i),2) for i in range (1,1000)}
    print(dictionary)

if __name__ == '__main__':
    run()