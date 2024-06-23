class BXN:
    def __init__(self, bon_codigo=None, nom_codigo=None, bxn_valor=None, bxn_descripcion=None):
        self._bon_codigo = bon_codigo
        self._nom_codigo = nom_codigo
        self._bxn_valor = bxn_valor
        self._bxn_descripcion = bxn_descripcion

    def __str__(self):
        return f'Bonificación: {self._bon_codigo}, Nómina: {self._nom_codigo}, Valor: {self._bxn_valor}, Descripción: {self._bxn_descripcion}'

    # Getters
    @property
    def bon_codigo(self):
        return self._bon_codigo

    @property
    def nom_codigo(self):
        return self._nom_codigo

    @property
    def bxn_valor(self):
        return self._bxn_valor

    @property
    def bxn_descripcion(self):
        return self._bxn_descripcion

    # Setters
    @bon_codigo.setter
    def bon_codigo(self, value):
        self._bon_codigo = value

    @nom_codigo.setter
    def nom_codigo(self, value):
        self._nom_codigo = value

    @bxn_valor.setter
    def bxn_valor(self, value):
        self._bxn_valor = value

    @bxn_descripcion.setter
    def bxn_descripcion(self, value):
        self._bxn_descripcion = value
