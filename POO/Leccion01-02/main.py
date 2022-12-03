# Comentario
print("Hola Mundo")
print("Esto es una prueba para ver cómo funciona PYTHON")
# Las variables se almacenan en la memoria ram, con lo cual, cuando se reejecuta el código no vuelve a tener la misma dirección de memoria.
#Variable:
x=10
y=20
if x+y==30 : 
	print("Es 30") 
else :
	print("Error")

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

print("Es Mayor") if x > y else print("Es menor")

#Direcciones de memoria
print("Esto es la direccion de memoria de la variable X " + str(id(x))) #print(id(x)))

#Tipos de datos en Python (Todos los tipos de datos tambien son almacenados en CLASES)
#Numeric (integer, complex number, float)
#Dictionary
#Boolean
#Set
#Sequence type (strings, list, tuple)

#para saber que tipo de dato contiene una variable:
print(type(x))

########## LAS VARIABLES EN PYTHON SON DINAMICAS!!!!

z=10.5
print(z)
print(type(z))
z='Hola, mi nombre es Culebra Connor'
print(z)
print(type(z))

#Booleano (siempre respetar mayusculas y minusculas)
t=True
f=False

print(type(t))


#Resumen de tipos de datos
#tipo entero
x=10
#tipo flotante
x=11.5
#tipo string
x='Hola papá'
#tipo booleano
x=True
x=False

#manejo de cadenas de caracteres
miGrupoFavorito = 'La Renga'
print(miGrupoFavorito)
#concatenar
print("Mi grupo favorito es " + miGrupoFavorito)
miGrupoFavorito='La Renga' + 'La mejor banda'
print(miGrupoFavorito)
#otra forma de imprimir variables
print("mi grupo favorito es:",miGrupoFavorito) # Sirve para imprimir un vector o matriz
#suma de variables
n1=1
n2=1
print("el resultado es: ", int(n1)+int(n2))

#tipos booleanos (nos permite saber si un valor es verdadero o falso)
miVariable=True
miVariable=False
print(miVariable)

miVariable = 3>1
print(miVariable)

#estructura if
if miVariable:
	print("verdadero")
else:
	print("falso")


#procesar la entrada de usuario
#funcion input 
resultado = input()
print(resultado)


#nueva forma de imprimir datos (la mas uilizada)
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print(f'El resultado es {suma} ')

resta = operandoA - operandoB
print(f'el resultado de la resta es {resta} ')
multiplica = operandoA * operandoB
print(f'el resultado de la multiplicación es {multiplica} ')
division = operandoA / operandoB
print(f'el resultado de la división es {division} ')
divisionInt = operandoA // operandoB
print(f'el resultado de la division entera es {divisionInt} ')
potencia = operandoA ** operandoB
print(f'el resultado de la potencia es {potencia} ')

input('fin')

#        >     <
# ejercicio 1
numeroA = int(input('Por favor ingrese un numero: '))
if numeroA % 2 == 0:
	print(f'El numero {numeroA} es par')
else:
	print(f'El numero {numeroA} no es par')

# otro ejercicio
adulto = 18
edad = int(input('Por favor ingrese su edad: '))
if edad >= adulto:
	print('Usted es adulto')
else:
	print('Usted es menor')

# Operadores logicos (and, or, not)
a = int(input("Ingrese un valor: "))
if a>=0 and a<=5:
	print(f'El valor {a} está entre 0 y 5')
else:
	print(f'El valor {a} no está entre 0 y 5')

# Operadores logicos
a = int(input("Ingrese un valor: "))
if a>=0 and a<=5:
	print(f'El valor {a} está entre 0 y 5')
else:
	print(f'El valor {a} no está entre 0 y 5')

# Ejercicio Operadores logicos
print('Proporcione los sieguientes datos del Libro:')
a=input('Proporcione el nombre del libro: ')
b=int(input('Proporcione el ID: '))
c=float(input('Proporcione el precio del libro: '))

print(f'El libro que desea comprar es {a}.')
print(f'El ID del libro es {b}.')
print(f'El precio del libro es {c}.')

if c>100.00:
	print('El envío es GRATUITO')
