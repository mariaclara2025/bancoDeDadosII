from sqlalchemy import create_engine
from modelos_loja import Base
engine = create_engine("sqlite:///loja_virtual.db", echo=True)
print("Gerando schema do banco de dados")
Base.metadata.create_all(engine)
print(Base)