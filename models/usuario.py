from pydantic import BaseModel


class Usuario(BaseModel):
    cedula: str
    nombre_completo: str
    activo: bool
    telefono: str
    rol: str

class UsuarioDb( Usuario ):
    password: str