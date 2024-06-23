class DXN:
    def __init__(self, des_codigo=None, nom_codigo=None, dxn_valor=None, dxn_descripcion=None):
        self._des_codigo = des_codigo
        self._nom_codigo = nom_codigo
        self._dxn_valor = dxn_valor
        self._dxn_descripcion = dxn_descripcion

    def __str__(self):
        return f'Descuento: {self._des_codigo}, Nómina: {self._nom_codigo}, Valor: {self._dxn_valor}, Descripción: {self._dxn_descripcion}'

    # Getters
    @property
    def des_codigo(self):
        return self._des_codigo

    @property
    def nom_codigo(self):
        return self._nom_codigo

    @property
    def dxn_valor(self):
        return self._dxn_valor

    @property
    def dxn_descripcion(self):
        return self._dxn_descripcion

    # Setters
    @des_codigo.setter
    def des_codigo(self, value):
        self._des_codigo = value

    @nom_codigo.setter
    def nom_codigo(self, value):
        self._nom_codigo = value

    @dxn_valor.setter
    def dxn_valor(self, value):
        self._dxn_valor = value

    @dxn_descripcion.setter
    def dxn_descripcion(self, value):
        self._dxn_descripcion = value
