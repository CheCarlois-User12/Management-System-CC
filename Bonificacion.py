class Bonificacion:
    def __init__(self, bon_codigo=None, bon_descripcion=None, bon_valor=None):
        self._bon_codigo = bon_codigo
        self._bon_descripcion = bon_descripcion
        self._bon_valor = bon_valor

    def __str__(self):
        return f'Código: {self._bon_codigo}, Descripción: {self._bon_descripcion}, Valor: {self._bon_valor}'

    # Getters
    @property
    def bon_codigo(self):
        return self._bon_codigo

    @property
    def bon_descripcion(self):
        return self._bon_descripcion

    @property
    def bon_valor(self):
        return self._bon_valor

    # Setters
    @bon_codigo.setter
    def bon_codigo(self, value):
        self._bon_codigo = value

    @bon_descripcion.setter
    def bon_descripcion(self, value):
        self._bon_descripcion = value

    @bon_valor.setter
    def bon_valor(self, value):
        self._bon_valor = value
