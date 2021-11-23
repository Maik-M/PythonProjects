import funcs.password_funcs as pf
from interfaces.consts import Regex
from interfaces.consts import ErrorPopup as error
from re import match
from datetime import datetime
from db.db_functions import DBFunctions as db

########################################################################################################################
# AQUI ESTÃO AS FUNÇÕES PARA VALIDAÇÕES DE DADOS DE ENTRADA DE USUÁRIOS E PRONTUÁRIOS ##################################
########################################################################################################################

###################
# Functions #######-----------------------------------------------------------------------------------------------------
###################


# Usuários -----------------------------------
def validate_register_usuario(usuario, senha):
    """Valida os dados de registro de novo usuário."""
    if not match(Regex.USUARIO_REGEX, usuario):
        raise error.USUARIO_ERROR
    if not match(Regex.SENHA_REGEX, senha):
        raise error.SENHA_ERROR
    if db.select_usuario(usuario):
        raise error.USUARIO_EXISTENTE_ERROR
    return 1


def validate_login_usuario(usuario_digitado, senha_digitada):
    """Validação de usuário para login no sistema."""
    if not usuario_digitado or not senha_digitada:
        raise error.USUARIO_INVALIDO_ERROR
    usuario = db.select_usuario(usuario_digitado)
    senha_db = usuario[3]
    salt = usuario[4]
    hash_senha_digitada = pf.hashing_validate_password(senha_digitada, salt)
    if hash_senha_digitada == senha_db:
        return 1
    else:
        raise error.USUARIO_INVALIDO_ERROR


# Prontuários ------------------------------------------------------------
def validate_register(num_sus, nome_paciente, sexo, dt_nasc, nome_mae=''):
    """Valida os dados para o registro do prontuário."""
    if not match(Regex.SUS_REGEX, num_sus):
        raise error.SUS_ERROR
    if not match(Regex.NOME_REGEX, nome_paciente):
        raise error.NOME_ERROR
    if len(nome_mae) >= 1:
        if not match(Regex.NOME_REGEX, nome_mae):
            raise error.MAE_ERROR
    if not match(Regex.SEXO_REGEX, sexo):
        raise error.SEXO_ERROR
    if not match(Regex.DATA_REGEX, dt_nasc):
        raise error.NASC_ERROR
    return 1


def validate_find(num_sus='', nome_paciente='', dt_nasc=''):
    """Valida os dados para a pesquisa do prontuário."""
    if (num_sus == '') and (nome_paciente == '') and (dt_nasc == ''):
        raise ValueError('ERRO: Nenhum dado informado para a busca!')
    else:
        if len(num_sus) >= 1:
            if not match(Regex.SUS_REGEX, num_sus):
                raise error.SUS_ERROR
        if len(nome_paciente) >= 1:
            if not match(Regex.NOME_REGEX, nome_paciente):
                raise error.NOME_ERROR
        if len(dt_nasc) >= 1:
            if not match(Regex.DATA_REGEX, dt_nasc):
                raise error.NASC_ERROR
    return 1


def validate_out(num_sus, nome_funcionario, dt_saida, hr_saida):
    """Valida a saída do prontuário."""
    if not match(Regex.SUS_REGEX, num_sus):
        raise error.SUS_ERROR
    if not match(Regex.FUNCIONARIO_REGEX, nome_funcionario):
        raise error.FUNCIONARIO_ERROR
    if not match(Regex.DATA_REGEX, dt_saida):
        raise error.DATA_ERROR
    if not match(Regex.HORA_REGEX, hr_saida):
        raise error.HORA_ERROR
    return 1


def validate_in(num_sus, nome_funcionario, dt_saida, hr_saida, dt_chegada, hr_chegada):
    """Valida a volta do prontuário."""
    date_saida = datetime.strptime(dt_saida, '%Y-%m-%d')
    date_chegada = datetime.strptime(dt_chegada, '%Y-%m-%d')
    hora_saida = datetime.strptime(hr_saida, '%H:%M')
    hora_chegada = datetime.strptime(hr_chegada, '%H:%M')
    if not match(Regex.SUS_REGEX, num_sus):
        raise error.SUS_ERROR
    if not match(Regex.FUNCIONARIO_REGEX, nome_funcionario):
        raise error.FUNCIONARIO_ERROR
    # Verifica data se não é menor que a data de saida
    if not match(Regex.DATA_REGEX, dt_chegada):
        raise error.DATA_ERROR
    elif not match(Regex.HORA_REGEX, hr_chegada):
        raise error.HORA_ERROR
    else:
        if date_saida > date_chegada:
            raise error.DATA_MENOR_ERROR
        elif date_saida == date_chegada:
            if hora_saida > hora_chegada:
                raise error.HORA_MENOR_ERROR
    return 1


def validate_chegada(is_devolvido):
    """Verifica se prontuário está fora do arquivo antes de registrar chegada."""
    if is_devolvido:
        raise error.DEVOLVIDO_ERROR
    return 1


def validate_saida(is_devolvido):
    """Verifica de prontuário no arquivo antes de registrar saída."""
    if not is_devolvido:
        raise error.NAO_DEVOLVIDO_ERROR
    return 1


def movimentacao(is_devolvido):
    """Verifica se prontuário possui movimentação."""
    if is_devolvido == -1:
        raise error.SEM_MOVIMENTO_ERROR
    return 1


if __name__ == '__main__':
    try:
        print(validate_login_usuario('Maik4521', 'A1515151sss'))
    except ValueError as e:
        print(e)
