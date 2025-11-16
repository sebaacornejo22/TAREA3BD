from pymongo import MongoClient

# Dirección de conexión al replica set
uri = "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set&readPreference=primary&ssl=false"

# Crear cliente
client = MongoClient(uri)

# Probar la conexión mostrando las bases de datos existentes
print("Bases de datos disponibles:")
print(client.list_database_names())
