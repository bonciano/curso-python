# Ejercicio contador de objetos

class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls): # antes estaba la logica en el __init__, ahora independizamos la logica
        # Si quisiera que no se pueda acceder de manera externa deberia colocarle un _ delante del nombre del metodo, asi: _generar_siguiente_valor
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Alberto',33)
print(persona1)

persona2 = Persona('Carlos',32)
print(persona2)

persona3 = Persona('Roberto',31)
print(persona3)

# Reviso que valor tiene la variable de clase contador_personas
print(f'Valor de mi contador: {Persona.contador_personas}')

Persona.generar_siguiente_valor()

persona4 = Persona('Sara',22)
print(persona4)
