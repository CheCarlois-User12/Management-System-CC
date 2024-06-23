from conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool
from BXN import BXN

class BXNDAO:
    _SELECCIONAR = 'SELECT * FROM BXN WHERE bxnStatus <> "INA" ORDER BY bonCodigo'
    _INSERTAR = '''INSERT INTO BXN(bonCodigo, nomCodigo, bxnValor, bxnDescripcion, bxnStatus) 
                  VALUES(%s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE BXN SET bxnValor=%s, bxnDescripcion=%s, bxnStatus=%s WHERE bonCodigo=%s AND nomCodigo=%s'''
    _ELIMINAR = 'UPDATE BXN SET bxnStatus="INA" WHERE bonCodigo=%s AND nomCodigo=%s'
    _BUSCAR = "SELECT * FROM BXN WHERE bonCodigo=%s AND nomCodigo=%s AND bxnStatus <> 'INA'"

    @classmethod
    def buscar(cls, bon_codigo, nom_codigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (bon_codigo, nom_codigo))
            registro = cursor.fetchone()
            if registro:
                return BXN(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            bxns = []
            for registro in registros:
                bxn = BXN(*registro)
                bxns.append(bxn)
            return bxns

    @staticmethod
    def insertar(bxn, cursor=None):
        query = BXNDAO._INSERTAR
        valores = (bxn.bon_codigo, bxn.nom_codigo, bxn.bxn_valor, bxn.bxn_descripcion, bxn.bxn_status)
        if cursor:
            cursor.execute(query, valores)
        else:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            try:
                cursor.execute(query, valores)
                conexion.commit()
            except Exception as e:
                print(f"Error al insertar la bonificación: {e}")
            finally:
                Conexion.liberarConexion(conexion)

    @classmethod
    def actualizar(cls, bxn):
        with CursorDelPool() as cursor:
            valores = (bxn.bxn_valor, bxn.bxn_descripcion, bxn.bxn_status, bxn.bon_codigo, bxn.nom_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Bonificación actualizada: {bxn}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, bon_codigo, nom_codigo):
        try:
            conexion = Conexion.obtenerConexion()
            with conexion.cursor() as cursor:
                query = "CALL desactivar_nomina(%s)"
                cursor.execute(query, (nom_codigo,))
            conexion.commit()
            log.debug(f'Bonificación eliminada: bon_codigo={bon_codigo}, nom_codigo={nom_codigo}')
        except Exception as e:
            print(f"Error al eliminar la bonificación: {e}")
        finally:
            Conexion.liberarConexion(conexion)
