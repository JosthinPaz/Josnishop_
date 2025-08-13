from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import SessionLocal
from dtos.inventario_dto import InventarioCreate, InventarioOut, InventarioUpdate
from models.inventario import Inventario

router = APIRouter(prefix="/inventarios", tags=["inventarios"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=InventarioOut)
def crear_inventario(inventario: InventarioCreate, db: Session = Depends(get_db)):
    db_inventario = Inventario(**inventario.dict())
    db.add(db_inventario)
    db.commit()
    db.refresh(db_inventario)
    return db_inventario


@router.get("/", response_model=list[InventarioOut])
def listar_inventarios(db: Session = Depends(get_db)):
    return db.query(Inventario).all()


@router.get("/{inventario_id}", response_model=InventarioOut)
def obtener_inventario(inventario_id: int, db: Session = Depends(get_db)):
    inventario = db.get(Inventario, inventario_id)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inventario


@router.put("/{inventario_id}", response_model=InventarioOut)
def actualizar_inventario(
    inventario_id: int, datos: InventarioUpdate, db: Session = Depends(get_db)
):
    inventario = db.get(Inventario, inventario_id)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(inventario, key, value)
    db.commit()
    db.refresh(inventario)
    return inventario


@router.delete("/{inventario_id}")
def eliminar_inventario(inventario_id: int, db: Session = Depends(get_db)):
    inventario = db.get(Inventario, inventario_id)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    db.delete(inventario)
    db.commit()
    return {"ok": True}
