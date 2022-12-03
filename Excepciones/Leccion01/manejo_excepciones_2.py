resultado = None
a = '10'
b = 0

try:
    resultado = a/b
except Exception as e:
    print(f'Error al intentar realizar la operacion: {e}')

print(f'El resultado de la division es: {resultado}')
print(f'Continuamos..')