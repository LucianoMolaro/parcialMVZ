from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules import ProductoIngrediente
from app.modules.Producto.Model import Producto


class Ingrediente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    unidad: str

    productos: List["Producto"] = Relationship(back_populates="ingredientes", link_model=ProductoIngrediente)

