# Con la palabra with (manejador de contexto) python abre y cierra el archivo de manera automatica.
#
#with open('prueba.txt','r',encoding='utf8') as archivo:
#    print(archivo.read())

# Manejo de archivos con nuestra propia clase
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
