from sqlalchemy import create_engine
from modelos_escola import Base
engine = create_engine("sqlite:///memory:.db", echo=True)
print("Gerando schema do banco de dados")
Base.metadata.create_all(engine)
print(Base)