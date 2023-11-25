# main.py
import cadastro_cliente
import efetuar_compras 
import listar_produtos 
import gerenciar_estoque 
import cadastro_admin
import registrar 
import produto as produto



def menu():
    while True:
        print("Menu Principal:")
        print("1. Efetuar Compras")
        print("2. Listar Produtos")
        print("3. Gerenciar Estoque (Apenas Administrador)")
        print("4. Registrar-se")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            efetuar_compras.efetuar_compras()
        elif opcao == '2':
            listar_produtos.listar_produtos()
        elif opcao == '3':
            gerenciar_estoque.gerenciar_estoque()
        elif opcao == '4':
            registrar.registrar()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
            
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    executando = True
    while executando:
        menu()
        reiniciar = input("Deseja reiniciar o menu? (s/n): ")
        if reiniciar.lower() != 's':
            executando = False


