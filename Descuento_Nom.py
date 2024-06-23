
class Descuento_Nom:
    def __init__(self, nom_codigo=None, des_codigo=None, des_descripcion=None, des_valor=None, des_status='ACT'):
        self.nom_codigo = nom_codigo
        self.des_codigo = des_codigo
        self.des_descripcion = des_descripcion
        self.des_valor = des_valor
        self.des_status = des_status

    @property
    def codigo(self):
        return self.des_codigo

    @property
    def descripcion(self):
        return self.des_descripcion

    @property
    def valor(self):
        return self.des_valor

    @property
    def tipo(self):
        return "Descuento"
