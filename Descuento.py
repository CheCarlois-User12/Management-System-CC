# Descuento.py
class Descuento:
    def __init__(self, des_codigo=None, des_descripcion=None, des_valor=None):
        self._des_codigo = des_codigo
        self._des_descripcion = des_descripcion
        self._des_valor = des_valor

    def __str__(self):
        return f'Código: {self._des_codigo}, Descripción: {self._des_descripcion}, Valor: {self._des_valor}'

    # Getters
    @property
    def des_codigo(self):
        return self._des_codigo

    @property
    def des_descripcion(self):
        return self._des_descripcion

    @property
    def des_valor(self):
        return self._des_valor

    # Setters
    @des_codigo.setter
    def des_codigo(self, value):
        self._des_codigo = value

    @des_descripcion.setter
    def des_descripcion(self, value):
        self._des_descripcion = value

    @des_valor.setter
    def des_valor(self, value):
        self._des_valor = value
