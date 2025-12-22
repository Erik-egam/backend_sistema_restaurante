from pydantic import BaseModel

class Plato(BaseModel):
    id_plato: int
    nombre:str
    descripcion: str
    image: str
    precio: int
    