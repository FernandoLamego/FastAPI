from fastapi import APIRouter, Depends, HTTPException
from models import Usuarios
from dependencias import pegar_sessao
from main import bcrypt_context
from schemas import LoginSchema, UsuarioSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(email):
    #JWT
    #identificação do usuario, tempo de expiração, assinatura.
    token = f"ldflaf{email}"
    return token

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuarios).filter(Usuarios.email==email).first()
    if not usuario:
        return False
    else:
        if not bcrypt_context.verify(senha, usuario.senha):
            return False
    return usuario

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

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario nao encontrado ou senha incorreta")
    else:
        access_token = criar_token(usuario.id)
        return {
            "access_token": access_token,
            "token_type": "bearer",
            }