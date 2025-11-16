Nombre: Sebastián Ignacio Cornejo Yañez
Rol: 202373602-3
Nombre:
Rol:

Instalación y Configuración Técnica (paso a paso)
Requisitos previos:
Docker Desktop instalado
Docker Compose instalado
Python 3

Instalar librerias necesarias:
# Cliente MongoDB
pip install pymongo

# Modelo de embeddings
pip install sentence-transformers

Levantar el Replica Set con Docker Compose:
El proyecto incluye un archivo: deploy-rol1-rol2.yml

Para levantar el cluster se ejecuta: docker compose -f deploy-rol1-rol2.yml up -d

Verificar servicios: docker ps

Configuración del archivo "/etc/hosts" para permitir que Python se conecte usando los nombres del cluster:

Editar /etc/hosts: sudo nano /etc/hosts

Y Agregar:
127.0.0.1 mongo1
127.0.0.1 mongo2
127.0.0.1 mongo3

Para hacer correr los contenedores si ya estan creados:
docker start mongo1 mongo2 mongo3