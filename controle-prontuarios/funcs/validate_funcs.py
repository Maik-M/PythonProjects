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
def validate_new_user(user_name, user, password, re_password):
    """Valida os dados de registro de novo usuário."""
    if len(user_name) <= 5:
        raise error.SHORT_NAME_ERROR
    if not match(Regex.USER_REGEX, user):
        raise error.USER_ERROR
    if not match(Regex.PASSWORD_REGEX, password):
        raise error.PASSW_ERROR
    if password != re_password:
        raise error.PASSW_ERROR_2
    if db.select_user(user):
        raise error.USER_EXIST_ERROR
    return 1


def validate_user_login(user_input, password_input):
    """Validação de usuário para login no sistema e guarda o id do user logado, caso esteja tudo certo."""
    if not user_input or not password_input:
        raise error.INVALID_USER_ERROR
    user = db.select_user(user_input)
    if not user:
        raise error.INVALID_USER_ERROR
    db_password = user[3]
    salt = user[4]
    hash_input_passw = pf.hashing_validate_password(password_input, salt)
    if hash_input_passw == db_password:
        login.user_id = user[0]
        return 1
    else:
        raise error.INVALID_USER_ERROR


def validate_return_user(id_user):
    """Valida a busca de usuário."""
    db_return = db.select_user_id(id_user)
    if not db_return:
        raise error.USER_N_FOUND_ERROR
    return db_return[1]


# Prontuários ------------------------------------------------------------
def validate_register(sus_number, patient_name, gender, bith_date, mother=''):
    """Valida os dados para o registro do prontuário."""
    if not match(Regex.SUS_REGEX, sus_number):
        raise error.SUS_ERROR
    if not match(Regex.NAME_REGEX, patient_name):
        raise error.NAME_ERROR
    if len(mother) >= 1:
        if not match(Regex.NAME_REGEX, mother):
            raise error.MOTHER_ERROR
    if not gender:
        raise error.GENDER_ERROR
    else:
        if not match(Regex.GENDER_REGEX, gender):
            raise error.GENDER_ERROR
    if not match(Regex.DATE_REGEX, bith_date):
        raise error.BIRTH_ERROR
    return 1


def validate_search(sus_number='', patient_name='', birth_date='Ano-Mês-Dia'):
    """Valida os dados para a pesquisa do prontuário."""
    if (not sus_number) and (not patient_name) and (birth_date == 'Ano-Mês-Dia'):
        raise ValueError('ERRO: Nenhum dado informado para a busca!')
    else:
        if len(sus_number) >= 1:
            if not match(Regex.SUS_REGEX, sus_number):
                raise error.SUS_ERROR
        if len(patient_name) >= 1:
            if not match(Regex.NAME_REGEX, patient_name):
                raise error.NAME_ERROR
        if birth_date != 'Ano-Mês-Dia':
            if not match(Regex.DATE_REGEX, birth_date):
                raise error.BIRTH_ERROR
    return 1


def validate_edit(sus_number, patient_name, gender, birth_date, mother):
    """Valida os dados antes de alterar."""
    if (not patient_name) and (not gender) and (birth_date == 'Ano-Mês-Dia') and (not mother):
        raise ValueError('ERRO: Nenhum dado informado pra alteração! Por favor, informe o dado que vocÊ deseja alterar.')
    else:
        if len(patient_name) >= 1:
            if not match(Regex.NAME_REGEX, patient_name):
                raise error.NAME_ERROR
            db.update_name(patient_name, sus_number)
        if len(mother) >= 1:
            if not match(Regex.NAME_REGEX, mother):
                raise error.MOTHER_ERROR
            db.update_mother(mother, sus_number)
        if birth_date != 'Ano-Mês-Dia':
            if not match(Regex.DATE_REGEX, birth_date):
                raise error.BIRTH_ERROR
            db.update_birth(birth_date, sus_number)
        if gender:
            if not match(Regex.GENDER_REGEX, gender):
                raise error.GENDER_ERROR
            db.update_gender(gender, sus_number)



def validate_sus(sus_number):
    """Valida o número do sus e se existe algum prontuário com esse número."""
    if not match(Regex.SUS_REGEX, sus_number):
        raise error.SUS_ERROR
    db_return = db.select_sus(sus_number)
    if not db_return:
        raise error.RECORD_N_FOUND_ERROR
    return  1


