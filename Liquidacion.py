# Liquidacion.py

class Liquidacion:
    def __init__(self, liq_codigo, emp_codigo, liq_fecha_inicial, liq_fecha_final, liq_motivo, liq_region,
                 liq_mensual_d_tercera, liq_mensual_d_cuarta, liq_vacaciones, liq_status):
        self.liq_codigo = liq_codigo
        self.emp_codigo = emp_codigo
        self.liq_fecha_inicial = liq_fecha_inicial
        self.liq_fecha_final = liq_fecha_final
        self.liq_motivo = liq_motivo
        self.liq_region = liq_region
        self.liq_mensual_d_tercera = liq_mensual_d_tercera
        self.liq_mensual_d_cuarta = liq_mensual_d_cuarta
        self.liq_vacaciones = liq_vacaciones
        self.liq_status = liq_status

    # Métodos getter y setter si es necesario
    @property
    def liq_fecha_inicial(self):
        return self._liq_fecha_inicial

    @liq_fecha_inicial.setter
    def liq_fecha_inicial(self, value):
        self._liq_fecha_inicial = value

    # Repite para otros atributos si es necesario
