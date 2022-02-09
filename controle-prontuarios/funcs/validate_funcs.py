import funcs.password_funcs as pf
from interfaces.consts import Regex
from interfaces.consts import ErrorPopup as error
from re import match
from datetime import datetime
from db.db_functions import DBFunctions as db
from interfaces.login_interface_lines import LoginInterfaceLines as login

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
    """Validação de usuário para login no sistema e guarda o id do usuario logado, caso esteja tudo certo."""
    if not usuario_digitado or not senha_digitada:
        raise error.USUARIO_INVALIDO_ERROR
    usuario = db.select_usuario(usuario_digitado)
    if not usuario:
        raise error.USUARIO_INVALIDO_ERROR
    senha_db = usuario[3]
    salt = usuario[4]
    hash_senha_digitada = pf.hashing_validate_password(senha_digitada, salt)
    if hash_senha_digitada == senha_db:
        login.id_usuario = usuario[0]
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
    if not sexo:
        raise error.SEXO_ERROR
    else:
        if not match(Regex.SEXO_REGEX, sexo):
            raise error.SEXO_ERROR
    if not match(Regex.DATA_REGEX, dt_nasc):
        raise error.NASC_ERROR
    return 1


def validate_search(num_sus='', nome_paciente='', dt_nasc='Ano-Mês-Dia'):
    """Valida os dados para a pesquisa do prontuário."""
    if (not num_sus) and (not nome_paciente) and (dt_nasc == 'Ano-Mês-Dia'):
        raise ValueError('ERRO: Nenhum dado informado para a busca!')
    else:
        if len(num_sus) >= 1:
            if not match(Regex.SUS_REGEX, num_sus):
                raise error.SUS_ERROR
        if len(nome_paciente) >= 1:
            if not match(Regex.NOME_REGEX, nome_paciente):
                raise error.NOME_ERROR
        if dt_nasc != 'Ano-Mês-Dia':
            if not match(Regex.DATA_REGEX, dt_nasc):
                raise error.NASC_ERROR
    return 1


def validate_search_input(num_sus, nome_paciente, dt_nasc):
    """Valida a saída de dados de pesquisa do DB, caso não encontre, retorna um erro."""
    if (not num_sus) and (not nome_paciente) and (dt_nasc == 'Ano-Mês-Dia'):
        raise ValueError('ERRO: Nenhum dado informado para a busca!')
    if (len(num_sus) >= 1) and (len(nome_paciente) >= 1):
        dados = db.select_sus_nome(num_sus, nome_paciente)
        if not dados:
            raise error.N_ENCONTRADO_ERROR
        else:
            return dados
    if len(num_sus) >= 1:
        dados = db.select_sus(num_sus)
        if not dados:
            raise error.N_ENCONTRADO_ERROR
        else:
            return dados
    if len(nome_paciente) >= 1:
        dados = db.select_nome(nome_paciente)
        if not dados:
            raise error.N_ENCONTRADO_ERROR
        else:
            return dados
    if dt_nasc != 'Ano-Mês-Dia':
        if match(Regex.DATA_REGEX, dt_nasc):
            dados = db.select_nasc(dt_nasc)
            if not dados:
                raise error.N_ENCONTRADO_ERROR
            else:
                return dados
    raise error.INPUT_EM_BRANCO


def validate_db_return_devolvidos():
    """Valida a saída de dados do DB para prontuários devolvidos, caso não encontre, retorna um erro."""
    dados = db.select_devolvidos()
    if not dados:
        raise error.N_ENCONTRADO_ERROR
    else:
        return dados


def validate_db_return_n_devolvidos():
    """Valida a saida de dados do DB para prontuários não devolvidos, caso não encontre, retorna um erro."""
    dados = db.select_nao_devolvidos()
    if not dados:
        raise error.N_ENCONTRADO_ERROR
    else:
        return dados


def validate_data_only(ano, mes, dia):
    """Valida a data, apenas a data."""
    data = f'{ano}-{mes}-{dia}'
    if data != 'Ano-Mês-Dia':
        if not match(Regex.DATA_REGEX, data):
            raise error.NASC_ERROR
    return 1


def validate_out(num_sus, nome_funcionario, dt_saida, hr_saida):
    """Valida a saída do prontuário."""
    if validate_saida(num_sus):
        if not match(Regex.SUS_REGEX, num_sus):
            raise error.SUS_ERROR
        if not match(Regex.FUNCIONARIO_REGEX, nome_funcionario):
            raise error.FUNCIONARIO_ERROR
        if not match(Regex.DATA_REGEX, dt_saida):
            raise error.DATA_ERROR
        if not match(Regex.HORA_REGEX, hr_saida):
            raise error.HORA_ERROR
    return 1


def validate_in(num_sus, nome_funcionario, dt_chegada, hr_chegada):
    """Valida a volta do prontuário."""
    dt_saida, hr_saida = str(db.select_sus(num_sus)[0][7]).split(' ')
    if validate_chegada(num_sus):
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


def validate_chegada(num_sus):
    """Verifica se prontuário está fora do arquivo antes de registrar chegada."""
    if movimentacao(num_sus):
        db_values = db.select_sus(num_sus)
        if db_values[0][10]:
            raise error.DEVOLVIDO_ERROR
    return 1


def validate_saida(num_sus):
    """Verifica se o prontuário está no arquivo antes de registrar saída."""
    if not match(Regex.SUS_REGEX, num_sus):
        raise error.SUS_ERROR
    db_values = db.select_sus(num_sus)
    if not db_values[0][10]:
        raise error.NAO_DEVOLVIDO_ERROR
    return 1


def movimentacao(num_sus):
    """Verifica se prontuário possui movimentação."""
    if not match(Regex.SUS_REGEX, num_sus):
        raise error.SUS_ERROR
    db_values = db.select_sus(num_sus)
    if db_values[0][10] == -1:
        raise error.SEM_MOVIMENTO_ERROR
    return 1


if __name__ == '__main__':
    try:
        print(validate_login_usuario('Maik4521', 'A1515151sss'))
    except ValueError as e:
        print(e)