else:
	print('El envío NO es gratuito')

# Para imprimir en varias lineas, colocar comillas triples en el inicio y el fin de todo el bloque de texto.
print(f'''
Esto es una cadena
en varias lineas
porque soy re heavy
re jodido
''')


#conversion de valor numerico a texto
n1 = int(input("Proporcionar un valor entre 1 y 3"))

if n1 == 1:
	numeroTexto = 'Número uno'
elif n1 == 2:
	numeroTexto = 'Número dos'
elif n1 == 3:
	numeroTexto = 'Número tres'
else:
	numeroTexto = 'Número fuera de rango'

print(f'Número prorcionado: {n1} - {numeroTexto}')


#conversion de valor numerico a texto
n1 = int(input("Proporcionar un valor entre 1 y 3: "))

if n1 == 1:
	numeroTexto = 'Número uno'
elif n1 == 2:
	numeroTexto = 'Número dos'
elif n1 == 3:
	numeroTexto = 'Número tres'
else:
	numeroTexto = 'Número fuera de rango'

print(f'Número prorcionado: {n1} - {numeroTexto}')
input("Presione una tecla para continuar...")

# operador if else simplificado
condicion = False

if condicion:
	print(f'Condición verdadera')
else:
	print(f'Condición falsa')

print(f'Condición verdadera') if condicion else print(f'Condición falsa')


# operador if else simplificado
mes = int(input('Ingrese el mes del año: '))
estacion = None #indica que esta variable no contiene ningun valor

if 1 <= mes <= 3:
	estacion = 'Verano'
elif 4 <= mes <= 6:
	estacion = 'Otoño'
elif 7 <= mes <= 9:
	estacion = 'Invierno'
elif 10 <= mes <= 12:
	estacion = 'Primavera'
else:
	estacion = 'Valor incorrecto'

print(f'El mes {mes} corresponde a la estación {estacion}')

# Ciclo while
vari = int(input('Ingrese un valor: '))
num = 0

while vari == 1:
	num = num + 1
	print(f'El valor es correcto y la suma es {num}')
	vari = int(input('Ingrese un valor: '))
else:
	print(f'Fin del ciclo while.')

# Ciclo for (Se utiliza mas para listar una cadena de datos)
# Una cadena es un arreglo (conjunto de datos) de caracteres. Es decir print(cadena[1]) es "o"
cadena = 'Hola' 

for letra in cadena:
	print(f'La letra correspondiente a la cadena "{cadena}" es: {letra}')
else:
	print('Fin de la cadena')



for letra in 'Holanda':
	if letra == 'a':
		print(f'Letra encontrada: {letra}')
		break
else:
	print(f'Fin ciclo for')

print('es el fin????')
print('-------------------------------------')
for i in range(6):
	if i % 2 == 0:
		print(f' El valor de i es: {i}')
print('-------------------------------------')

#Palabra reservada continue
for i in range(6):
	if i % 2 != 0:
		continue # Continue ejecuta la siguiente iteracion | Brake sale de todo
	print(f'Valor: {i}')

	

# Listas - Conjunto de elementos
nombre = ['Juan','Carla','Ricardo','Maria',1,True] 
# En python, las listas pueden tener distintos tipos de datos
for i in nombre:
	print(i)
else:
	print('----- Fin de la lista -----')

print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])

print('----- Fin de la lista -----')
#Accediendo a los elementos de manera inversa
print(nombre[-1])

#Acceder a rangos de una lista
print(nombre[0:2]) # No incluye el indice 2

#Ir del inicio de la lista al indice sin incluirlo
print(nombre[:3])

#Desde el indice indicado hasta el final de nuestra lista
print(nombre[1:]) 

nombre[3] = 'Ivone'

print(nombre[1:]) 

# Preguntar largo de una lista
print(len(nombre))

#Agregar un elemento a la lista
nombre.append('Rigoberto')
print(nombre)

#Insertar un elemento en un indice en especifico
nombre.insert(1,'Octavio')
print(nombre)

#Remover un elemento de la lista
nombre.remove('Octavio')
print(nombre)