def validate_search_input(sus_number, patient_name, birth_date):
    """Valida a saída de dados de pesquisa do DB, caso não encontre, retorna um erro."""
    if (not sus_number) and (not patient_name) and (birth_date == 'Ano-Mês-Dia'):
        raise ValueError('ERRO: Nenhum dado informado para a busca!')
    if (len(sus_number) >= 1) and (len(patient_name) >= 1):
        db_return = db.select_sus_name(sus_number, patient_name)
        if not db_return:
            raise error.RECORD_N_FOUND_ERROR
        else:
            return db_return
    if len(sus_number) >= 1:
        db_return = db.select_sus(sus_number)
        if not db_return:
            raise error.RECORD_N_FOUND_ERROR
        else:
            return db_return
    if len(patient_name) >= 1:
        db_return = db.select_name(patient_name)
        if not db_return:
            raise error.RECORD_N_FOUND_ERROR
        else:
            return db_return
    if birth_date != 'Ano-Mês-Dia':
        if match(Regex.DATE_REGEX, birth_date):
            db_return = db.select_birth(birth_date)
            if not db_return:
                raise error.RECORD_N_FOUND_ERROR
            else:
                return db_return
    raise error.EMPTY_INPUT_ERROR


def validate_db_return_all_returned():
    """Valida a saída de dados do DB para prontuários devolvidos, caso não encontre, retorna um erro."""
    db_return = db.select_returned()
    if not db_return:
        raise error.RECORD_N_FOUND_ERROR
    else:
        return db_return


def validate_db_return_all_n_returned():
    """Valida a saida de dados do DB para prontuários não devolvidos, caso não encontre, retorna um erro."""
    db_return = db.select_n_returned()
    if not db_return:
        raise error.RECORD_N_FOUND_ERROR
    else:
        return db_return


def validate_only_date(year, month, day):
    """Valida a data, apenas a data."""
    date = f'{year}-{month}-{day}'
    if date != 'Ano-Mês-Dia':
        if not match(Regex.DATE_REGEX, date):
            raise error.DATE_ERROR
    return 1


def validate_out(sus_number, employee_name, out_date, out_hour):
    """Valida a saída do prontuário."""
    if validate_out_record(sus_number):
        if not match(Regex.SUS_REGEX, sus_number):
            raise error.SUS_ERROR
        if not match(Regex.EMPLOYEE_REGEX, employee_name):
            raise error.EMPLOYEE_ERROR
        if not match(Regex.DATE_REGEX, out_date):
            raise error.DATE_ERROR
        if not match(Regex.HOUR_REGEX, out_hour):
            raise error.HOUR_ERROR
    return 1


def validate_returned(sus_number, employee_name, returned_date, returned_hour):
    """Valida a volta do prontuário."""
    out_date, out_hour = str(db.select_sus(sus_number)[0][7]).split(' ')
    if validate_returned_record(sus_number):
        out_dt = datetime.strptime(out_date, '%Y-%m-%d')
        returned_dt = datetime.strptime(returned_date, '%Y-%m-%d')
        out_hr = datetime.strptime(out_hour, '%H:%M')
        returned_hr = datetime.strptime(returned_hour, '%H:%M')
        if not match(Regex.SUS_REGEX, sus_number):
            raise error.SUS_ERROR
        if not match(Regex.EMPLOYEE_REGEX, employee_name):
            raise error.EMPLOYEE_ERROR
        # Verifica data se não é menor que a data de saida
        if not match(Regex.DATE_REGEX, returned_date):
            raise error.DATE_ERROR
        elif not match(Regex.HOUR_REGEX, returned_hour):
            raise error.HOUR_ERROR
        else:
            if out_dt > returned_dt:
                raise error.MINOR_DATE_ERROR
            elif out_dt == returned_dt:
                if out_hr > returned_hr:
                    raise error.MINOR_HOUR_ERROR
    return 1


def validate_returned_record(sus_number):
    """Verifica se prontuário está fora do arquivo antes de registrar chegada."""
    if movimentacao(sus_number):
        db_values = db.select_sus(sus_number)
        if db_values[0][10]:
            raise error.RETURNED_ERROR
    return 1


def validate_out_record(sus_number):
    """Verifica se o prontuário está no arquivo antes de registrar saída."""
    if not match(Regex.SUS_REGEX, sus_number):
        raise error.SUS_ERROR
    db_values = db.select_sus(sus_number)
    if not db_values[0][10]:
        raise error.NOT_RETURNED_ERROR
    return 1


def movimentacao(sus_number):
    """Verifica se prontuário possui movimentação."""
    if not match(Regex.SUS_REGEX, sus_number):
        raise error.SUS_ERROR
    db_values = db.select_sus(sus_number)
    if db_values[0][10] == -1:
        raise error.NOT_UPDATE_ERROR
    return 1
