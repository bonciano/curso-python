## CLASES, METODOS Y OBJETOS
# Concepto de HERENCIA
# Sobreescritura del método __str__()
#-------------------------------------------------------
# 

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Persona[Nombre: {self._nombre}, Edad: {self._edad}]'

    @property
    def nombre(self):
        return self._nombre 

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

# Para decirle a una clase de qué otra clase vamos a heredar atributos, se coloca entre paréntesis el nombre de la clase de la que se hereda.

# Para inicializar correctamente la clase hija, hay que llamar al constructor de la clase padre, y se hace con la palabra reservada "super()"
# super() es un método que nos va a permitir acceder a los métodos de la clase padre
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        self._sueldo = sueldo
        super().__init__(nombre, edad)

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Sueldo: {self._sueldo}] {super().__str__()}' 

# El método super() nos permite acceder a los atributos y métodos de la clase padre.
#


