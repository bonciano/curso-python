# Concepto de polimorfismo
# Multiples formas en tiempo de ejecucion.
# Una misma variable puede ejecutar varios metodos de distintos objetos dependiendo del objeto al cual esta apuntando en 
# tiempo de ejecucion.
# La variable var (del ejemplo) puede apuntar a cualquier tipo de objeto y ejecutar otro metodo del objeto al que apunta.
# Puede ejecutar cualquier otro metodo, no solamente __str__()

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return f'[Empleado: {self.nombre}, Sueldo: {self.sueldo}]'
    
    def mostrar_detalles(self):
        return self.__str__()

if __name__ == '__main__': # Este if es para que la prueba se ejecute solo si estamos ejecutando este archivo python.
    empleado1 = Empleado('Ruben', 1000)
    print(empleado1.__str__())

