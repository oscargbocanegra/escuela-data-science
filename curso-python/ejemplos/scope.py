def function1():
    """Funcion que define el SCOPE
    var mensaje tipye string
    function funcion2 unifica la palabra Hola Mundo
    """
    mensaje = "Hola, funcion1 "
    def function2(mensaje):
        mensaje += "Mundo, function 2"
        return print(mensaje)
    function2(mensaje)
    return print(mensaje)
function1()