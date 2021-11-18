from re import compile, match
from datetime import datetime


# Regex ----------------------------------------------------------------------------------------------------------------
USUARIO_REGEX = compile(r'[a-zA-Z0-9-_.]{4,10}$')
SENHA_REGEX = compile(r'[a-z A-Z0-9-_@#*]{5,12}$')
SUS_REGEX = compile(r'[^a-zA-Z]{15}$')
NOME_REGEX = compile(r'[a-zA-Zà-úÀ-Ú ]{5,80}$')
SEXO_REGEX = compile(r'[MF]$')
DATA_REGEX = compile(r'(([1]|[2])([0-9]{3}))-(([0][1-9])|([1][0-2]))-(([0][1-9])|([1-2][0-9])|([3][0-1]))$')
HORA_REGEX = compile(r'(([0][0-9])|([1][0-9])|([2][1-3])):([0-5][0-9])$')
FUNCIONARIO_REGEX = compile(r'[a-zA-Z]{2,15}$')


# Error messagens ------------------------------------------------------------------------------------------------------
USUARIO_ERROR = ValueError('ERRO: O usuário pode conter: Lestrar, Números, "-", "_", ".", não aceita espaço e '
                           'deve conter de 4 à 10 caractéres!')
SENHA_ERROR = ValueError('ERRO: A senha deve conter de 5 à 12 caractéres!')
SUS_ERROR = ValueError('ERRO: O nome do paciente deve conter de 5 à 80 letras e não deve conter números!')
NOME_ERROR = ValueError('ERRO: O nome do paciente deve conter de 5 à 80 letras e não deve conter números!')
MAE_ERROR = ValueError('ERRO: Nome da mãe não é obrigatório, mas caso for preenchido,'
                       'deve conter de 5 à 80 letras e não conter números!')
SEXO_ERROR = ValueError('ERRO: Sexo não informado!')
NASC_ERROR = ValueError('ERRO: Data de nascimento não informada ou incorreta!')
DATA_ERROR = ValueError('ERRO: Data não informada ou inválida!')
DATA_MENOR_ERROR = ValueError('ERRO: Data de chegada pode ser anterior a data de saída!')
FUNCIONARIO_ERROR = ValueError('ERRO: Nome do funcionário não informado ou inválido!')
HORA_ERROR = ValueError('ERRO: Hora não informada ou inválida!')
HORA_MENOR_ERROR = ValueError('ERRO: Datas iguais! Nesse caso, a hora da chegada não pode ser menor que a da saída!')
DEVOLVIDO_ERROR = ValueError('ERRO: Prontuário já foi devolvido! Verifique o número do SUS.')
NAO_DEVOLVIDO_ERROR = ValueError('ERRO: Esse prontuário ainda não foi devolvido! Verifiquei o número do SUS.')
SEM_MOVIMENTO_ERROR = ValueError('ERRO: Prontuário ainda sem movimentação!')


# Functions ------------------------------------------------------------------------------------------------------------
def validate_register(num_sus, nome_paciente, sexo, dt_nasc, nome_mae=''):
    """Valida os dados para o registro do prontuário."""
    if not match(SUS_REGEX, num_sus):
        raise SUS_ERROR
    if not match(NOME_REGEX, nome_paciente):
        raise NOME_ERROR
    if len(nome_mae) >= 1:
        if not match(NOME_REGEX, nome_mae):
            raise MAE_ERROR
    if not match(SEXO_REGEX, sexo):
        raise SEXO_ERROR
    if not match(DATA_REGEX, dt_nasc):
        raise NASC_ERROR
    return 1


def validate_find(num_sus='', nome_paciente='', dt_nasc=''):
    """Valida os dados para a pesquisa do prontuário."""
    if (num_sus == '') and (nome_paciente == '') and (dt_nasc == ''):
        raise ValueError('ERRO: Nenhum dado informado para a busca!')
    else:
        if len(num_sus) >= 1:
            if not match(SUS_REGEX, num_sus):
                raise SUS_ERROR
        if len(nome_paciente) >= 1:
            if not match(NOME_REGEX, nome_paciente):
                raise NOME_ERROR
        if len(dt_nasc) >= 1:
            if not match(DATA_REGEX, dt_nasc):
                raise NASC_ERROR
    return 1


def validate_out(num_sus, nome_funcionario, dt_saida, hr_saida):
    """Valida a saída do prontuário."""
    if not match(SUS_REGEX, num_sus):
        raise SUS_ERROR
    if not match(FUNCIONARIO_REGEX, nome_funcionario):
        raise FUNCIONARIO_ERROR
    if not match(DATA_REGEX, dt_saida):
        raise DATA_ERROR
    if not match(HORA_REGEX, hr_saida):
        raise HORA_ERROR
    return 1


def validate_in(num_sus, nome_funcionario, dt_saida, hr_saida, dt_chegada, hr_chegada):
    """Valida a volta do prontuário."""
    date_saida = datetime.strptime(dt_saida, '%Y-%m-%d')
    date_chegada = datetime.strptime(dt_chegada, '%Y-%m-%d')
    hora_saida = datetime.strptime(hr_saida, '%H:%M')
    hora_chegada = datetime.strptime(hr_chegada, '%H:%M')
    if not match(SUS_REGEX, num_sus):
        raise SUS_ERROR
    if not match(FUNCIONARIO_REGEX, nome_funcionario):
        raise FUNCIONARIO_ERROR
    # Verifica data se não é menor que a data de saida
    if not match(DATA_REGEX, dt_chegada):
        raise DATA_ERROR
    elif not match(HORA_REGEX, hr_chegada):
        raise HORA_ERROR
    else:
        if date_saida > date_chegada:
            raise DATA_MENOR_ERROR
        elif date_saida == date_chegada:
            if hora_saida > hora_chegada:
                raise HORA_MENOR_ERROR
    return 1


def validate_chegada(is_devolvido):
    """Verifica se prontuário está fora do arquivo antes de registrar chegada."""
    if is_devolvido:
        raise DEVOLVIDO_ERROR
    return 1


def validate_saida(is_devolvido):
    """Verifica de prontuário no arquivo antes de registrar saída."""
    if not is_devolvido:
        raise NAO_DEVOLVIDO_ERROR
    return 1


def movimentacao(is_devolvido):
    """Verifica se prontuário possui movimentação."""
    if is_devolvido == -1:
        raise SEM_MOVIMENTO_ERROR
    return 1


if __name__ == '__main__':
    try:
        print()
    except ValueError as e:
        print(e)
