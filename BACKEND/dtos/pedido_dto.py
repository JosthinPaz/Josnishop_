from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PedidoBase(BaseModel):
    cliente_id: int
    fecha_pedido: Optional[datetime] = None
    estado: Optional[str] = None
    total: Optional[float] = None


class PedidoCreate(PedidoBase):
    pass


class PedidoUpdate(PedidoBase):
    pass


class PedidoOut(PedidoBase):
    id_pedido: int

    class Config:
        from_attributes = True
