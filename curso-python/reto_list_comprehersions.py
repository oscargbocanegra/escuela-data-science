def multiple(valor, multiple):
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False

def run():
    """Reto list comprehension
    Crear, con un list comprehension una lista de todos los multipos de 4 que a la vez tambien 
    son multiplos de 6 y de 9 hasta 5 digitos
    """
    option = [4,6,9]
    squares = [i for i in range(1, 10000) if multiple(i, 4) and multiple(i, 6) and multiple(i, 9)]
    print(squares)

if __name__ == '__main__':
    run()