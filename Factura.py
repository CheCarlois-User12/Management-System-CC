class Factura:
    def __init__(self, facCodigo, cliCodigo, facFecha, facHora, facSubtotal, facDescuento, facIva, facTotal, facFormaPago, facStatus):
        self.facCodigo = facCodigo
        self.cliCodigo = cliCodigo
        self.facFecha = facFecha
        self.facHora = facHora
        self.facSubtotal = facSubtotal
        self.facDescuento = facDescuento
        self.facIva = facIva
        self.facTotal = facTotal
        self.facFormaPago = facFormaPago
        self.facStatus = facStatus

    # Getters
    def get_facCodigo(self):
        return self.facCodigo

    def get_cliCodigo(self):
        return self.cliCodigo

    def get_facFecha(self):
        return self.facFecha

    def get_facHora(self):
        return self.facHora

    def get_facSubtotal(self):
        return self.facSubtotal

    def get_facDescuento(self):
        return self.facDescuento

    def get_facIva(self):
        return self.facIva

    def get_facTotal(self):
        return self.facTotal

    def get_facFormaPago(self):
        return self.facFormaPago

    def get_facStatus(self):
        return self.facStatus

    # Setters
    def set_facCodigo(self, facCodigo):
        self.facCodigo = facCodigo

    def set_cliCodigo(self, cliCodigo):
        self.cliCodigo = cliCodigo

    def set_facFecha(self, facFecha):
        self.facFecha = facFecha

    def set_facHora(self, facHora):
        self.facHora = facHora

    def set_facSubtotal(self, facSubtotal):
        self.facSubtotal = facSubtotal

    def set_facDescuento(self, facDescuento):
        self.facDescuento = facDescuento

    def set_facIva(self, facIva):
        self.facIva = facIva

    def set_facTotal(self, facTotal):
        self.facTotal = facTotal

    def set_facFormaPago(self, facFormaPago):
        self.facFormaPago = facFormaPago

    def set_facStatus(self, facStatus):
        self.facStatus = facStatus
