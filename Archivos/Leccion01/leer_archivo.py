# Para leer un archivo, el modo de apertura sera r de read, lectura

archivo = open('prueba.txt', 'r', encoding='utf8')

# Para leer todo el archivo
#print(archivo.read())

# Para leer algunos caracteres
#print(archivo.read(5)) # solo 5 caracteres

# Para leer lineas completas
# Si no especificamos nada, lee por default la primer linea, y si repetimos la accion de leer la linea, lee la siguiente.
#print(archivo.readline())
#print(archivo.readline())


# Iterar nuestro archivo
#for linea in archivo:
#    print(linea)

# Leer todas las lineas con un solo metodo
#print(archivo.readlines())

# Acceder a una linea de la lista que obtenemos con el metodo readlines
#print(archivo.readlines()[1])

# Crear copia del archivo original
# abrimos un nuevo archivo
# a - utilizamos la opcion 'a', que es para anexar informacion.

archivo2 = open('copia.txt', 'a')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()


# Opciones para la funcion open()
# r - Read -- Abre un archivo en modo lectura. Si no existe da error.
# a - Append -- Abre el archivo para agregar informacion, crea el archivo si no existe.
# w - Write -- Abre el archivo para escribir informacion, si no existe, lo crea y si existe, pisa lo que tiene dentro.
# x - Create -- Crea un archivo especifico. Devuelve un error si el archivo ya existe.
# Tambien existen modos combinados:
# w+ - Escribir y agregar informacion
# r+ - Leer informacion pero tambien par escribir.
# Tambien se puede especificar si el archivo es binario (para las imagenes por ejemplo) o texto:
# t - Text -- Valor por defecto. Modo texto.
# b - Binary -- Modo binario. (Por ejemplo: imagenes)
