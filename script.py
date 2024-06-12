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

"""
# Mostrar o id do documento do carro hellcat
hellcat_documento = colecaoCarros.insert_one(hellcat)
print(hellcat_documento.inserted_id)
"""

# Inserir vários documentos na coleção carros
carros_americanos = [
    {"Marca": "Ford", "Modelo": "Mustang", "Preco":30.920},
    {"Marca": "Chevrolet", "Modelo": "Camaro", "Preco":40.100},
    {"Marca": "Cadillac", "Modelo": "CT4-V Blackwing", "Preco":62.000}
]

carros_docs = colecaoCarros.insert_many(carros_americanos)
"""
# Mostrar ids dos carros
print(carros_docs.inserted_ids)
"""

# Mostrar o primeiro documento na coleção carros
primeiro_carro = colecaoCarros.find_one()
print(primeiro_carro)