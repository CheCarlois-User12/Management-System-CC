class Bonificacion:
    def __init__(self, bon_codigo, bon_descripcion, bon_valor):
        self.bon_codigo = bon_codigo
        self.bon_descripcion = bon_descripcion
        self.bon_valor = bon_valor

    def __str__(self):
        return f'Bonificacion({self.bon_codigo}, {self.bon_descripcion}, {self.bon_valor})'
