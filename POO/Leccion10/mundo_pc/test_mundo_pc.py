
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
from orden import Orden

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('LG', 'USB')
raton2 = Raton('LG', 'USB')
monitor2 = Monitor('LG', 15)
computadora2 = Computadora('LG', monitor2, teclado2, raton2)

teclado3 = Teclado('Bluetooh', 'Gamer')
raton3 = Raton('Bluetooh', 'Gamer')
monitor3 = Monitor('BenQ', 24)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)

# Finalizado