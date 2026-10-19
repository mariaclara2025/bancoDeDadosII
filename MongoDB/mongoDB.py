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