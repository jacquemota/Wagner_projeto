import gerenciar_estoque as gerenciar_estoque

def cadastro_admin():
    

    def verificar_nome(nome):
    # Verifique se o nome não contém caracteres iguais
        if len(set(nome)) == 1:
            return False
        elif nome.lower() in ["sim", "não"]:
            return False
    return True

def verificar_email(email):
    # Verifique se o email contém '@'
    if '@' not in email:
        return False
    return True

def validar_usuario_senha(usuario, senha):
    # Verifique se o usuário e senha estão corretos
    if usuario == 'admin' and senha == '1234':
        return True
    return False
    pass