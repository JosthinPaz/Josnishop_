from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from db import Base


class Reseña(Base):
    __tablename__ = "reseñas"
    id_reseña = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cliente_id = Column(Integer, ForeignKey("usuarios.id_usuario"))
    calificación = Column(Integer)
    comentario = Column(Text)
    fecha = Column(DateTime)

    producto = relationship("Producto")
    cliente = relationship("Usuario")
