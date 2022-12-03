# Esto sirve para capturar errores, por ejemplo, la division por cero.
# Primero le digo que intente hacer la operacion y luego, le coloco except, el objeto de tipo de excepcion, y luego renombro el objeto para poder visualizarlo posteriormente.
try:
    10/0
except Exception as e:
    print(f'Ocurrio un error: {e}')
# Si coloco 'Exception', tal como esta aca arriba, lo que hago es decirle que me capture una excepcion generica, pero si se de que tipo puede ser la excepcion. Aunque siempre conviene capturar excepciones lo mas global posible, tambien se puede capturar excepciones de forma mas especifica, tal cual vemos aca abajo:

try:
    10/0
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}')