#Remover el ultimo valor agregado a la lista
nombre.pop()
print(nombre)

#Eliminar un elemento en un indice indicado
del nombre[0]
print(nombre)

#Limpiar todos los elementos de la lista
nombre.clear()
print(nombre)

#Borrar la lista por completo
del nombre
# print(nombre) -------- Error porque no existe.

# Tuplas - Es una lista a la que no se le puede borrar, insertar, agregar elementos.
# Tipo inmutable

frutas = ('Naranja','Banana','Manzana')

#Saber cantidad de elementos de la tupla
print(len(frutas))
print(frutas)

#Acceder a un elmento
print(frutas[0])

#Navegación inversa
print(frutas[-1])

#Acceder a un rango de valores
print(frutas[0:1]) #sin incluir el indice 2

#-------------------------------------------------
#Parte 2

for fruta in frutas:
	print(fruta, end=' ')

#Cambiar valor tupla
#frutas[0] = 'Pera'
#Se cambia la tupla a lista, se modifica y luego se vuelve a poner como tupla

frutasLista = list(frutas) #list() convierte la tupla en lista
frutasLista[0] = 'Pera'
frutas = tuple(frutas) #tuple() convierte una lista en tupla
for fruta in frutas:
	print('\n',fruta, end = ' - ')

#Eliminar por completo la tupla:
del frutas

#Ejercicio
#Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando el ciclo for: tupla = (13,1,8,3,2,5,8)

tupla = (13,1,8,3,2,5,8)
lista = []

for i in tupla:
	if int(i) < 5:
		lista.append(i)

for l in lista:
	print(l)


# Colección de tipo SET 
# un SET no mantiene un orden, no admite duplicados, no es posible modificar sus elementos, sí es posible agregar mas elementos o eliminarlos.
# cuando decimos que no mantiene un orden, es porque no tiene indices.

planetas = {'Marte','Jupiter','Venus'}
print(planetas)
#conocer el largo de los elementos
print(len(planetas))

#Revisar si un elemento esta presente en el set
print('Marte' in planetas)
print('Martes' in planetas) #estas preguntas se pueden usar tambien en listas y tuplas

#Agregar elementos
planetas.add('Tierra')
print(planetas)

#no se puede duplicar elementos
planetas.add('Tierra')
print(planetas)

# eliminar elementos (posiblemente arrojando error)
planetas.remove('Tierra')
print(planetas)
planetas.discard('Jupiters') #Sirve para eliminar elementos de un tipo set sin arrojar error

#limpiar set
planetas.clear()
print(planetas)

#eliminar set
del planetas
print(planetas) #si la quiero imprimir, me da error porque ya no existe



#Diccionarios
#Coleccion de datos organizados por key y value.
#dict(key,value)
diccionario = {
	'IDE':'Entorno de desarrollo',
	'OOP':'Programacion orientada a objetos',
	'DBMS':'Gestor de base de datos'
}

print(diccionario)

#conocer el largo de los elementos del diccionario
print(len(diccionario))

#acceder a un elemento del diccionario (no existen indices)
#para acceder, proporcionar la key
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#modificar elementos de un diccionario
diccionario['IDE'] = 'entorno de desarrollo'
print(diccionario)

#recorrer elementos de un diccionario
for termino,valor in diccionario.items():
	print(termino,valor)

#recuperando solo las key sin el termino asociado
for termino in diccionario.keys():
	print(termino)

#recuperar solo los valores de las keys
for termino in diccionario.values():
	print(termino)

#comprobar si ya existe un elemento
print('IDE' in diccionario)
print('ide' in diccionario) #el diccionario es CASE SENSITIVE

#agregar elemento en el diccionario
diccionario['PK'] = 'Llave primaria'
print(diccionario)

#remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#limpiar el diccionario
diccionario.clear()
print(diccionario)

#eliminar la variable de diccionario
del diccionario
#print(diccionario)


#FUNCIONES
#Bloque de codigo que se puede llamar n veces.
#def para indicar que vamos a definir una funcion

def miFuncionA():
	print('Saludos desde mi funcion')

miFuncionA()

