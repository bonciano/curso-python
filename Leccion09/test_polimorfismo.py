from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
         print(objeto.departamento)

empleado = Empleado('Roberto',2500)
imprimir_detalles(empleado)

gerente = Gerente('Carla',6000,'Sistemas')
imprimir_detalles(gerente)

''' *********************************************************************************

Cuando definimos la funcion imprimir_detalles, al estar haciendo un print del objeto y que existe la funcion __str__
dentro de las clases (que en este caso son clases heredadas, pero puede que no los sea), python interpreta que se esta 
invocando a la funcion __str__ e imprime la misma.

Debido a que en este momento estamos heredando el mismo codigo del objeto padre al objeto hijo, si mando a llamar la funcion
__str__() a traves de mostrar_detalles(), por herencia va a ejecutar el metodo __str__() de la clase hija, ya que ademas de
heredarla, mostrar_detalles() hace referencia a la construccion del metodo __str__() que esta definido tambien en la clase hija.

El metodo isinstance() nos permite identificar si el atributo que estamos intentando recuperar existe en la clase
del objeto creado.

En Python no se recomienda agregar tantas validaciones de tipos de datos, sino que la recomendacion es que mayormente se
escriba codigo lo mas generico posible para no andar haciendo tantas validaciones de datos.
Solo se recomienda validaciones especificas.

********************************************************************************* ''' 

