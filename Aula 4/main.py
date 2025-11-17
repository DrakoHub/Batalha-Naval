from usuarios import cadastrar_usuario, listar_usuarios
from formatacao import formatar_nome, validar_email

def menu():
    while True:
        print("\n==== Menu ====")
        print("1. Cadastrar novo usuário")
        print("2. Listar usuários")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            nome_formatado = formatar_nome(nome)

            while True:
                email = input("Digite o e-mail: ")
                if validar_email(email):
                    break
                print("E-mail inválido. Tente novamente.")

            cadastrar_usuario(nome_formatado, email)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
