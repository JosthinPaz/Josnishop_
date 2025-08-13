from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship

from db import Base


class Inventario(Base):
    __tablename__ = "inventarios"
    id_inventario = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad_actual = Column(Integer)
    fecha_actualizacion = Column(DateTime)

    producto = relationship("Producto")
