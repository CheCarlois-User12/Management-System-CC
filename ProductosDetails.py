class ProductosDetails:
    def __init__(self, prodCodigo, prodDescipcion, prodUnidadMedida, prodCostoxUnidad, prodxdetCantidad, prodxdetDescuento, prodxdetIVA):
        self.prodCodigo = prodCodigo
        self.prodDescipcion = prodDescipcion
        self.prodUnidadMedida = prodUnidadMedida
        self.prodCostoxUnidad = prodCostoxUnidad
        self.prodxdetCantidad = prodxdetCantidad
        self.prodxdetDescuento = prodxdetDescuento
        self.prodxdetIVA = prodxdetIVA

        # Cálculos
        self.prodxdetSubtotal = prodCostoxUnidad * prodxdetCantidad
        self.prodxdetDescuentoSubtotal = self.prodxdetSubtotal - (self.prodxdetSubtotal * (prodxdetDescuento / 100))
        self.prodxdetIVASubtotal = self.prodxdetDescuentoSubtotal + (self.prodxdetDescuentoSubtotal * (prodxdetIVA / 100))

    # Getters
    def get_prodCodigo(self):
        return self.prodCodigo

    def get_prodDescipcion(self):
        return self.prodDescipcion

    def get_prodUnidadMedida(self):
        return self.prodUnidadMedida

    def get_prodCostoxUnidad(self):
        return self.prodCostoxUnidad

    def get_prodxdetCantidad(self):
        return self.prodxdetCantidad

    def get_prodxdetDescuento(self):
        return self.prodxdetDescuento

    def get_prodxdetIVA(self):
        return self.prodxdetIVA

    def get_prodxdetSubtotal(self):
        return self.prodxdetSubtotal

    def get_prodxdetDescuentoSubtotal(self):
        return self.prodxdetDescuentoSubtotal

    def get_prodxdetIVASubtotal(self):
        return self.prodxdetIVASubtotal

    # Setters
    def set_prodCodigo(self, prodCodigo):
        self.prodCodigo = prodCodigo

    def set_prodDescipcion(self, prodDescipcion):
        self.prodDescipcion = prodDescipcion

    def set_prodUnidadMedida(self, prodUnidadMedida):
        self.prodUnidadMedida = prodUnidadMedida

    def set_prodCostoxUnidad(self, prodCostoxUnidad):
        self.prodCostoxUnidad = prodCostoxUnidad
        self.calculate_totals()

    def set_prodxdetCantidad(self, prodxdetCantidad):
        self.prodxdetCantidad = prodxdetCantidad
        self.calculate_totals()

    def set_prodxdetDescuento(self, prodxdetDescuento):
        self.prodxdetDescuento = prodxdetDescuento
        self.calculate_totals()

    def set_prodxdetIVA(self, prodxdetIVA):
        self.prodxdetIVA = prodxdetIVA
        self.calculate_totals()

    def calculate_totals(self):
        self.prodxdetSubtotal = self.prodCostoxUnidad * self.prodxdetCantidad
        self.prodxdetDescuentoSubtotal = self.prodxdetSubtotal - (self.prodxdetSubtotal * (self.prodxdetDescuento / 100))
        self.prodxdetIVASubtotal = self.prodxdetDescuentoSubtotal + (self.prodxdetDescuentoSubtotal * (self.prodxdetIVA / 100))