#Pasar parametros a la funcion (argumentos)
def miFuncionB(nombre,apellido):
	print(f'Nombre: {nombre}, Apellido: {apellido}')

miFuncionB('Roberto','Gomez')
miFuncionB('Carla','Lara')

#palabra reservada return
def sumar(a,b):
	return a + b

resultado = sumar(3,4)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(3,4)}')

#valores por default a los parametros de las funciones
#def sumar(a:int = 0, b:int = 0) -> int: #esos son los valores por default (el -> se utiliza para dar mas detalle del tipo de dato que devuelve la funcion)
def sumar(a = 0,b = 0): 
 	return a + b

resultado = sumar()
print(f'El resultado de la suma es: {resultado}')
resultado = sumar(4,5)
print(f'El resultado de la suma es: {resultado}')

# Argumentos variables en Python
#con el '*' le indico que no sé cuántos elementos puedo recibir como argumento.
#internamente python lo interpreta como TUPLA
def listarNombres(*nombres):
	for nombre in nombres:
		print(nombre)

listarNombres('Lucas','Juan','Marcos','Sonia','Tahiel')
listarNombres('Ricardo','Roberto')


#FUNCIONES Ejercicio
#Tarea: Función con argumentos variables para sumar todos los valores recibidos
def sumaValores(*numeros):
	suma = 0
	for numero in numeros:
		suma += numero
	return print(suma)

sumaValores(1,2,3)


#Tarea: Función con argumentos variables para multiplicar los valores
def multiplicaValores(*numeros):
	res = 1
	for numero in numeros:
		res *= numero
	return print(res)

multiplicaValores(4,4)



#Funcion para definir lista de terminos (con diccionarios)

def listarTerminos(**terminos): # con el doble * le decimos que pasamos un diccionario
	for llave,valor in terminos.items():
		print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated development environment', PK='Primary Key')
listarTerminos(DBMS='Gestor de base de datos')

# Definir una funcion que recibe una lista de elementos y que accede a cada elemnto
def desplegarNombres(nombres):
	for nombre in nombres:
		print(nombre)

nombres = ['Juan','Carla','Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
#desplegarNombres(10,11) # No es un elemento iterable
desplegarNombres((10,11)) # El paréntesis lo convierte en una TUPLA y sí es iterable
desplegarNombres([10,11]) # El corchete lo convierte en una LISTA


#FUNCIONES RECURSIVAS
#Funcion que se manda a llamar a si misma para completar cierta tarea
#Ejemplo clásico es el factorial

def factorial(numero):
	if numero == 1:
		return 1
	else:
		return numero * factorial(numero - 1)

numero = 3
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')


#FUNCIONES RECURSIVAS
#Funcion que se manda a llamar a si misma para completar cierta tarea
#Ejemplo clásico es el factorial
#La mierda que hice yo
def imprimirNumero(numero):
	if numero < 1:
		return print('No es un número válido.')
	else:
		if numero == 1:
			return 1
		else: 
			print(numero)
			return print(imprimirNumero(numero - 1))
		

num = 5
res = imprimirNumero(num)
print(res)


#Versus lo que hizo el profesor:
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero-1)

imprimir_numero_recursivo(5)



#EJERCICIO - Calculadora de Impuestos
#Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
#La función se llama calcular_total()
#La función recibe dos parámetros:
#1. pago_sin_impuesto
#2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)
#La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.
#Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0
#Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.



def calcular_total(pago_sin_impuesto = 0,impuesto = 0):
	if pago_sin_impuesto:
		if impuesto > 0:
			return pago_sin_impuesto * (1 + (impuesto / 100))
		else:
			return pago_sin_impuesto
	else:
		return 0


print(f'Bienvenido al sistema de cálculo de impuesto \n')
pago_sin_impuesto = float(input('Pago sin impuesto: '))
impuesto = float(input('Impuesto: '))

print(f'El total a pagar es de: {calcular_total(pago_sin_impuesto,impuesto)}')


