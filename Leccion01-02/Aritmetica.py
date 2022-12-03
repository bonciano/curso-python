# Suma, resta, multiplicación y divisió en python
# Ejercicio Clase Aritmetica
#-----------------------------------------------------------------------------
#
# En el metodo sumar, ya no es necesario pasarle parametros, debido a que con self le indico que voy a utilizar los atributos de mi clase.
#
#

class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def division(self):
        if self.operandoB == 0:
            return 'Error al intentar dividir por 0'
        else:
            return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,1)
print(aritmetica1.sumar())

aritmetica2 = Aritmetica(10,5)
print(aritmetica2.restar())

aritmetica3 = Aritmetica(2,2)
print(aritmetica3.multiplicar())

print(f'La resta dio como resultado: {aritmetica2.restar()}')

aritmetica4 = Aritmetica(4,0)
print(aritmetica4.division())


aritmetica5 = Aritmetica(4,2)
print(f'La división da como resultado {aritmetica5.division():.2f}')
#

