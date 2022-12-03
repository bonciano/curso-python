class Vehiculo:
    def __init__(self,color,ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'Color: {self._color}, Ruedas: {self._ruedas}'

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        self._velocidad = velocidad
        super().__init__(color,ruedas)

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self._velocidad} km/h'

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        self._tipo = tipo
        super().__init__(color,ruedas)

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Tipo: {self._tipo}'

vehiculo1 = Vehiculo('Rojo',4)
print(vehiculo1)

vehiculo2 = Coche('Blanco',4,150)
print(vehiculo2)

vehiculo3 = Bicicleta('Azul',2,'Urbana')
print(vehiculo3)

