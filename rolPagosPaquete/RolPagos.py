class RolPagos:
    def __init__(self, rolcodigo=None, bonxdescodigo=None, detcodigo=None, roltotalbeneficios=None, roltotaldescuentos=None,
                 rolsubtotal=None, roltotalpagar=None):
        self._rolcodigo = rolcodigo
        self._bonxdescodigo = bonxdescodigo
        self._detcodigo = detcodigo
        self._roltotalbeneficios = roltotalbeneficios
        self._roltotaldescuentos = roltotaldescuentos
        self._rolsubtotal = rolsubtotal
        self._roltotalpagar = roltotalpagar

    def __str__(self):
        return f'''
            ROLCODIGO: {self._rolcodigo}, BONXDESCODIGO: {self._bonxdescodigo}, DETCODIGO: {self._detcodigo},
            ROLTOTALBENEFICIOS: {self._roltotalbeneficios}, ROLTOTALDESCUENTOS: {self._roltotaldescuentos},
            ROLSUBTOTAL: {self._rolsubtotal}, ROLTOTALPAGAR: {self._roltotalpagar}
        '''

    @property
    def rolcodigo(self):
        return self._rolcodigo

    @rolcodigo.setter
    def rolcodigo(self, rolcodigo):
        self._rolcodigo = rolcodigo

    @property
    def bonxdescodigo(self):
        return self._bonxdescodigo

    @bonxdescodigo.setter
    def bonxdescodigo(self, bonxdescodigo):
        self._bonxdescodigo = bonxdescodigo

    @property
    def detcodigo(self):
        return self._detcodigo

    @detcodigo.setter
    def detcodigo(self, detcodigo):
        self._detcodigo = detcodigo

    @property
    def roltotalbeneficios(self):
        return self._roltotalbeneficios

    @roltotalbeneficios.setter
    def roltotalbeneficios(self, roltotalbeneficios):
        self._roltotalbeneficios = roltotalbeneficios

    @property
    def roltotaldescuentos(self):
        return self._roltotaldescuentos

    @roltotaldescuentos.setter
    def roltotaldescuentos(self, roltotaldescuentos):
        self._roltotaldescuentos = roltotaldescuentos

    @property
    def rolsubtotal(self):
        return self._rolsubtotal

    @rolsubtotal.setter
    def rolsubtotal(self, rolsubtotal):
        self._rolsubtotal = rolsubtotal

    @property
    def roltotalpagar(self):
        return self._roltotalpagar

    @roltotalpagar.setter
    def roltotalpagar(self, roltotalpagar):
        self._roltotalpagar = roltotalpagar
