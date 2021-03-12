import unittest

def suma(num_1, num_2):
    """
    Funcion que suma dos numeros.
    Num_1 = primer numero  en leer.
    Num_2 = segundo numero en leer.
    Return la sumatoria de los 2 numeros
    """

    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

if __name__ == "__main__":
    unittest.main()