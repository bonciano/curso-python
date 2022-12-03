try:
    10/0
except Exception as e:
    a = 'Vamos a ver si cuando entra a la excepcion me muestra este texto!'
    print(f'Ocurrio un error: {e}')

try:
    10/0
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}')

print(a)
