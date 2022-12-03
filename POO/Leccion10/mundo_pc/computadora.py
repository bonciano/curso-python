from teclado import Teclado
from monitor import Monitor
from raton import Raton

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''
    # Cada uno de estos objetos tiene ya definido su propio metodo str, por lo tanto se va a mandar a llamar el metodo str en cada uno de esos objetos.

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('LG', 'USB')
    raton2 = Raton('LG', 'USB')
    monitor2 = Monitor('LG', 15)
    computadora2 = Computadora('LG', monitor2, teclado2, raton2)
    print(computadora2)

# Finalizado