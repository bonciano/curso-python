## Manejo de excepciones -- bloques else y finally
from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer Numero: '))
    b = int(input('Segundo Numero: '))
    resultado = a/b
    if a == b:
        ## raise se utiliza para lanzar manualmente una excepcion.
        raise NumerosIdenticosException('Numeros identicos')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:
    ## Es un bloque completamente opcional
    ## Se ejecuta si no salio por ninguna excepcion
    print('No se arrojo ninguna excepcion')
finally:
    ## Tambien es un bloque opcional
    ## Se ejecuta siempre
    ## Este bloque se puede utilizar para liberar algun recurso, para dar aviso que se finalizo una validacion, etc.
    print('Validacion realizada con exito')

print(f'Resultado {resultado}')
print('Continuamos..')
