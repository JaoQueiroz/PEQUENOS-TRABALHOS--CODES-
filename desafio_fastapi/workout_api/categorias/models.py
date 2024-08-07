from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from workout_api.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(integer, primary_key= True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    