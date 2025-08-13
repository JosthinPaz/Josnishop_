from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from db import Base


class Pedido(Base):
    __tablename__ = "pedidos"
    id_pedido = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_pedido = Column(DateTime)
    estado = Column(String(50))
    total = Column(Float)

    cliente = relationship("Usuario")
    detalles = relationship("DetallePedido", back_populates="pedido")
