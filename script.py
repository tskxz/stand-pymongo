import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Criar base de dados "stand_auto"
stand_auto = client["stand_auto"]

# Verifica se já existe a base de dados
dblist = client.list_database_names()
if "stand_auto" in dblist:
    print("A base de dados já existe.")

collecaoCarros = stand_auto["carros"]

collist = stand_auto.list_collection_names()
if "carros" in collist:
    print("A coleção carros já existe")