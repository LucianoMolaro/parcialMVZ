from typing import Optional, List
from sqlmodel import SQLModel
from app.modules.Categoria.Schema import CategoriaRead
from app.modules.Ingrediente.IngredienteSchema import IngredienteRead


class ProductoCreate(SQLModel):
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    categoria_ids: List[int] = []
    ingrediente_ids: List[int] = []


class ProductoRead(SQLModel):
    id: int
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    categorias: List[CategoriaRead] = []
    ingredientes: List[IngredienteRead] = []
