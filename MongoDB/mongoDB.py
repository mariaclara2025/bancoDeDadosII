from pymongo import MongoClient
uri = "mongodb+srv://mariasantos61_db_user:B81d5prPUA6gm2wl@cluster0.znic9gm.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

db = client['cinema']
colletion = db['filmes'] 
db = client.cinema

collection = db.filmes
from conexao import AtlasConnection
db_name ='filmes'
try:
    with AtlasConnection() as conexao:
        db = conexao.get_database(db_name)
        colletion = db['filmes']
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
    print(f"IDs dos documentos inseridos: {resultado_many.inserted_ids}")

    filmes_anos2000 = collection.find({"lançamento": {"$gte": 2000}})
    for filmes in filmes_anos2000:
        print(f"Segue a lista de filmes anos 2000: \n{filmes_anos2000}")
