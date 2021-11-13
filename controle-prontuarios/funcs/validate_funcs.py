from re import compile, match
from datetime import datetime

# Regex ----------------------------------------------------------------------------------------------------------------
SUS_REGEX = compile(r'[^a-zA-Z]{15}$')
NOME_REGEX = compile(r'[a-z A-Z]{5,80}$')
SEXO_REGEX = compile(r'[MF]$')
DATA_REGEX = compile(r'(([1]|[2])([0-9]{3}))-(([0][1-9])|([1][0-2]))-(([0][1-9])|([1-2][0-9])|([3][0-1]))$')
HORA_REGEX = compile(r'(([0][0-9])|([1][0-9])|([2][1-3])):([0-5][0-9])$')
FUNCIONARIO_REGEX = compile(r'[a-zA-Z]{2,15}')

# Error messagens ------------------------------------------------------------------------------------------------------
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


# Functions ------------------------------------------------------------------------------------------------------------
def validate_register(num_sus, nome_paciente, sexo, dt_nasc, nome_mae=''):
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
    date_saida = datetime.strptime(dt_saida, '%Y-%m-%d')
    date_chegada = datetime.strptime(dt_chegada, '%Y-%m-%d')
    hora_saida = datetime.strptime(hr_saida, '%H:%M')
    hora_chegada = datetime.strptime(hr_chegada, '%H:%M')

    if not match(SUS_REGEX, num_sus):
        raise SUS_ERROR
    if not match(FUNCIONARIO_REGEX, nome_funcionario):
        raise FUNCIONARIO_ERROR

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


if __name__ == '__main__':
    try:
        print(validate_in('123456789123456', 'Ana Carolina', '2021-01-01', '13:56', '2020-01-02', '13:54'))
    except ValueError as e:
        print(e)