# EJERCICIO
#Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
#Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a fahrenheit
#La función se llama: celsius_fahrenheit(celsius) 
#La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32 
#Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius:
#fahrenheit_celsius(fahrenheit)         
#La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9
#Los valores los debe proporcionar el usuario, utilizando la función input y convirtiendolo a tipo float.
#Deben hacer al menos dos pruebas, una donde conviertan de grados celcius a grados fahrenheit, y otra donde conviertan de grados fahrenheit a grados celsius y mandar a imprimir los resultados.

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
        return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
        return (fahrenheit-32) * 5/9

# Realizamos algunas pruebas de conversión
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Los dos puntos después de la variable de resultado dan un formato de 2 digitos flotantes
print(f'{celsius} C a F: {resultado:.2f}')
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f}')

# CLASES Y OBJETOS
#CLASES
#se recomienda que el nombre del archivo y el nombre de la clase lleven la notacion de mayúsculas y minúsculas.
#ej: PersonaAdulta (esa es la clase) - Archivo PersonaAdulta.py
class Persona:
	#pass # esta palabra reservada se utiliza tanto en clases como en funciones para indicar que está vacía
	#para agregar características o atributos a una clase se necesita un metodo llamado 'init' - similar a un constructor
	def __init__(self): #métodos dunder (double underscore)
		self.nombre = 'Juan'
		self.apellido = 'Perez'
		self.edad = 28


#print(type(Persona))
persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


# ----------------------------------------------------------------------------------------------
class Persona:
	def __init__(self, nombre, apellido, edad): 
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

persona1 = Persona('Laura','Sanchez',32)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)



# ----------------------------------------------------------------------------------------------
class Persona:
	def __init__(self, nombre, apellido, edad): # Estos son atributos de objeto o de instancia, por ende no comparten información entre objetos.
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

persona1 = Persona('Laura','Sanchez',32)
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido}, edad {persona1.edad}')

persona2 = Persona('Loro','Carlos',32)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido}, edad {persona2.edad}')

## CLASES Y OBJETOS
#CLASES
# ----------------------------------------------------------------------------------------------
# Modificar valores de una instancia
class Persona:
	def __init__(self, nombre, apellido, edad): # Estos son atributos de objeto o de instancia, por ende no comparten información entre objetos.
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

persona1 = Persona('Laura','Sanchez',32)
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido}, edad {persona1.edad}')

persona1 = Persona('Ciro','Gonzalez',33)
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido}, edad {persona1.edad}')

persona2 = Persona('Loro','Carlos',32)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido}, edad {persona2.edad}')

 ## CLASES Y OBJETOS
#CLASES
# ----------------------------------------------------------------------------------------------
# Creación de de método dentro de la clase 
# Estos son atributos de objeto o de instancia, por ende no comparten información entre objetos.
# self se conoce como metodo de instancia porque se asocia a los objetos que se crea - se llama a self sólo dentro de la definición de nuestra clase
 
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, Edad: {self.edad}')

persona0 = Persona('Carlos','Carmen',11)
persona0.mostrar_detalle()

## CLASES Y OBJETOS
#CLASES
# ----------------------------------------------------------------------------------------------
# Más sobre "self" y atributos de instancia 
# La variable self es como el this en otros lenguajes de programación
# Puede tener otro nombre como this, pero la recomendación es que se use self
# Se puede llamar directamente al método con el nombre de nuestra clase sin pasar por una variable

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, Edad: {self.edad}')

persona0 = Persona('Carlos','Carmen',11)
persona0.mostrar_detalle()


persona1 = Persona('Carlos','Carmen',11)
persona1.telefono='1123232331'
persona1.mostrar_detalle()
print(persona1.telefono)

# La ventaja de trabajar con python y la poo es que en cualquier momento podemos agregarle atributos a nuestro objeto. Igualmente, si le agrego un atributo al vuelo, esos atributos no se van a compartir con otros objetos.
#Persona.mostrar_detalle(persona0)
# Esta forma no es la común, es solamente otra forma de llamar al método.

# Suma, resta, multiplicación y divisió en python
# Ejercicio Clase Aritmetica
#-----------------------------------------------------------------------------
#
# En el metodo sumar, ya no es necesario pasarle parametros, debido a que con self le indico que voy a utilizar los atributos de mi clase.
#
#

class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

