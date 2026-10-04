import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv(override=True)

# Pega a conexão do MongoDB
uri = os.getenv("MONGO_URI")

# Conecta ao MongoDB
client = MongoClient(uri)

# Seleciona o banco e a coleção
db = client["saude_recife"]
usuarios = db["usuarios"]

# Testa a conexão
try:
    client.admin.command("ping")
    print("Conectado ao MongoDB com sucesso!")
except Exception as erro:
    print("Erro ao conectar ao MongoDB:")
    print(erro)