from typing import Annotated
from pydantic import Field, PositiveFloat

from workout api.contrib.schemas import BaseSchema


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='NOME DO ATLETA', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF DO ATLETA', examples='12312312312', max_length=11)]
    idade: Annotated[int, Field(description='IDADE DO ATLETA', examples='41')]
    peso: Annotated[PositiveFloat, Field(description='PESO DO ATLETA', examples='94.5')]
    altura: Annotated[PositiveFloat, Field(description='ALTURA DO ATLETA', examples='1.70')]
    sexo: Annotated[str, Field(description='SEXO DO ATLETA', examples='M', max_length=1)]