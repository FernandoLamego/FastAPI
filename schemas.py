from pydantic import BaseModel, Field
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str = Field(..., example="johndoe")
    email: str = Field(..., example="")
    senha: str = Field(..., example="123456")
    ativo: Optional[bool] = Field(default=True, example=True)
    admin: Optional[bool] = Field(default=False, example=False)

    class Config:
        from_atributes = True
