
# Abrir un archivo. Con open() tambien podemos crear un archivo en caso de que no exista. Lo comun es que se escriba dentro de un bloque try except, por si llegara a dar algun error la creacion del mismo.

try:
    print('Se abre el archivo prueba.txt')
    archivo = open('prueba.txt', 'w', encoding='utf8') # La w es para indicar write (escritura) - el encoding es para decirle que mapa de caracteres utilizar
    print('Se agrega informacion al archivo.')
    archivo.write('Agregamos informacion al archivo\n') # Este metodo write es para escribir dentro del archivo
    archivo.write('Adios')
except Exception as e:
    print(f'Error al intentar crear el archivo {e}')
finally:
    archivo.close()
    print('Se cierra el archivo')

