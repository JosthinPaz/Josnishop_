from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InventarioBase(BaseModel):
    producto_id: int
    cantidad_actual: int
    fecha_actualizacion: Optional[datetime] = None


class InventarioCreate(InventarioBase):
    pass


class InventarioUpdate(InventarioBase):
    pass


class InventarioOut(InventarioBase):
    id_inventario: int

    class Config:
        from_attributes = True
