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

# CREATE - cadastrar usuário
def criar_usuario():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    usuario = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    resultado = usuarios.insert_one(usuario)

    print("Usuário cadastrado com sucesso!")
    print("ID:", resultado.inserted_id)


# READ - listar usuários
def listar_usuarios():
    print("\n--- USUÁRIOS CADASTRADOS ---")

    for usuario in usuarios.find():
        print("ID:", usuario["_id"])
        print("Nome:", usuario["nome"])
        print("Email:", usuario["email"])
        print("Telefone:", usuario["telefone"])
        print("---------------------------")

# UPDATE - atualizar usuário
def atualizar_usuario():
    email = input("Digite o email do usuário que deseja atualizar: ")

    usuario = usuarios.find_one({"email": email})

    if usuario:
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")

        usuarios.update_one(
            {"email": email},
            {
                "$set": {
                    "nome": novo_nome,
                    "telefone": novo_telefone
                }
            }
        )

        print("Usuário atualizado com sucesso!")

    else:
        print("Usuário não encontrado!")

# DELETE - excluir usuário
def excluir_usuario():
    email = input("Digite o email do usuário que deseja excluir: ")

    usuario = usuarios.find_one({"email": email})

    if usuario:
        usuarios.delete_one({"email": email})
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado!")

# MENU
while True:
    print("\n===== SAÚDE RECIFE =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        atualizar_usuario()

    elif opcao == "4":
        excluir_usuario()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")