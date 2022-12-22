# Podemos crear una clase para realizar el manejo de archivos
class ManejoArchivos:
    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre,'r',encoding='utf8')
        return self.nombre

    def __exit__(self,tipo_excepcion,valor_excepcion,traza_error):
        # Los parametros despues del self no son necesarios agregarlos, pero si los tenemos que poner como parametros para cumplir con la firma de este metodo
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre: # Se coloca asi porque evalua si ese atributo de nombre esta apuntando a un tipo de objeto todavia.
            self.nombre.close()

# Los metodos __enter__ y __exit__ tambien se pueden utilizar para abrir y cerrar conexiones a la base de datos.
