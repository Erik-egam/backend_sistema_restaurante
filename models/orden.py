from pydantic import BaseModel
from typing import List, Optional


class OrdenPlatos(BaseModel):
    id_plato: int
    cantidad: int

class Orden(BaseModel):
    id_orden: Optional[int] = None
    platos: List[OrdenPlatos]
    # id_sesion: int
    # pagado: Optional[bool] = None
    # preparado: Optional[bool] = None
    