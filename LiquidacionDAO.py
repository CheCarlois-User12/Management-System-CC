from logger_base import log
from cursor_del_pool import CursorDelPool
from Liquidacion import Liquidacion

class LiquidacionDAO:
    _SELECCIONAR = 'SELECT * FROM LIQUIDACIONES ORDER BY liqCodigo'
    _INSERTAR = '''INSERT INTO LIQUIDACIONES (liqCodigo, empCodigo, liqFechaInicial, liqFechaFinal, liqMotivo, liqRegion, liqMensualDTercera, liqMensualDCuarta, liqVacaciones, liqStatus)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'ACT')'''
    _ACTUALIZAR = '''UPDATE LIQUIDACIONES SET empCodigo=%s, liqFechaInicial=%s, liqFechaFinal=%s, liqMotivo=%s, liqRegion=%s, liqMensualDTercera=%s, liqMensualDCuarta=%s, liqVacaciones=%s, liqStatus=%s
                     WHERE liqCodigo=%s'''
    _ELIMINAR = 'DELETE FROM LIQUIDACIONES WHERE liqCodigo=%s'
    _BUSCAR = 'SELECT * FROM LIQUIDACIONES WHERE liqCodigo=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            liquidaciones = []
            for registro in registros:
                liquidacion = Liquidacion(*registro)
                liquidaciones.append(liquidacion)
            return liquidaciones

    @classmethod
    def buscar(cls, liqCodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (liqCodigo,))
            registro = cursor.fetchone()
            if registro:
                return Liquidacion(*registro)
            return None

    @classmethod
    def insertar(cls, liquidacion):
        with CursorDelPool() as cursor:
            liqCodigo = cls.generar_nuevo_codigo()
            valores = (liqCodigo, liquidacion.emp_codigo, liquidacion.liq_fecha_inicial, liquidacion.liq_fecha_final, liquidacion.liq_motivo,
                       liquidacion.liq_region, liquidacion.liq_mensual_d_tercera, liquidacion.liq_mensual_d_cuarta, liquidacion.liq_vacaciones)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Liquidación insertada: {liquidacion}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, liquidacion):
        with CursorDelPool() as cursor:
            valores = (liquidacion.emp_codigo, liquidacion.liq_fecha_inicial, liquidacion.liq_fecha_final, liquidacion.liq_motivo,
                       liquidacion.liq_region, liquidacion.liq_mensual_d_tercera, liquidacion.liq_mensual_d_cuarta, liquidacion.liq_vacaciones, liquidacion.liq_status, liquidacion.liq_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Liquidación actualizada: {liquidacion}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, liqCodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (liqCodigo,))
            log.debug(f'Liquidación eliminada: {liqCodigo}')
            return cursor.rowcount

    @classmethod
    def generar_nuevo_codigo(cls):
        with CursorDelPool() as cursor:
            cursor.execute("SELECT MAX(CAST(SUBSTRING(liqCodigo, 5) AS UNSIGNED)) FROM LIQUIDACIONES")
            max_codigo = cursor.fetchone()[0]
            if max_codigo:
                return f"LIQ-{max_codigo + 1:03d}"
            else:
                return "LIQ-001"
