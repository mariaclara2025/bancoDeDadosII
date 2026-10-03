from sqlalchemy import create_engine, text
from models import Base 
engine = create_engine("sqlite://memory:.db", echo=True)
Session = sessionmaker(bind=engine)
Base.metadase.create_all(engine)

with engine.connect() as connection:
    console.log('Sistema de Loja Virtual Conectado com Sucesso')
    result = connection.execute(text('Select sqlite_version()'))
    print(result.scalar())