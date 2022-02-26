from hashlib import sha512
from uuid import uuid4


########################################################################################################################
# AQUI ESTÃO AS FUNÇÕES PARA FAZEER O HASHING DA SENHA PARA SALVAR NO DB JUNTAMENTE COM SALT ###########################
########################################################################################################################

def hashing_password(senha):
    """Faz o hash da password com o salt, e retorna ambos."""
    salt = uuid4().hex
    hash_senha = sha512(senha.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return hash_senha, salt


def hashing_validate_password(senha, salt):
    """Faz o hash da password digitada pela usuário para comparação."""
    hash_senha = sha512(senha.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return hash_senha
