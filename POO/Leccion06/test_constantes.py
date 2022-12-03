# from constantes import * # el asterisco es para traer todos los elementos del archivo
# from constantes import MI_CONSTANTE,Matematicas # Otra forma de poder importar
from constantes import MI_CONSTANTE
from constantes import Matematicas as Mate # con el as renombro la clase con un nombre mas corto si quisiera

print(MI_CONSTANTE)
# MI_CONSTANTE = 'Nuevo valor' # Se puede hacer, pero NO SE DEBE HACER porque hay que respetar la convencion
# print(MI_CONSTANTE)

print(Mate.PI)
