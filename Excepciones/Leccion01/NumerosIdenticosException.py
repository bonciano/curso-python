## Creacion de una clase de excepcion para poner en practica esto.

class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje
