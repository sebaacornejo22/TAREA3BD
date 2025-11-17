# Proyecto: Procesamiento de Discursos Políticos

## Nombre y Rol
- **Nombre:** Sebastián Ignacio Cornejo Yañez  
- **Rol:** 202373602-3  
- **Nombre:** Emilio Jesus Moran Valdebenito
- **Rol:** 202473575-6

---

## Instalación y Configuración Técnica

1. Requisitos previos:
    - Docker Desktop instalado  
    - Docker Compose instalado  
    - Python 3 (recomendado 3.10 o superior)  

2. Instalación de librerías necesarias
    - Cliente MongoDB:
    > pip install pymongo
    - Modelo de embeddings:
    > pip install sentence-transformers

3. Crear carpetas para almacenar datos de MongoDB y dar permisos:
    > mkdir -p data/mongo-1 data/mongo-2 data/mongo-3
    > chmod -R 777 data/mongo-1 data/mongo-2 data/mongo-3

3. Levantar el Replica Set con Docker Compose:
    - El proyecto incluye un archivo: "deploy-rol1-rol2.yml"
    - Para levantar el cluster se ejecuta:
    > docker compose -f deploy-rol1-rol2.yml up -d
    - Verificar servicios: 
    > docker ps

4. Configuración del archivo "/etc/hosts":
    **Permite que Python se conecte usando los nombres del cluster:**
    > sudo nano /etc/hosts
    - Y Agregar:
    127.0.0.1 mongo1
    127.0.0.1 mongo2
    127.0.0.1 mongo3

5. Ejecutar y procesar discursos:
    > python3 procesar_discursos.py

## Extras:
- Para hacer correr los contenedores si ya estan creados:
    > docker start mongo1 mongo2 mongo3
- Abrir el shell de MongoDB:
    > docker exec -it mongo3 mongosh --port 30003
    (mongo1/mongo2/mongo3) y puerto, depende de la replica primaria.
- Verificar documentos dentro de shell de MongoDB:
    > use Politica
    > db.Discursos.countDocuments()