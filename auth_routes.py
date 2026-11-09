from fastapi import APIRouter, Depends, HTTPException
from models import Usuarios
from dependencias import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"message": "Rota de login"}


@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuarios).filter(Usuarios.email==usuario_schema.email).first()
    if usuario:
        #ja existe esse usuario
        return HTTPException(status_code=400, detail="email de usuario ja cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuarios(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message": "usuario cadastrado com sucesso"}