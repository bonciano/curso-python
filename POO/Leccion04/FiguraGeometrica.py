# HERENCIA MULTIPLE
#--------------------
#Clases abstractas: ahora vamos a convertir la clase FiguraGeometrica en una clase abstracta.
# Para hacerlo hay que extender de otra clase a la vez, en este caso la clase ABC
#ABC = Abstract Base Class
from abc import ABC, abstractmethod #(con la coma indicamos que importamos mas de un elemento del modulo)




class FiguraGeometrica(ABC): # entre parentesis colocamos la clase de la que "hereda" para volverla abstracta
    def __init__(self,ancho,alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    #aca agregamos el metodo abstracto
    @abstractmethod # éste decorador nos sirve para indicar que es un método abstracto
    def calcular_area(self):
        pass #se utiliza para definir el método sin implementación

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
# Cuando creamos un método y colocamos doble guion bajo ("__"), estamos indicando que ese método va a ser privado, cuando colocamos un solo guion bajo ("_") estamos indicando que el metodo es encapsulado (ese metodo no se debe utilizar fuera de la clase)

    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False



#
