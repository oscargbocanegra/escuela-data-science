def factorial(n):
    """Funcion que calcula el factorial de n.

    n int > 0 
    return n!
    
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n -1 )

def run():
    n = int(input('Escribe un entero: '))
    print(factorial(n))

if __name__ == "__main__":
    run()