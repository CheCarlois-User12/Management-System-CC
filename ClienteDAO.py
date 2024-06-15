from logger_base import log
from cursor_del_pool import CursorDelPool
from Cliente import Cliente

class ClienteDAO:
    _SELECCIONAR = 'SELECT * FROM clientes ORDER BY CLICODIGO'
    _INSERTAR = '''INSERT INTO clientes(CLICODIGO, CLINOMBRE, CLIIDENTIFICACION, CLIDIRECCION, CLITELEFONO, CLICELULAR, CLIEMAIL, CLITIPO, CLISTATUS) 
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    _ACTUALIZAR = '''UPDATE clientes SET CLINOMBRE=%s, CLIIDENTIFICACION=%s, CLIDIRECCION=%s, CLITELEFONO=%s, CLICELULAR=%s, CLIEMAIL=%s, CLITIPO=%s, CLISTATUS=%s 
                    WHERE CLICODIGO=%s'''
    _ELIMINAR = 'DELETE FROM CLIENTES WHERE CLICODIGO=%s'
    _BUSCAR = "SELECT * FROM CLIENTES WHERE CLICODIGO=%s"

    _SELECCIONAR_CODIGOS = 'SELECT CLICODIGO FROM CLIENTES ORDER BY CLICODIGO'

    @classmethod
    def seleccionar_codigos(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR_CODIGOS)
            registros = cursor.fetchall()
            codigos = [registro[0] for registro in registros]
            return codigos

    @classmethod
    def buscar(cls, clicodigo):
        with CursorDelPool() as cursor:
            cursor.execute(cls._BUSCAR, (clicodigo,))
            registro = cursor.fetchone()
            if registro:
                return Cliente(*registro)
            return None

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(*registro)
                clientes.append(cliente)
            return clientes

    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.cli_codigo, cliente.cli_nombre, cliente.cli_identificacion, cliente.cli_direccion,
                       cliente.cli_telefono, cliente.cli_celular, cliente.cli_email, cliente.cli_tipo, cliente.cli_status)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Cliente insertado: {cliente}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.cli_nombre, cliente.cli_identificacion, cliente.cli_direccion, cliente.cli_telefono,
                       cliente.cli_celular, cliente.cli_email, cliente.cli_tipo, cliente.cli_status, cliente.cli_codigo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Cliente actualizado: {cliente}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, clicodigo):
        with CursorDelPool() as cursor:
            try:
                cursor.execute(cls._ELIMINAR, (clicodigo,))
                log.debug(f"Registro eliminado: {clicodigo}")
                return cursor.rowcount
            except Exception as e:
                log.error(f"Error al eliminar el registro: {e}")
                raise
