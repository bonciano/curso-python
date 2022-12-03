# HERENCIA MULTIPLE
# Prueba
#
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica # solo para la prueba de abstracción

print('Creacion Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado = 5, color = 'Rojo')
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
#print(cuadrado1.color)
#print(cuadrado1.calcular_area())

# Cuando trabajamos con herencias multiples, es importante el orden en que se mandan a llamar las clases padre.

# Método MRO : Method Resolution Order
print(Cuadrado.mro())
# Sirve para saber el orden en que se van a llamar las clases, para tener referencia por si tenemos dudas.


cuadrado1.alto = -10
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)


print('Creacion Objeto Rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho = 9, alto = 8, color = 'verde')
rectangulo1.ancho = 15
# Si se quisiera evitar modificar un atributo del objeto, deberíamos hacer que las propiedades de la clase sean sólo lectura.
# Para hacerlo, habría que eliminar los metodos SET definidos en la clase Rectángulo (por ejmeplo) 


print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#Validaciones de la aplicación de FiguraGeometrica
# Se realizaron en las validaciones dentro de las clases para que esté dentro de rangos soportados.
# También se podría validar el color, que sea de tipo string, o que esté dentro de una gama de colores.

# Clases Abstactas:
# La clase FiguraGeometrica, hasta el momento no tenía un método llamado área, debido a que FiguraGeometrica por sí sola no es una figura, sino que hay que especificarle qué figura quiero calcular.
# Pero definiendo a la clase padre como abstracta y obligar a las clases hijas a crear un método area, podemos agragar en la clase padre un método abstracto.
# IMPORTANTE!!!: Si en una clase agregamos un método abstracto, toda la clase se vuelve abstracta.
# Esto quiere decir que no podemos crear instancias u objetos de una clase abstracta, asi que no podemos crear objetos de nuestra clase FiguraGeometrica. Esto en nuestro modelo esta bien, porque no se puede calcular el area si no se conoce la figura a la que se le desea calcular el area.
# ** modificaciones en los scripts ** (solo impacta en las clases padre)

#tratamos de crear un objeto de la clase FiguraGeometrica
# figura = FiguraGeometrica()
# no se puede instanciar una clase abstracta


# Cuando se coloca a la clase padre como abstracta, ésto modifica la estructura de jerarquía de clases
# y el Method Resolution Order nos muestra como queda
print(Cuadrado.mro())