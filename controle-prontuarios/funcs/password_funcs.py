from hashlib import sha512
from uuid import uuid4


def hashing_password(senha):
    salt = uuid4().hex
    hash_senha = sha512(senha.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return hash_senha, salt


def hashing_validate_password(senha, salt):
    hash_senha = sha512(senha.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return hash_senha
