from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.modules import ProductoCategoria
from app.modules.Producto.Model import Producto
from app.modules.Categoria.Model import Categoria


class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: Optional[str] = None

    productos: List["Producto"] = Relationship(back_populates="categorias", link_model=ProductoCategoria)
    parent_id: Optional[int] = Field(default=None, foreign_key="categoria_id")
    padre: Optional["Categoria"] = Relationship(back_populates="subcategorias", sa_relationship_kwargs={"remote_side": "categoria_id"},)
    subcategorias: List["Categoria"] = Relationship(back_populates="padre")

