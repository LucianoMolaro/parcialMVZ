from sqlmodel import Session
from app.core.UnitOfWork import UnitOfWork
from app.modules.Categoria.Repository import CategoriaRepository


class CategoriaUnitOfWork(UnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.categorias = CategoriaRepository(session)