aritmetica1 = Aritmetica(5,1)
print(aritmetica1.sumar())

#
# Suma, resta, multiplicación y divisió en python
# Ejercicio Clase Aritmetica
#-----------------------------------------------------------------------------
#
# En el metodo sumar, ya no es necesario pasarle parametros, debido a que con self le indico que voy a utilizar los atributos de mi clase.
#
#

class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def division(self):
        if self.operandoB == 0:
            return 'Error al intentar dividir por 0'
        else:
            return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,1)
print(aritmetica1.sumar())

aritmetica2 = Aritmetica(10,5)
print(aritmetica2.restar())

aritmetica3 = Aritmetica(2,2)
print(aritmetica3.multiplicar())

print(f'La resta dio como resultado: {aritmetica2.restar()}')

aritmetica4 = Aritmetica(4,0)
print(aritmetica4.division())


aritmetica5 = Aritmetica(4,2)
print(f'La división da como resultado {aritmetica5.division():.2f}')
#

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

## CLASES Y OBJETOS
# ----------------------------------------------------------------------------------------------
# ROBUSTECIENDO EL METODO INIT
# Para pasar una tupla de valores podemos pasar *args y para un diccionario de datos podemos pasar **kargs (aunque a éstas palabras reservadas le podemos poner nombres)

class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, Edad: {self.edad} {self.valores} {self.terminos}')

persona0 = Persona('Carlos','Carmen',11,'1133223322', 2, 3, 5, m='manzana', p='pera')
persona0.mostrar_detalle()

persona1 = Persona('Roberta', 'Tarrox', 30)
persona1.mostrar_detalle()

#

 ## CLASES Y OBJETOS
## ENCAPSULAMIENTO!!!!
# ----------------------------------------------------------------------------------------------
# Encapsulamiento
# Cuando no hay encapsulamiento, se puede acceder públicamente a los atributos de la clase, pero ésto no es seguro, lo que se recomienda es no poder acceder directamente a sus atributos. Se utiliza un _ en la definicion de atributos de una clase de ésta forma:
# Python no funciona como otros lenguajes de programación en donde tenemos modificadores de acceso (self._nombre = nombre NO FUNCIONA), en éste caso es solo una sugerencia al programador para que no utilice las líneas de código de reemplazo de atributos.
# Para evitar que se modifiquen atributos (realmente) como medida de seguridad (aunque es poco frecuente) (self.__nombre = nombre)
# Resumiendo, la práctica más comun y la que vamos a utilizar en el curso es con un sólo _ para indicar encapsulamiento.

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.apellido}, Edad: {self.edad}')


persona1 = Persona('Roberta', 'Tarrox', 30)
persona1.__nombre = 'Juan Carlos'
persona1.mostrar_detalle()

#

   
## CLASES Y OBJETOS
## ENCAPSULAMIENTO
# ----------------------------------------------------------------------------------------------
# Metodos Get y Set
# El encapsulamiento subjetivo es que no podamos acceder de manera directa a los atributos de nuestra clase.
# Metodo get = obtener/recuperar
# Metodo set = colocar/modificar
# Para asegurarnos de que no se acceda a atributos encapsulado, se utiliza el decorador (modifica el comportamiento de nuestro metodo). En este caso vamos a modificar el comportamiento de nuestro metodo del tipo get.
# El decorador @property le indica a un metodo que se puede acceder como si fuera un atributo.
# Y si queremos definir el metodo set para modificar el atributo de nombre: @nombre.setter

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print('Llamando metodo get nombre (Esto es solo para ver que estamos llamando al metodo y no al atributo)')
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        print('Llamando metodo set nombre (Misma comprobación que con get)')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido}, Edad: {self.edad}')


persona1 = Persona('Roberta', 'Tarrox', 30)
print(persona1._nombre) # Esto ya no se debe hacer
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)

#

  ## CLASES Y OBJETOS
