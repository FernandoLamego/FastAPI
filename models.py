from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, text
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# cria uma conexão com o banco de dados SQLite
db = create_engine("sqlite:///banco.db")

#  CORREÇÃO 1: Adicionados os parênteses () para executar a função e criar a Base real
Base = declarative_base()

# cria as classes/tabelas do banco

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False, server_default=text("false"))

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
    #  CORREÇÃO 2: O atributo correto do SQLAlchemy é __tablename__ (com dois underlines de cada lado)
    __tablename__ = "pedidos"

    STATUS_PEDIDOS = [
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO")
    ]

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    #  CORREÇÃO 3: O parâmetro correto da biblioteca sqlalchemy_utils é `choices`, no plural
    status = Column("status", ChoiceType(choices=STATUS_PEDIDOS)) 
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE",  preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco


class ItensPedido(Base):
    #  CORREÇÃO 4: Alterado de __table_name__ para __tablename__
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade =  quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido
