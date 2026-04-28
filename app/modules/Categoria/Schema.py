from typing import Optional
from sqlmodel import SQLModel


class CategoriaCreate(SQLModel):
    nombre: str
    descripcion: Optional[str] = None


class CategoriaRead(SQLModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
