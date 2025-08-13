from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import SessionLocal
from dtos.detalle_pedido_dto import (
    DetallePedidoCreate,
    DetallePedidoOut,
    DetallePedidoUpdate,
)
from models.detallepedido import DetallePedido

router = APIRouter(prefix="/detalles_pedido", tags=["detalles_pedido"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DetallePedidoOut)
def crear_detalle_pedido(detalle: DetallePedidoCreate, db: Session = Depends(get_db)):
    db_detalle = DetallePedido(**detalle.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle


@router.get("/", response_model=list[DetallePedidoOut])
def listar_detalles_pedido(db: Session = Depends(get_db)):
    return db.query(DetallePedido).all()


@router.get("/{detalle_id}", response_model=DetallePedidoOut)
def obtener_detalle_pedido(detalle_id: int, db: Session = Depends(get_db)):
    detalle = db.get(DetallePedido, detalle_id)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de pedido no encontrado")
    return detalle


@router.put("/{detalle_id}", response_model=DetallePedidoOut)
def actualizar_detalle_pedido(
    detalle_id: int, datos: DetallePedidoUpdate, db: Session = Depends(get_db)
):
    detalle = db.get(DetallePedido, detalle_id)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de pedido no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(detalle, key, value)
    db.commit()
    db.refresh(detalle)
    return detalle


@router.delete("/{detalle_id}")
def eliminar_detalle_pedido(detalle_id: int, db: Session = Depends(get_db)):
    detalle = db.get(DetallePedido, detalle_id)
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de pedido no encontrado")
    db.delete(detalle)
    db.commit()
    return {"ok": True}
