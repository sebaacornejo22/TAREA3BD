from pymongo import MongoClient
import os
import hashlib
from sentence_transformers import SentenceTransformer

# Ruta donde están los discursos
ruta_discursos = "DiscursosOriginales"

# Conexión a MongoDB
uri = "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set&readPreference=primary&ssl=false"
client = MongoClient(uri)
db = client['Politica']
collection = db['Discursos']

# Inicializar modelo de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo liviano para embeddings

# Funciones auxiliares
def calcular_hash(texto):
    """Genera hash SHA-256 de un texto"""
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

def generar_embedding(texto):
    """Genera embedding vectorial del texto"""
    return modelo.encode(texto).tolist()

# Procesar todos los archivos .txt
archivos = [f for f in os.listdir(ruta_discursos) if f.endswith(".txt")]
total_archivos = len(archivos)  # Total de archivos a procesar
contador = 0  # Contador de archivos procesados

for archivo in archivos:
    ruta = os.path.join(ruta_discursos, archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read()

    _id = calcular_hash(texto)
    embedding = generar_embedding(texto)

    documento = {
        "_id": _id,
        "texto": texto,
        "embedding": embedding
    }

    # Insertar o actualizar documento en MongoDB
    collection.replace_one({"_id": _id}, documento, upsert=True)

    # Incrementar contador de archivos
    contador += 1

print(f"Todos los documentos fueron procesados e insertados correctamente. Total: {contador}")
