from logger_base import log
from cursor_del_pool import CursorDelPool
from Liquidacion import Liquidacion

class LiquidacionCalculoDAO:
    @classmethod
    def calcular_liquidacion(cls, liquidacion):
        with CursorDelPool() as cursor:
            # Obtener el sueldo del empleado
            cursor.execute("SELECT empSueldo FROM EMPLEADOS WHERE empCodigo=%s", (liquidacion.emp_codigo,))
            empSueldo = cursor.fetchone()[0]

            # Calcular subtotal y total horas trabajadas
            nomTotalHoras = (liquidacion.liq_fecha_final - liquidacion.liq_fecha_inicial).days * 8
            nomSubTotal = (empSueldo / 160) * nomTotalHoras

            # Calcular el año y el mes de la nómina
            nomAnio = liquidacion.liq_fecha_inicial.year
            nomMes = f"{liquidacion.liq_fecha_inicial.month:02d}"

            # Generar nuevo código de nómina
            cursor.execute("SELECT CONCAT('NOM-', LPAD(IFNULL(MAX(CAST(SUBSTRING(nomCodigo, 5) AS UNSIGNED)), 0) + 1, 3, '0')) FROM NOMINAS")
            nomCodigo = cursor.fetchone()[0]

            # Insertar la nueva nómina
            cursor.execute('''
                INSERT INTO NOMINAS (nomCodigo, empCodigo, empCargo, nomNombreEmpleado, nomAnio, nomMes, nomFechaInicial, nomFechaFinal, nomTotalHoras, nomSubTotal, nomTotalBonificaciones, nomTotalDescuentos, nomTotal, nomStatus)
                SELECT %s, e.empCodigo, e.empCargo, CONCAT(e.empNombre1, ' ', e.empApellido1), %s, %s, %s, %s, %s, %s, 0, 0, %s, 'ACT'
                FROM EMPLEADOS e WHERE e.empCodigo = %s
            ''', (nomCodigo, nomAnio, nomMes, liquidacion.liq_fecha_inicial, liquidacion.liq_fecha_final, nomTotalHoras, nomSubTotal, nomSubTotal, liquidacion.emp_codigo))

            # Calcular bonificaciones especiales
            nomTotalBonificaciones = 0

            if liquidacion.liq_mensual_d_tercera == 'No':
                bonificacion = empSueldo / 12
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-001', nomCodigo, bonificacion, 'Valor Decimotercera Remuneración', 'ACT'))
                nomTotalBonificaciones += bonificacion

            if liquidacion.liq_mensual_d_cuarta == 'No':
                bonificacion = empSueldo
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-002', nomCodigo, bonificacion, 'Valor Decimocuarta Remuneración', 'ACT'))
                nomTotalBonificaciones += bonificacion

            bonificacion = (empSueldo / 30) * liquidacion.liq_vacaciones
            cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                           ('BES-003', nomCodigo, bonificacion, 'Valor Vacaciones Último Periodo', 'ACT'))
            nomTotalBonificaciones += bonificacion

            # Insertar otras bonificaciones según el motivo de la liquidación
            if liquidacion.liq_motivo == 'Por despido Intempestivo':
                bonificacion = empSueldo * 3
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-004', nomCodigo, bonificacion, 'Valor Indemnización Despido Intempestivo', 'ACT'))
                nomTotalBonificaciones += bonificacion
            elif liquidacion.liq_motivo == 'Por desahucio':
                bonificacion = (empSueldo * 0.25) * (liquidacion.liq_fecha_final.year - liquidacion.liq_fecha_inicial.year)
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-005', nomCodigo, bonificacion, 'Valor Indemnización Desahucio', 'ACT'))
                nomTotalBonificaciones += bonificacion
            elif liquidacion.liq_motivo == 'Por muerte o incapacidad del empleador o extincion de la persona juridica':
                bonificacion = empSueldo * 12
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-006', nomCodigo, bonificacion, 'Valor Indemnización Mujer Embarazada', 'ACT'))
                nomTotalBonificaciones += bonificacion
            elif liquidacion.liq_motivo == 'Dirigente sindical':
                bonificacion = empSueldo * 12
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-007', nomCodigo, bonificacion, 'Valor Indemnización Dirigente Sindical', 'ACT'))
                nomTotalBonificaciones += bonificacion
            elif liquidacion.liq_motivo == 'Por discapacidad':
                bonificacion = empSueldo * 12
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-008', nomCodigo, bonificacion, 'Valor Indemnización Por Discapacidad', 'ACT'))
                nomTotalBonificaciones += bonificacion
            elif liquidacion.liq_motivo == 'Enfermedad no profesional':
                bonificacion = empSueldo * 12
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-009', nomCodigo, bonificacion, 'Valor Indemnización Enfermedad No Profesional', 'ACT'))
                nomTotalBonificaciones += bonificacion
            elif liquidacion.liq_motivo == 'Terminación antes de plazo':
                bonificacion = empSueldo * (liquidacion.liq_fecha_final.month - liquidacion.liq_fecha_inicial.month)
                cursor.execute('INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)',
                               ('BES-010', nomCodigo, bonificacion, 'Valor Indemnización Terminación Antes de Plazo', 'ACT'))
                nomTotalBonificaciones += bonificacion

            # Actualizar el total de bonificaciones y el total en la tabla NOMINAS
            nomTotal = nomSubTotal + nomTotalBonificaciones
            cursor.execute('UPDATE NOMINAS SET nomTotalBonificaciones=%s, nomTotal=%s WHERE nomCodigo=%s', (nomTotalBonificaciones, nomTotal, nomCodigo))

            # Actualizar el estado del empleado según el motivo de la liquidación
            if liquidacion.liq_motivo in ('Por acuerdo de las partes', 'Por la conclusion de la obra, periodo de labor o servicios objeto del contrato'):
                empStatus = 'DES'
            elif liquidacion.liq_motivo in ('Por muerte o incapacidad del empleador o extincion de la persona juridica', 'Por muerte del trabajador o incapacidad permanente y total para el trabajo.'):
                empStatus = 'MUE'
            elif liquidacion.liq_motivo == 'Por caso fortuito o fuerza mayor que imposibiliten el trabajo, como incendio, terremoto':
                empStatus = 'FUE'
            elif liquidacion.liq_motivo in ('Por voluntad del empleador previo visto bueno.', 'Por voluntad del trabajador previo visto bueno'):
                empStatus = 'VOL'
            elif liquidacion.liq_motivo == 'Por desahucio':
                empStatus = 'HUC'
            elif liquidacion.liq_motivo == 'Por despido Intempestivo':
                empStatus = 'INT'
            cursor.execute('UPDATE EMPLEADOS SET empStatus=%s WHERE empCodigo=%s', (empStatus, liquidacion.emp_codigo))
