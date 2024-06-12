import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Criar base de dados "stand_auto"
stand_auto = client["stand_auto"]

dblist = client.list_database_names()
if "stand_auto" in dblist:
    print("A base de dados já existe.")