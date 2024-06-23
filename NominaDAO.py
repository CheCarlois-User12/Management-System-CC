from conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool
from Nomina import Nomina

class NominaDAO:
    _SELECCIONAR = 'SELECT * FROM nominas WHERE NOMSTATUS <> "INA" ORDER BY NOMCODIGO'
    _INSERTAR = '''INSERT INTO nominas(NOMCODIGO, EMPCODIGO, EMPCARGO, NOMNOMBREEMPLEADO, NOMANIO, NOMMES, NOMFECHAINICIAL, NOMFECHAFINAL,
                  NOMTOTALHORAS, NOMSUBTOTAL, NOMTOTALBONIFICACIONES, NOMTOTALDESCUENTOS, NOMTOTAL, NOMSTATUS) 
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE nominas SET EMPCODIGO=%s, EMPCARGO=%s, NOMNOMBREEMPLEADO=%s, NOMANIO=%s, NOMMES=%s, NOMFECHAINICIAL=%s, 
                    NOMFECHAFINAL=%s, NOMTOTALHORAS=%s, NOMSUBTOTAL=%s, NOMTOTALBONIFICACIONES=%s, NOMTOTALDESCUENTOS=%s, NOMTOTAL=%s, 
                    NOMSTATUS=%s WHERE NOMCODIGO=%s'''
    _ELIMINAR = 'UPDATE nominas SET NOMSTATUS="INA" WHERE NOMCODIGO=%s'
    _BUSCAR = "SELECT * FROM nominas WHERE NOMCODIGO=%s AND NOMSTATUS <> 'INA'"
    _BUSCAR_DESCUENTOS = "SELECT * FROM DXN WHERE nomCodigo=%s AND dxnStatus <> 'INA'"
    _BUSCAR_BONIFICACIONES = "SELECT * FROM BXN WHERE nomCodigo=%s AND bxnStatus <> 'INA'"

    @classmethod
    def buscar(cls, nom_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (nom_codigo,))
            registro = cursor.fetchone()
            if registro:
                return Nomina(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            nominas = []
            for registro in registros:
                nomina = Nomina(*registro)
                nominas.append(nomina)
            return nominas

    @staticmethod
    def insertar(nomina, descuentos, bonificaciones):
        try:
            conexion = Conexion.obtenerConexion()
            with conexion.cursor() as cursor:
                log.debug(f"Insertando nómina: {nomina}")
                cursor.execute(NominaDAO._INSERTAR, (
                    nomina.nom_codigo,
                    nomina.emp_codigo,
                    nomina.emp_cargo,
                    nomina.nom_nombre_empleado,
                    nomina.nom_anio,
                    nomina.nom_mes,
                    nomina.nom_fecha_inicial,
                    nomina.nom_fecha_final,
                    nomina.nom_total_horas,
                    nomina.nom_subtotal,
                    nomina.nom_total_bonificaciones,
                    nomina.nom_total_descuentos,
                    nomina.nom_total,
                    nomina.nom_status
                ))

                # Inserción en BXN y DXN
                log.debug(f"Insertando bonificaciones: {bonificaciones}")
                for bonificacion in bonificaciones:
                    query_bxn = "INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(query_bxn, (
                        bonificacion.bon_codigo, nomina.nom_codigo, bonificacion.bon_valor,
                        bonificacion.bon_descripcion, 'ACT'))

                log.debug(f"Insertando descuentos: {descuentos}")
                for descuento in descuentos:
                    query_dxn = "INSERT INTO DXN (desCodigo, nomCodigo, dxnValor, dxnDescripcion, dxnStatus) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(query_dxn, (
                        descuento.des_codigo, nomina.nom_codigo, descuento.des_valor, descuento.des_descripcion, 'ACT'))

            conexion.commit()
            log.debug(f"Nómina insertada correctamente: {nomina.nom_codigo}")
        except Exception as e:
            log.error(f"Error al insertar la nómina: {e}")
        finally:
            Conexion.liberarConexion(conexion)

    @classmethod
    def actualizar(cls, nomina, descuentos, bonificaciones):
        try:
            conexion = Conexion.obtenerConexion()
            with conexion.cursor() as cursor:
                valores = (nomina.emp_codigo, nomina.emp_cargo, nomina.nom_nombre_empleado, nomina.nom_anio, nomina.nom_mes,
                           nomina.nom_fecha_inicial, nomina.nom_fecha_final, nomina.nom_total_horas, nomina.nom_subtotal,
                           nomina.nom_total_bonificaciones, nomina.nom_total_descuentos, nomina.nom_total, nomina.nom_status,
                           nomina.nom_codigo)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Nomina actualizada: {nomina}")

                # Actualizar la tabla DXN
                cursor.execute("DELETE FROM DXN WHERE nomCodigo = %s", (nomina.nom_codigo,))
                for descuento in descuentos:
                    cursor.execute(
                        "INSERT INTO DXN (desCodigo, nomCodigo, dxnValor, dxnDescripcion, dxnStatus) VALUES (%s, %s, %s, %s, %s)",
                        (descuento.des_codigo, nomina.nom_codigo, descuento.des_valor, descuento.des_descripcion, 'ACT')
                    )
                    log.debug(f"Descuento actualizado en DXN: {descuento}")

                # Actualizar la tabla BXN
                cursor.execute("DELETE FROM BXN WHERE nomCodigo = %s", (nomina.nom_codigo,))
                for bonificacion in bonificaciones:
                    cursor.execute(
                        "INSERT INTO BXN (bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) VALUES (%s, %s, %s, %s, %s)",
                        (bonificacion.bon_codigo, nomina.nom_codigo, bonificacion.bon_valor, bonificacion.bon_descripcion,
                         'ACT')
                    )
                    log.debug(f"Bonificacion actualizada en BXN: {bonificacion}")

                conexion.commit()
                log.debug(f"Nomina actualizada correctamente: {nomina.nom_codigo}")
        except Exception as e:
            log.error(f"Error al actualizar la nómina: {e}")
        finally:
            Conexion.liberarConexion(conexion)

    @classmethod
    def eliminar(cls, nom_codigo):
        try:
            conexion = Conexion.obtenerConexion()
            with conexion.cursor() as cursor:
                query = "CALL desactivar_nomina(%s)"
                cursor.execute(query, (nom_codigo,))
            conexion.commit()
            log.debug(f"Nomina eliminada: nom_codigo={nom_codigo}")
        except Exception as e:
            log.error(f"Error al eliminar la nómina: {e}")
        finally:
            Conexion.liberarConexion(conexion)

    @classmethod
    def buscar_descuentos(cls, nom_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR_DESCUENTOS, (nom_codigo,))
            registros = cursor.fetchall()
            return registros

    @classmethod
    def buscar_bonificaciones(cls, nom_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR_BONIFICACIONES, (nom_codigo,))
            registros = cursor.fetchall()
            return registros

    @classmethod
    def seleccionar_DXN_BXN(cls, nom_codigo):
        try:
            conexion = Conexion.obtenerConexion()
            with conexion.cursor() as cursor:
                query = "CALL obtener_DXN_BXN_activos(%s)"
                cursor.execute(query, (nom_codigo,))
                descuentos = cursor.fetchall()
                cursor.nextset()
                bonificaciones = cursor.fetchall()
                return descuentos, bonificaciones
        except Exception as e:
            log.error(f"Error al obtener DXN y BXN: {e}")
        finally:
            Conexion.liberarConexion(conexion)
