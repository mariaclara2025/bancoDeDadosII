from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean,ForeignKey
Base = declarative_base()
class Produto(Base):
    __tablename__='produtos'

    id  = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    codigo_barras = Column(String(30), nullable=False, unique=True)
    preco =   Column(Float(), unique=True)
    em_estoque = Column(Boolean(),default = True)
    categoria_id = Column(ForeignKey('categorias.id'))
    def  __repr__(self):
        return f'Produto: {self.nome} Preço: {self.preco}'

class Categoria(Base):
    __tablename__='categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)

Base