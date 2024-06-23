from datetime import datetime

from EmpleadoDAO import EmpleadoDAO


class LiquidacionesCons:
    @staticmethod
    def calcular_decimotercera(sueldo_anual):
        """Calcula el valor de la decimotercera remuneración"""
        return sueldo_anual / 12

    @staticmethod
    def calcular_decimocuarta(sueldo_basico_unificado):
        """Calcula el valor de la decimocuarta remuneración"""
        return sueldo_basico_unificado

    @staticmethod
    def calcular_vacaciones(sueldo_mensual, dias_vacaciones_no_gozadas):
        """Calcula el valor de las vacaciones no gozadas"""
        return (sueldo_mensual / 30) * dias_vacaciones_no_gozadas

    @staticmethod
    def calcular_despido_intempestivo(sueldo_mensual):
        """Calcula el valor de la indemnización por despido intempestivo"""
        return sueldo_mensual * 3

    @staticmethod
    def calcular_desahucio(sueldo_mensual, años_servicio):
        """Calcula el valor de la indemnización por desahucio"""
        return (sueldo_mensual * 0.25) * años_servicio

    @staticmethod
    def calcular_indemnizacion(sueldo_mensual, meses_restantes):
        """Calcula el valor de la indemnización por terminación antes de plazo"""
        return sueldo_mensual * meses_restantes

    @staticmethod
    def obtener_sueldo_anual(emp_codigo):
        """Obtiene el sueldo anual del empleado"""
        empleado = EmpleadoDAO.buscar(emp_codigo)
        return float(empleado.emp_sueldo) * 12

    @staticmethod
    def obtener_sueldo_basico_unificado():
        """Obtiene el sueldo básico unificado"""
        # Sueldo básico unificado en Ecuador (actualizar según corresponda)
        return 425.0

    @staticmethod
    def calcular_antiguedad(fecha_inicial, fecha_final):
        """Calcula los años de servicio del empleado"""
        fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d")
        fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
        return (fecha_final - fecha_inicial).days // 365

    @staticmethod
    def calcular_liquidacion(emp_codigo, fecha_inicial, fecha_final, dias_vacaciones, decimotercera, decimocuarta, motivo):
        sueldo_anual = LiquidacionesCons.obtener_sueldo_anual(emp_codigo)
        sueldo_mensual = sueldo_anual / 12
        sueldo_basico_unificado = LiquidacionesCons.obtener_sueldo_basico_unificado()
        años_servicio = LiquidacionesCons.calcular_antiguedad(fecha_inicial, fecha_final)

        total_liquidacion = 0.0

        if decimotercera:
            total_liquidacion += LiquidacionesCons.calcular_decimotercera(sueldo_anual)
        if decimocuarta:
            total_liquidacion += LiquidacionesCons.calcular_decimocuarta(sueldo_basico_unificado)

        total_liquidacion += LiquidacionesCons.calcular_vacaciones(sueldo_mensual, dias_vacaciones)

        if motivo == "Por despido Intempestivo":
            total_liquidacion += LiquidacionesCons.calcular_despido_intempestivo(sueldo_mensual)
        elif motivo == "Por desahucio":
            total_liquidacion += LiquidacionesCons.calcular_desahucio(sueldo_mensual, años_servicio)
        # Añadir más cálculos de indemnización según el motivo

        return total_liquidacion
