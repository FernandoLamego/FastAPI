from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

#cria uma conexão com o banco de dados SQLite
db = create_engine("sqlite:///banco.db")

#cria a base do bando de dados
Base = declarative_base

#cria as classes/tabelas do banco

class Usuarios(Base):
    __tablename__: "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#Pedido
#ItensPedido

#executa a criação de metadados do seu banco (cria efitivamente o banco de dados)
