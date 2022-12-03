# Variables de Clase
# Hasta ahora se crearon atributos de instancia.
# Esto quiere decir que se pueden asignar a cada uno de los objetos
# Las variables de clase se asocia sólo a la clase misma y no con los objetos.
# Es decir, la variable de clase, una vez definida se la puede utilizar en los objetos, pero sin modificar el valor para cada objeto, es decir, el valor definido para esa clase es el mismo para todos los objetos que se creen.
# Las variables definidas con el método init corresponden a atributos de instancia, y cuando no se utiliza un metodo para crear variables se las conoce como variables de clase.


class MiClase:
	variable_clase = 'Valor variable clase'

	def __init__(self,variable_instancia):
		self.variable_instancia = variable_instancia

# Los metodos estaticos no pueden acceder a las variables de instancia (porque se crean en el momento en que definimos un objeto), con lo cual, no utilizan la palabra reservada "self" ya que self hace referencia a objetos
# Desde los metodos estáticos podemos acceder solo a las variables de clase y no a las de instancia.
	@staticmethod
	def metodo_estatico():
		print(MiClase.variable_clase)
# Este tipo de métodos sirve para asociar de manera lógica algun metodo que no tenga que ver directamente con los atributos de nuestra clase
# Se puede acceder a las variables de clase de manera indirecta, es decir, hay que utilizar el nombre de la clase seguido del nombre de la variable de clase.
# Generalmente, como no tienen un funcionalidad sobre las instancias, los metodos estaticos suelen reemplazarse por funciones dentro de la logica del proyecto.

# Metodo de clase
	@classmethod
	def metodo_clase(cls): #cls es lo mismo que colocar class, pasa que no podemos usar class porque es una palabra reservada para definir una clase.
		print(cls.variable_clase)
#cls se utiliza para indicar que es el parametro de la clase en si misma que estamos recibiendo. Se puede usar cualquier otro nombre, pero es recomendación del manual de python
	def metodo_instancia(self):
		self.metodo_clase()
		self.metodo_estatico()
		print(self.variable_clase)
		print(self.variable_instancia)

# Para poder acceder a una variable de clase, no necesito crear un objeto:
print(MiClase.variable_clase)

# Para acceder a una variable de instancia, sí necesito crear previamente un objeto:
miClase1 = MiClase('Valor variable instancia')
print(miClase1.variable_instancia)
# Desde el objeto tambien podemos acceder a la variable de clase de esta forma:
print(miClase1.variable_clase)

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# Definicion de una variable de clase al vuelo:
# Tambien se pueden asociar variables de clase al vuelo  (en cualquier momento)
MiClase.variable_clase2 = 'Valor variable clase 2'
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

# Así como tenemos variables de clase, tambien tenemos métodos de clase
# 2 tipos de métodos: estáticos y métodos de clase
# Métodos Estáticos: se asocian con la clase en si misma igual que una variable de clase. Para ejecutarlo hay que llamar primero a la clase y luego al metodo.
# Para indicar que un método es estático, se utiliza el decorador @staticmethod
# Se conoce como Contexto Estático, cuando apenas estamos definiendo variables y métodos de clase. (que no puede acceder a los atributos ni metodos de instancia)
# Se conoce como Contexto Dinámico, cuando ya podemos crear objetos de nuestra clase. (Un objeto si puede acceder al contexto estatico, mientras que los del contexto estatico no pueden acceder al contexto dinamico)
# La clase se carga en memoria la primera vez que se crea un objeto

# Así se ejecuta un método estático, primero hay que colocar el nombre de la clase y luego el nombre del metodo estatico.
MiClase.metodo_estatico()

# Los metodos de clase se invocan de la siguiente manera:
MiClase.metodo_clase()

# La gran diferencia entre un metodo estatico y un metodo de clase, es que en el estatico, para utilizar las variables de clase hay que llamarlas una a una y el metodo no recibe ningun tipo de referencia de la clase; mientras que en los metodos de clase estamos definiendo previamente que el metodo va a estar recibiendo referencias de la clase como atributos o metodos.

# A los metodos de clase se los puede acceder tambien desde un objeto.
miOIbjeto1 = MiClase('variable_instancia')
miOIbjeto1.metodo_clase()
print(miOIbjeto1.variable_instancia)
print(miOIbjeto1.variable_clase)
miOIbjeto1.metodo_instancia()