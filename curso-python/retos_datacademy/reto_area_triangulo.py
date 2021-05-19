#Es momento de poner ese conocimiento a la práctica. El área de un triángulo se describe 
# de la siguiente manera: A = (b * h) / 2 .
# Escribe un programa que tome la base y la altura como parámetros y calcule el área 
# del triángulo.

def run(base,altura):
    #base = input("Ingrese la Base: ")
    #altura = input("Ingrese Altura: ")
    
    area = (base * altura)/2
    if (base == altura and base == area):
        return print(f' Es un triangulo Equilatero con base {base}, altura {altura} y {area}')
    elif (base == altura or base == area or altura == base):
        return print(f' Es un triangulo Isoseles con base {base}, altura {altura} y {area}')
    else:
        return print(f' Es un triangulo Escaleno con base {base}, altura {altura} y {area}')
    

if __name__ == '__main__':
    run(7,7)