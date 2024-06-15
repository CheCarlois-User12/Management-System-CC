class Producto:
    def __init__(self, prod_codigo, prod_descripcion, prod_unidad_medida, prod_saldo_inicial, prod_ingresos, prod_egresos, prod_ajustes, prod_saldo_final, prod_costo_x_unidad, prod_status):
        self.prod_codigo = prod_codigo
        self.prod_descripcion = prod_descripcion
        self.prod_unidad_medida = prod_unidad_medida
        self.prod_saldo_inicial = prod_saldo_inicial
        self.prod_ingresos = prod_ingresos
        self.prod_egresos = prod_egresos
        self.prod_ajustes = prod_ajustes
        self.prod_saldo_final = prod_saldo_final
        self.prod_costo_x_unidad = prod_costo_x_unidad
        self.prod_status = prod_status

    # Getters y Setters
    def get_prod_codigo(self):
        return self.prod_codigo

    def set_prod_codigo(self, prod_codigo):
        self.prod_codigo = prod_codigo

    def get_prod_descripcion(self):
        return self.prod_descripcion

    def set_prod_descripcion(self, prod_descripcion):
        self.prod_descripcion = prod_descripcion

    def get_prod_unidad_medida(self):
        return self.prod_unidad_medida

    def set_prod_unidad_medida(self, prod_unidad_medida):
        self.prod_unidad_medida = prod_unidad_medida

    def get_prod_saldo_inicial(self):
        return self.prod_saldo_inicial

    def set_prod_saldo_inicial(self, prod_saldo_inicial):
        self.prod_saldo_inicial = prod_saldo_inicial

    def get_prod_ingresos(self):
        return self.prod_ingresos

    def set_prod_ingresos(self, prod_ingresos):
        self.prod_ingresos = prod_ingresos

    def get_prod_egresos(self):
        return self.prod_egresos

    def set_prod_egresos(self, prod_egresos):
        self.prod_egresos = prod_egresos

    def get_prod_ajustes(self):
        return self.prod_ajustes

    def set_prod_ajustes(self, prod_ajustes):
        self.prod_ajustes = prod_ajustes

    def get_prod_saldo_final(self):
        return self.prod_saldo_final

    def set_prod_saldo_final(self, prod_saldo_final):
        self.prod_saldo_final = prod_saldo_final

    def get_prod_costo_x_unidad(self):
        return self.prod_costo_x_unidad

    def set_prod_costo_x_unidad(self, prod_costo_x_unidad):
        self.prod_costo_x_unidad = prod_costo_x_unidad

    def get_prod_status(self):
        return self.prod_status

    def set_prod_status(self, prod_status):
        self.prod_status = prod_status
