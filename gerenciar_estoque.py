import main as main
import cadastro_admin
from listar_produtos import lista_produtos
import produto
import efetuar_compras as efetuar_compras

admin_logado = False

def login_admin():
    global admin_logado
    print("Bem-vindo, administrador! Use seu usuário e senha:")

    while True:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        if cadastro_admin.validar_usuario_senha(usuario, senha):
            admin_logado = True
            print("Login bem-sucedido.")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

def gerenciar_estoque():
    global admin_logado

    if not admin_logado:
        print("Apenas administradores registrados podem gerenciar estoque.")
        login_admin()
        if not admin_logado:
            return

    print("Bem-vindo à área de gerenciamento de estoque")
    
    while True:
        print("1. Ver estoque de produtos")
        print("2. Adicionar itens no estoque")
        print("3. Excluir itens no estoque")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista_produtos.listar_produtos()
        elif opcao == '2':
            adicionar_estoque()
        elif opcao == '3':
            excluir_estoque()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_estoque():
    # Lógica para adicionar itens ao estoque 
    
      while True:
        print("Selecione uma opção:")
        print("1. Adicionar um novo produto")
        print("2. Adicionar quantidade a um produto existente")
        print("3. Voltar ao Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                codigo = input("Digite o código do produto: ")
                nome = input("Digite o nome do produto: ")
                marca = input("Digite a marca do produto: ")
                data_validade = input("Digite a data de validade do produto: ")
                preco = input("Digite o preço do produto: ")
                preco = float(preco.replace('R$', '').replace(',', '.').strip())
                quantidade = int(input("Digite a quantidade a ser adicionada: "))

                novo_produto = produto(codigo, nome, marca, data_validade, preco, quantidade)
                lista_produtos.append(novo_produto)
                print("Produto adicionado com sucesso.")

            except ValueError:
                print("Erro: Certifique-se de que o código é uma string, o preço é um número e a quantidade é um número inteiro.")

        elif opcao == "2":
            codigo = input("Digite o código do produto que deseja adicionar quantidade: ")

            for produto in lista_produtos:
                if produto.codigo == codigo:
                    print(f"Produto encontrado: {produto.nome} - {produto.marca}")
                    confirmar = input("Confirma a adição de quantidade a este produto? (s/n) ")

                    if confirmar.lower() == "s":
                        try:
                            quantidade = int(input("Digite a quantidade a ser adicionada: "))
                            produto.estoque += quantidade
                            print(f"{quantidade} unidades adicionadas ao estoque do produto {produto.nome}.")
                        except ValueError:
                            print("Erro: Certifique-se de que a quantidade é um número inteiro.")

                    break
            else:
                print("Produto não encontrado.")

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")

# Exemplo de uso da função
def atualizar_estoque(codigo, quantidade):
    for produto in lista_produtos:
        if produto.codigo == codigo:
            produto.estoque -= quantidade
            break
    else:
        print("Produto não encontrado.")

# Verificar se o produto foi adicionado ou atualizado corretamente
print("\nLista de Produtos Atualizada:")
for produto in lista_produtos:
    print(f"Código: {produto.codigo}, Nome: {produto.nome}, Marca: {produto.marca}, Data de Validade: {produto.data_validade}, Preço: {produto.preco}, Estoque: {produto.estoque}")
    pass

def excluir_estoque():
    # Lógica para excluir itens do estoque (apenas administrador)
    
      while True:
        print("Selecione uma opção:")
        print("1. Excluir um produto")
        print("2. Diminuir a quantidade a um produto existente")
        print("3. Voltar ao Menu Inicial")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                codigo = input("Digite o código do produto: ")
                nome = input("Digite o nome do produto: ")
                marca = input("Digite a marca do produto: ")
                data_validade = input("Digite a data de validade do produto: ")
                preco = input("Digite o preço do produto: ")
                preco = float(preco.replace('R$', '').replace(',', '.').strip())
                quantidade = int(input("Digite a quantidade a ser adicionada: "))

                excluir_produto = produto(codigo, nome, marca, data_validade, preco, quantidade)
                lista_produtos.append(excluir_produto)
                print("Produto excluído com sucesso.")

            except ValueError:
                print("Erro: Certifique-se de que o código é uma string, o preço é um número e a quantidade é um número inteiro.")

        elif opcao == "2":
            codigo = input("Digite o código do produto que deseja diminuir a quantidade: ")

            for produto in lista_produtos:
                if produto.codigo == codigo:
                    print(f"Produto encontrado: {produto.nome} - {produto.marca}")
                    confirmar = input("Confirma a redução de quantidade a este produto? (s/n) ")

                    if confirmar.lower() == "s":
                        try:
                            quantidade = int(input("Digite a quantidade a ser diminuída: "))
                            produto.estoque -= quantidade
                            print(f"{quantidade} unidades diminuídas ao estoque do produto {produto.nome}.")
                        except ValueError:
                            print("Erro: Certifique-se de que a quantidade é um número inteiro.")

                    break
            else:
                print("Produto não encontrado.")

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")