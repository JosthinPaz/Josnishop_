from typing import Optional

from pydantic import BaseModel


class ProductoBase(BaseModel):
    nombre: str
    categoria_id: int
    descripcion: Optional[str] = None


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True
