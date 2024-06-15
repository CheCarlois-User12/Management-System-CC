class Cliente:
    def __init__(self, cli_codigo, cli_nombre, cli_identificacion, cli_direccion, cli_telefono, cli_celular, cli_email, cli_tipo, cli_status):
        self._cli_codigo = cli_codigo
        self._cli_nombre = cli_nombre
        self._cli_identificacion = cli_identificacion
        self._cli_direccion = cli_direccion
        self._cli_telefono = cli_telefono
        self._cli_celular = cli_celular
        self._cli_email = cli_email
        self._cli_tipo = cli_tipo
        self._cli_status = cli_status

    # Getters
    @property
    def cli_codigo(self):
        return self._cli_codigo

    @property
    def cli_nombre(self):
        return self._cli_nombre

    @property
    def cli_identificacion(self):
        return self._cli_identificacion

    @property
    def cli_direccion(self):
        return self._cli_direccion

    @property
    def cli_telefono(self):
        return self._cli_telefono

    @property
    def cli_celular(self):
        return self._cli_celular

    @property
    def cli_email(self):
        return self._cli_email

    @property
    def cli_tipo(self):
        return self._cli_tipo

    @property
    def cli_status(self):
        return self._cli_status

    # Setters
    @cli_codigo.setter
    def cli_codigo(self, value):
        self._cli_codigo = value

    @cli_nombre.setter
    def cli_nombre(self, value):
        self._cli_nombre = value

    @cli_identificacion.setter
    def cli_identificacion(self, value):
        self._cli_identificacion = value

    @cli_direccion.setter
    def cli_direccion(self, value):
        self._cli_direccion = value

    @cli_telefono.setter
    def cli_telefono(self, value):
        self._cli_telefono = value

    @cli_celular.setter
    def cli_celular(self, value):
        self._cli_celular = value

    @cli_email.setter
    def cli_email(self, value):
        self._cli_email = value

    @cli_tipo.setter
    def cli_tipo(self, value):
        self._cli_tipo = value

    @cli_status.setter
    def cli_status(self, value):
        self._cli_status = value
