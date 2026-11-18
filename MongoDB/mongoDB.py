
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Conectado com sucesso ao MongoDB!\n")

    db = client['cinema']
    collection = db['filmes']

    collection.delete_many({})

    lista_filmes = [
        {
            "titulo": "A Origem",
            "diretor": "Christopher Nolan",
            "lançamento": 2010,
            "generos": ["Ação", "Ficção Científica", "Aventura"]
        },
        {
            "titulo": "O Chefão",
            "diretor": "Francis Ford Coppola",
            "lançamento": 1972,
            "generos": ["Crime", "Drama"]
        },
        {
            "titulo": "A Viagem de Chihiro",
            "diretor": "Hayao Miyazaki",
            "lançamento": 2001,
            "generos": ["Animação", "Aventura", "Família", "Fantasia"]
        }
    ]

    resultado_many = collection.insert_many(lista_filmes)
    print(f"IDs inseridos: {resultado_many.inserted_ids}\n")

    # ==========================================
    # EXERCÍCIO 2 - OPERADORES DE CONSULTA
    # ==========================================

    filtro_equal = {"titulo": {"$eq": "O Chefão"}}
    res_equal = collection.find(filtro_equal)
    print("1. EQUAL (Título == 'O Chefão'):")
    for filme in res_equal:
        print("  ->", filme)

    filmes_maior_2000 = collection.find({"lançamento": {"$gte": 2000}})
    filmes_menor_2000 = collection.find({"lançamento": {"$lt": 2000}})
    
    print("\n2. MAIOR/MENOR (Lançamento >= 2000):")
    for filme in filmes_maior_2000:
        print("  ->", filme["titulo"], "-", filme["lançamento"])

    print("   MAIOR/MENOR (Lançamento < 2000):")
    for filme in filmes_menor_2000:
        print("  ->", filme["titulo"], "-", filme["lançamento"])

    filmes_drama = collection.find({"generos": {"$in": ["Drama"]}})
    filmes_nao_drama = collection.find({"generos": {"$nin": ["Drama"]}})

    print("\n3. IN (Contém gênero 'Drama'):")
    for filme in filmes_drama:
        print("  ->", filme["titulo"])

    print("   NIN (NÃO contém gênero 'Drama'):")
    for filme in filmes_nao_drama:
        print("  ->", filme["titulo"])

    filmes_com_diretor = collection.find({"diretor": {"$exists": True}})
    filmes_com_premio = collection.find({"oscar": {"$exists": True}})

    print("\n4. EXISTS (Filmes que possuem o campo 'diretor'):")
    for filme in filmes_com_diretor:
        print("  ->", filme["titulo"], "| Diretor:", filme["diretor"])

    filmes_acao_aventura = collection.find({"generos": {"$all": ["Ação", "Aventura"]}})

    print("\n5. ALL (Contém 'Ação' E 'Aventura' simultaneamente):")
    for filme in filmes_acao_aventura:
        print("  ->", filme["titulo"], "| Gêneros:", filme["generos"])

    filmes_2_generos = collection.find({"generos": {"$size": 2}})
    filmes_3_generos = collection.find({"generos": {"$size": 3}})

    print("\n6. SIZE (Filmes com  2 gêneros):")
    for filme in filmes_2_generos:
        print("  ->", filme["titulo"], "| Gêneros:", filme["generos"])

    for filme in filmes_3_generos:
        print("  ->", filme["titulo"], "| Gêneros:", filme["generos"])

except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    client.close()