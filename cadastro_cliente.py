import efetuar_compras as efetuar_compras


def verificar_nome(nome):
    # Verifique se o nome não contém caracteres iguais
    if len(set(nome)) == 1:
        return False
    nome_estranho = ["sim", "não"]
    if nome == nome_estranho:
        return False 
    return True

def verificar_email(email):
    # Verifique se o email contém '@'
    if '@' not in email:
        return False
    return True

def validar_usuario_senha(usuario, senha):
    # Verifique se o usuário e senha estão corretos
    if usuario == 'cliente' and senha == 'cliente':
        return True
    return False

def verificar_endereco(endereco):
    # Verifique se o endereço é 'cliente'
    if endereco == 'cliente':
        return True
    return False