# EJERCICIO CALCULAR AREA DE UN RECTANGULO

class CalcularArea:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


b = float(input('Proporciona la base: '))
a = float(input('Proporciona la altura: '))

area1 = CalcularArea(b,a)
print(f'Area del rectángulo: {area1.area():.2f}')

#
