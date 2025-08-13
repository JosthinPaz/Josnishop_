from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import SessionLocal
from dtos.notificacion_dto import (
    NotificacionCreate,
    NotificacionOut,
    NotificacionUpdate,
)
from models.notificaciones import Notificacion

router = APIRouter(prefix="/notificaciones", tags=["notificaciones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=NotificacionOut)
def crear_notificacion(notificacion: NotificacionCreate, db: Session = Depends(get_db)):
    db_notificacion = Notificacion(**notificacion.dict())
    db.add(db_notificacion)
    db.commit()
    db.refresh(db_notificacion)
    return db_notificacion


@router.get("/", response_model=list[NotificacionOut])
def listar_notificaciones(db: Session = Depends(get_db)):
    return db.query(Notificacion).all()


@router.get("/{notificacion_id}", response_model=NotificacionOut)
def obtener_notificacion(notificacion_id: int, db: Session = Depends(get_db)):
    notificacion = db.get(Notificacion, notificacion_id)
    if not notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return notificacion


@router.put("/{notificacion_id}", response_model=NotificacionOut)
def actualizar_notificacion(
    notificacion_id: int, datos: NotificacionUpdate, db: Session = Depends(get_db)
):
    notificacion = db.get(Notificacion, notificacion_id)
    if not notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(notificacion, key, value)
    db.commit()
    db.refresh(notificacion)
    return notificacion


@router.delete("/{notificacion_id}")
def eliminar_notificacion(notificacion_id: int, db: Session = Depends(get_db)):
    notificacion = db.get(Notificacion, notificacion_id)
    if not notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    db.delete(notificacion)
    db.commit()
    return {"ok": True}
