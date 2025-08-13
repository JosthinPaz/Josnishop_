from typing import Optional

from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    contraseña: str
    rol_id: int
    estado: Optional[bool] = True


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(UsuarioBase):
    pass


class UsuarioOut(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True
