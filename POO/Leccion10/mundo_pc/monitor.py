class Monitor:

    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio
    
    # @property
    # def marca(self):
    #     return self._marca
    
    # @marca.setter
    # def marca(self, marca):
    #     pass

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamano: {self._tamanio}'
    

if __name__ == '__main__':
    monitor1 = Monitor('Samsung', '24 pulgadas')
    print(monitor1)
    monitor2 = Monitor('Samsung','28 pulgadas')
    print(monitor2)

# Finalizado - Falta metodos GET y SET para los atributos