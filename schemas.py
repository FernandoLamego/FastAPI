from pydantic import BaseModel, Field
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_atributes = True

class PedidoSchema(BaseModel):
    usuario: int

    class Config:
        from_atributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_atributes = True