from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text())
    print(result.scalar())