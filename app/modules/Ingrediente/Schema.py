from sqlmodel import SQLModel


class IngredienteCreate(SQLModel):
    nombre: str
    unidad: str


class IngredienteRead(SQLModel):
    id: int
    nombre: str
    unidad: str
