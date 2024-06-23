class Bonificacion_Nom:
    def __init__(self, nom_codigo=None, bon_codigo=None, bon_descripcion=None, bon_valor=None, bon_status='ACT'):
        self.nom_codigo = nom_codigo
        self.bon_codigo = bon_codigo
        self.bon_descripcion = bon_descripcion
        self.bon_valor = bon_valor
        self.bon_status = bon_status

    @property
    def codigo(self):
        return self.bon_codigo

    @property
    def descripcion(self):
        return self.bon_descripcion

    @property
    def valor(self):
        return self.bon_valor

    @property
    def tipo(self):
        return "Bonificación"