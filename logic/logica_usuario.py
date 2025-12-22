from config.dbconfig import get_conexion
from mysql.connector import Error
from fastapi import HTTPException, status
from models.usuario import Usuario, UsuarioDb


class LogicaUsuario:
    def buscar_usuario_db( cedula: str ):
        cnx = get_conexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(
                """SELECT * FROM usuarios
                JOIN roles ON usuarios.id_rol=roles.id_rol
                WHERE cedula=%s;""",
                (cedula,)
            )
            usuario = cursor.fetchone()
            if usuario == None:
                return

            return UsuarioDb(
                cedula=usuario[1],
                nombre_completo=usuario[2],
                activo=usuario[3],
                telefono=usuario[4],
                password=usuario[6],
                rol=usuario[-1]
            )

        except Error as e:
            raise HTTPException(
                detail=f"{e}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        finally:
            cursor.close()
            cnx.close()
            
            
    def buscar_usuario(cedula: str):
        cnx = get_conexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(
                """SELECT * FROM usuarios
                JOIN roles ON usuarios.id_rol=roles.id_rol
                WHERE cedula=%s;""",
                (cedula,)
            )
            usuario = cursor.fetchone()
            if usuario == None:
                return

            return Usuario(
                cedula=usuario[1],
                nombre_completo=usuario[2],
                activo=usuario[3],
                telefono=usuario[4],
                rol=usuario[-1]
            )

        except Error as e:
            raise HTTPException(
                detail=f"{e}",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        finally:
            cursor.close()
            cnx.close()