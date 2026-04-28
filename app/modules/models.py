from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


# Tablas intermedias N:N
class ProductoCategoria(SQLModel, table=True):
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True)
    categoria_id: Optional[int] = Field(default=None, foreign_key="categoria.id", primary_key=True)


class ProductoIngrediente(SQLModel, table=True):
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True)
    ingrediente_id: Optional[int] = Field(default=None, foreign_key="ingrediente.id", primary_key=True)
    cantidad: str = Field(default="al gusto")


class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: Optional[str] = None

    productos: List["Producto"] = Relationship(back_populates="categorias", link_model=ProductoCategoria)


class Ingrediente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    unidad: str

    productos: List["Producto"] = Relationship(back_populates="ingredientes", link_model=ProductoIngrediente)


class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    descripcion: Optional[str] = None

    categorias: List[Categoria] = Relationship(back_populates="productos", link_model=ProductoCategoria)
    ingredientes: List[Ingrediente] = Relationship(back_populates="productos", link_model=ProductoIngrediente)
