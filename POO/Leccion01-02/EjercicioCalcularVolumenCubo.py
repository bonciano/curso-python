# EJERCICIO: CALCULAR VOLUMEN DE UN CUBO

class Cubo:
    def __init__(self,ancho,alto,profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_cubo(self):
        return self.ancho * self.alto * self.profundo

an = int(input('Proporcione el ancho: '))
al = int(input('Proporcione el alto: '))
pr = int(input('Proporcione lo profundo: '))

cubo1 = Cubo(an, al, pr)
print(f'Volúmen cubo: {cubo1.calcular_cubo()}')

#

