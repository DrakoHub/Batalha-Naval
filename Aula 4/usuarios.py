usuarios = []

def cadastrar_usuario(nome, email):
    usuarios.append({'nome': nome, 'email': email})
def listar_usuarios():
    if not usuarios:
        print("Nenhum Usuario Cadastrado pelo Sistema.")
    else:
        print("\n Lista de Usuarios")
        for i, u in enumerate(usuarios, 1):
            print(f"{i}. Nome: {u['nome']} | Email: {u['email']}")