## ENCAPSULAMIENTO
# ----------------------------------------------------------------------------------------------
# Metodos Get y Set
# Atributos read-only (solo lectura)
# Si quisieramos evitar modificar un atributo, se podría hacer quitando la funcion set del atributo (aunque nos daría error), sin embargo se podría utilizar _nombre (aunque si queremos demostrar que sabemos python, NO SE DEBE HACER).
# Este tipo de código se lo conoce como variables de solo lectura.

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print('Llamando metodo get nombre (Esto es solo para ver que estamos llamando al metodo y no al atributo)')
        return self._nombre

#   @nombre.setter
#   def nombre(self,nombre):
#       print('Llamando metodo set nombre (Misma comprobación que con get)')
#       self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido}, Edad: {self.edad}')


persona1 = Persona('Roberta', 'Tarrox', 30)
print(persona1._nombre) # Esto ya no se debe hacer
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)

#

  ## CLASES Y OBJETOS
## ENCAPSULAMIENTO
# ----------------------------------------------------------------------------------------------
# Encapsulando todos los atributos de una clase

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido}, Edad: {self._edad}')

# Cuando un metodo DENTRO de nuestra clase muestre atributos, sí se puede hacer accediendo directamente a los atributos encapsulados. Cuando lo hacemos por medio de un objeto, está PROHIBIDO accederlo directamente, sino que hay que utilizar los métodos set y get.

persona1 = Persona('Roberta', 'Tarrox', 30)
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
persona1.apellido = 'Gimenez'
print(persona1.apellido)
persona1.edad = '33'
print(persona1.edad)
persona1.mostrar_detalle()

#

  # MODULO
# Archivo o módulo es lo mismo
#---------------------------------------------------
# from nombre_del_archivo import clase_del_archivo
# Si quisiera importar todas las clases de un archivo, en la clase pongo *:
# from Persona import *

from Persona import Persona

persona1 = Persona('Carla','Gomez',39)
persona1.mostrar_detalle()

# MODULO
# Comprobación del Módulo en Ejecución
#---------------------------------------------------
# Para identificar desde qué módulo se está creando el objeto de la clase que se importa, se coloca "print(__name__)" al final de los archivos de las clases que estamos importando y el archivo que estamos utilizando actualmente. Esto nos da como resultado que las líneas de código que se ejecutan, si no son del archivo que se está utilizando actualmente, son de tal archivo o módulo, mientras que cuando son del archivo que estamos trabajando actualmente, nos muestra __main__ en el log.
# 

from Persona import Persona

persona1 = Persona('Carla','Gomez',39)
persona1.mostrar_detalle()

print(__name__)

#

# MODULO
# Destructor de objetos en python
#---------------------------------------------------
# En algunos casos, cuando creamos objetos, necesitamos liberar ciertos recursos.
# Creación del método destructor

from Persona import Persona

print('Creación objetos'.center(50,'-'))
persona1 = Persona('Carla','Gomez',39)
persona1.mostrar_detalle()

print('Eliminación de objetos'.center(50,'-'))
del persona1

#No es tan común en python ver que se eliminen objetos, debido a que existe un concepto llamado "Recolector de basura" que se encarga de liberar recursos que no se estén utilizando.
##

## CLASES, METODOS Y OBJETOS
# Concepto de HERENCIA
#-------------------------------------------------------
# Un clase Empleado que posee el atributo salario, hereda atributos de la clase Persona.

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

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

empleado1 = Empleado('Juan',25,5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#

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

# CLASES, METODOS Y OBJETOS
# Concepto de HERENCIA
# Sobreescritura del método __str__()
#---------------------------------------------------------------------------------
from Persona import * #importo todas las clases del módulo

persona1 = Persona('Juan',28)
print(persona1)

empleado1 = Empleado('Carla',22,5000)
print(empleado1)
#cuando se imprime la clase heredada, a pesar de escribirse 
print(empleado1)
#de forma implicita lo que está haciendo es ejecutar el método de esta forma
print(empleado1.__str__())

#
# El método __str__() nos imprime el valor de la direccion de memoria donde se ubica el objeto
# Lo común es que se envíe una representación del texto de cada uno de los objetos, para lo cual, se utiliza el método __str__() de la clase object.
# Sobreescribir el método __str__() significa que se está volviendo a llamar el método de la clase padre en las clases a las que querramos ir agregándolo.



