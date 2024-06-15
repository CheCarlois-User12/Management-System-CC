class Descuento:
    def __init__(self, des_codigo, des_descripcion, des_valor):
        self.des_codigo = des_codigo
        self.des_descripcion = des_descripcion
        self.des_valor = des_valor

    def __str__(self):
        return f'Descuento({self.des_codigo}, {self.des_descripcion}, {self.des_valor})'
