class DispositivoEntrada():
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipo_entrada

    @tipoEntrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Tipo entrada: {self.tipo_entrada}, Marca: {self.marca}'

if __name__ == "__main__":
    dispositivo_entrada1 = DispositivoEntrada('USB','Samsung')
    print(dispositivo_entrada1)

# Finalizada