from fastapi import APIRouter, Depends, HTTPException
from models import Usuarios
from dependencias import pegar_sessao
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"message": "Rota de login"}


@auth_router.post("/criar_conta")
async def criar_conta(email : str , senha : str, nome : str, session = Depends(pegar_sessao)):

    usuario = session.query(Usuarios).filter(Usuarios.email==email).first()
    if usuario:
        #ja existe esse usuario
        return HTTPException(status_code=400, datail="email de usuario ja cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuarios(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"messagem": "usuario cadastrado com sucesso"}