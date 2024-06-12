import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Criar base de dados "stand_auto"
stand_auto = client["stand_auto"]

# Verifica se já existe a base de dados
dblist = client.list_database_names()
if "stand_auto" in dblist:
    print("A base de dados já existe.")

# Criar uma coleção carros
colecaoCarros = stand_auto["carros"]

# Verifica se já existe a coleção
collist = stand_auto.list_collection_names()
if "carros" in collist:
    print("A coleção carros já existe")

# Inserir um documento na coleção carros
hellcat = {"Marca": "Dodge", "Modelo": "Challenger", "Preco":30.000}
hellcat_documento = colecaoCarros.insert_one(hellcat)

# Nistrar o id do documento do carro hellcat
print(hellcat_documento.inserted_id)