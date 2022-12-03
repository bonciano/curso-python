resultado = None
a = '10'
b = 0

try:
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Error al intentar realizar la operacion: {zde}, {type(zde)}')
except TypeError as te:
    print(f'TypeError - Error al intentar realizar la operacion: {te}, {type(te)}')
except Exception as e:
    print(f'Exception - Error al intentar realizar la operacion: {e}, {type(e)}')

# Si voy a colocar la opcion Exception (que es mas general), debo hacerlo a lo ultimo, ya que primero recorro las especificas, y si no corresponde a ninguna excepcion de las colocadas, sale por la general.

print(f'El resultado de la division es: {resultado}')
print(f'Continuamos..')