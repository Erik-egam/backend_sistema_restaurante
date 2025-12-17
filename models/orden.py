from pydantic import BaseModel
from typing import List


class OrdenPlatos(BaseModel):
    id_plato: int
    cantidad: int

class Orden(BaseModel):
    id_orden: int
    id_sesion: int
    pagado: bool
    preparado: bool
    platos: List[OrdenPlatos]
    