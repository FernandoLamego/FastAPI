from dependencias import pegar_sessao
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return {"message": "Rota de pedidos"}

@order_router.post("/pedidos")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    session.refresh(novo_pedido)
    return {"message": f"Pedido criado com sucesso, pedido: {novo_pedido.id}"}