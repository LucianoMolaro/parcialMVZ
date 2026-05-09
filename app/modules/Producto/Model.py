from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules.Ingrediente.Model import Ingrediente
from app.modules.Categoria.Model import Categoria
from app.modules.models import ProductoCategoria, ProductoIngrediente


class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    descripcion: Optional[str] = None

    categorias: List["Categoria"] = Relationship(back_populates="productos", link_model=ProductoCategoria)
    ingredientes: List["Ingrediente"] = Relationship(back_populates="productos", link_model=ProductoIngrediente)
