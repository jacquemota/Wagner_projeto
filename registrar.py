import cadastro_cliente
import cadastro_admin

def registrar():
    print("Opções de Registro:")
    print("1. Cliente")
    print("2. Administrador")
    opcao = input("Escolha uma opção de registro: ")
    
    if opcao == '1':
        while True:
            nome = input("Digite o nome completo: ")
            if cadastro_cliente.verificar_nome(nome):
                break
            else:
                print("Nome inválido. O nome não pode conter caracteres iguais.")

        while True:
            email = input("Digite o email: ")
            if cadastro_cliente.verificar_email(email):
                break
            else:
                print("Email inválido. O email deve conter '@'.")

        while True:
            usuario = input("Digite o usuário: ")
            senha = input("Digite a senha: ")

            if cadastro_cliente.validar_usuario_senha(usuario, senha):
                break
            else:
                print("Usuário ou senha incorretos.")

        while True:
            endereco = input("Digite o endereço: ")
            if cadastro_cliente.verificar_endereco(endereco):
                break
            else:
                print("Endereço inválido")

        print("Cadastro de cliente realizado com sucesso!")

    elif opcao == '2':
        while True:
            nome_admin = input("Digite o nome completo do administrador: ")
            if cadastro_admin.verificar_nome(nome_admin):
                break
            else:
                print("Nome inválido. O nome não pode conter caracteres iguais.")

        while True:
            email_admin = input("Digite o email do administrador: ")
            if cadastro_admin.verificar_email(email_admin):
                break
            else:
                print("Email inválido. O email deve conter '@'.")

        while True:
            usuario_admin = input("Digite o usuário do administrador: ")
            senha_admin = input("Digite a senha do administrador: ")

            if cadastro_admin.validar_usuario_senha(usuario_admin, senha_admin):
                break
            else:
                print("Usuário ou senha incorretos.")


        print("Cadastro de administrador realizado com sucesso!")

    else:
        print("Opção inválida. Tente novamente.")