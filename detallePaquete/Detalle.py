class Detalle:
    def __init__(self, empcodigo=None, detcodigo=None, detempnombre1=None, detempapellido1=None,
                 detempbanco=None, detempcuenta=None, detempstatus=None, detempsueldo=None):
        self._empcodigo = empcodigo
        self._detcodigo = detcodigo
        self._detempnombre1 = detempnombre1
        self._detempapellido1 = detempapellido1
        self._detempbanco = detempbanco
        self._detempcuenta = detempcuenta
        self._detempstatus = detempstatus
        self._detempsueldo = detempsueldo

    def __str__(self):
        return f'''
            EMP-CODIGO: {self._empcodigo}, DET-CODIGO: {self._detcodigo},
            NOMBRE: {self._detempnombre1}, APELLIDO: {self._detempapellido1},
            BANCO: {self._detempbanco}, CUENTA: {self._detempcuenta},
            STATUS: {self._detempstatus}, SUELDO: {self._detempsueldo}
        '''

    @property
    def empcodigo(self):
        return self._empcodigo

    @empcodigo.setter
    def empcodigo(self, empcodigo):
        self._empcodigo = empcodigo

    @property
    def detcodigo(self):
        return self._detcodigo

    @detcodigo.setter
    def detcodigo(self, detcodigo):
        self._detcodigo = detcodigo

    @property
    def detempnombre1(self):
        return self._detempnombre1

    @detempnombre1.setter
    def detempnombre1(self, detempnombre1):
        self._detempnombre1 = detempnombre1

    @property
    def detempapellido1(self):
        return self._detempapellido1

    @detempapellido1.setter
    def detempapellido1(self, detempapellido1):
        self._detempapellido1 = detempapellido1

    @property
    def detempbanco(self):
        return self._detempbanco

    @detempbanco.setter
    def detempbanco(self, detempbanco):
        self._detempbanco = detempbanco

    @property
    def detempcuenta(self):
        return self._detempcuenta

    @detempcuenta.setter
    def detempcuenta(self, detempcuenta):
        self._detempcuenta = detempcuenta

    @property
    def detempstatus(self):
        return self._detempstatus

    @detempstatus.setter
    def detempstatus(self, detempstatus):
        self._detempstatus = detempstatus

    @property
    def detempsueldo(self):
        return self._detempsueldo

    @detempsueldo.setter
    def detempsueldo(self, detempsueldo):
        self._detempsueldo = detempsueldo
