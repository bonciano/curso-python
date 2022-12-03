# Cuando trabajamos con clases, la se recomienda comenzar con la clase que no tiene relacion con ninguna otra
# Ejercicio Clase Producto y Orden

class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    # Agregar metodo GET y SET para estos atributos, ya que estan encapsulados
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa',100.00)
    producto2 = Producto('Pantalon',150.00)
    print(producto1)
    print(producto2)