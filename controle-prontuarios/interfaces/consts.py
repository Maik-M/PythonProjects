from re import compile


##################
# Keys ########### -----------------------------------------------------------------------------------------------------
##################

class Keys:
    """Classe que guarda todas a keys da interface."""
    L_LOGIN_INPUT = '-login-'
    L_PASSW_INPUT = '-password-'
    L_LOGIN_BUTTON = '-login_button-'
    L_NEW_USER_BUTTON = '-new_user_button-'

    MAIN_GREETINGS = '-main_greetings-'

    NEW_U_NAME = '-new_user_name-'
    NEW_U_LOGIN = '-new_user_login-'
    NEW_U_PASSWORD = '-new_user_password-'
    NEW_U_CONFIRM_PASS = '-new_user_confirm_password-'
    NEW_U_OK_BUTTON = '-new_user_ok_button-'
    NEW_U_CANCEL_BUTTON = '-new_user_cancel_button-'

    R_NAME_INPUT = '-r_name-'
    R_SUS_INPUT = '-r_sus-'
    R_MOTHER_INPUT = '-r_mother-'
    R_M_GENDER_INPUT = '-r_m_gender-'
    R_F_GENDER_INPUT = '-r_f_gender-'
    R_DAY_BIRTH_INPUT = '-r_day_birth-'
    R_MONTH_BIRTH_INPUT = '-r_month_birth-'
    R_YEAR_BIRTH_INPUT = '-r_year_birth-'
    R_REGISTER_BUTTON = '-r_register_button-'
    R_CLEAN_BUTTON = '-r_clean_button-'

    S_SUS_INPUT = '-s_sus-'
    S_NAME_INPUT = '-s_name-'
    S_DAY_BIRTH_INPUT = '-s_day_birth-'
    S_MONTH_BIRTH_INPUT = '-s_month_birth-'
    S_YEAR_BIRTH_INPUT = '-s_year_birth-'
    S_SEARCH_BUTTON = '-s_search_button-'
    S_CLEAN_BUTTON = '-s_clean_button-'
    S_RETURNED_BUTTON = '-s_returned_button-'
    S_N_RETURNED_BUTTON = '-s_n_returned_button-'

    R_O_SUS_INPUT = '-r_o_sus-'
    R_O_EMPLOYEE_INPUT = '-r_o_employee-'
    R_O_DAY_INPUT = '-r_o_day-'
    R_O_MONTH_INPUT = '-r_o_month-'
    R_O_YEAR_INPUT = '-r_o_year-'
    R_O_HOUR_INPUT = '-r_o_hour-'
    R_O_OUT_BUTTON = '-r_o_out_button-'
    R_O_RETURNED_BUTTON = '-r_o_returned_button-'
    R_O_CLEAN_BUTTON = '-r_o_clean_button-'

    EDIT_DEL_SEARCH_SUS = '-edit_del_search_sus-'
    EDIT_NAME_INPUT = '-edit_name-'
    EDIT_MOTHER_INPUT = '-edit_mother-'
    EDIT_M_GENDER_INPUT = '-edit_m_gender-'
    EDIT_F_GENDER_INPUT = '-edit_f_gender-'
    EDIT_DAY_BIRTH_INPUT = '-edit_day_birth-'
    EDIT_MONTH_BIRTH_INPUT = '-edit_month_birth-'
    EDIT_YEAR_BIRTH_INPUT = '-edit_year_birth-'
    EDIT_BUTTON = '-edit_button-'
    DEL_BUTTON = '-delete_button-'
    EDIT_DEL_CLEAN_BUTTON = '-edit_delete_clean_button-'


    SEARCH_R_OUTPUT = '-search_result_output-'
    SEARCH_R_CLEAN_BUTTON = '-clean_search_result-'

    N_RETURNED_VALUE = 0
    RETURNED_VALUE = 1
    N_UPDATE_VALUE = -1
    N_RETURNED_MSG = 'NÃO ENTREGUE'
    RETURNED_MSG = 'ENTREGUE'
    N_UPDATE_MSG = 'SEM MOVIMENTO'
    DB_NONE = '-----'


    MONTHS = {'Jan': '01', 'Fev': '02', 'Mar': '03', 'Abr': '04', 'Mai': '05', 'Jun': '06',
                    'Jul': '07', 'Ago': '08', 'Set': '09', 'Out': '10', 'Nov': '11', 'Dez': '12', 'Mês': 'Mês'}

###################
# Popup ########### ----------------------------------------------------------------------------------------------------
###################

class Popup:
    """Classe que guarda todas as mensagens de aviso."""
    NEW_USER_AGREE_MSG = 'Você deseja realmente cadastrar um novo usuário?'
    NEW_USER_MSG = 'Usuário cadastrado com sucesso! Agora, faça o login.'
    REGISTER_MSG = 'Prontuário cadastrado com sucesso!'
    RECORD_OUT_MSG = 'Você deu retirada no pronturio!'
    RECORD_RETURNED_MSG = 'Você deu baixa no prontuário. Eles está de volta ao arquivo.'
    EDIT_MSG = 'Você realmente deseja editar o prontuário?'
    EDITED_MSG = 'Dados alterados com sucesso!'
    DELETE_MSG = 'Você realmente deseja excluir o prontuário?'
    DELETED_MSG = 'Prontuário excluído com sucesso!'

    YES = 'Yes'
    NO = 'No'

###################
# ErrorPopup ###### ----------------------------------------------------------------------------------------------------
###################

class ErrorPopup:
    """Classe que guarda todas as mensagens de erro."""
    SHORT_NAME_ERROR = ValueError(19 * ' ' + 'ERRO!\nNome do usuário muito pequeno! Por favor, digite o nome completo.')
    USER_ERROR = ValueError(19 * ' ' + 'ERRO!\nO usuário pode conter: Letras, Números, "-", "_", ".".\nNão aceita espaço e deve conter de 4 à 10 caractéres!')
    PASSW_ERROR = ValueError(19 * ' ' + 'ERRO!\nA senha deve conter de 5 à 12 caractéres!')
    PASSW_ERROR_2 = ValueError(19 * ' ' + 'ERRO!\nAs senhas digitadas não conferem! Tente novamente')
    INVALID_USER_ERROR = ValueError(19 * ' ' + 'ERRO!\nUsuário ou senha inválidos.')
    USER_EXIST_ERROR = ValueError(19 * ' ' + 'ERRO!\nUsuário já cadastrado! Tente outro.')
    USER_N_FOUND_ERROR = ValueError(19 * ' ' + 'ERRO!\nUsuário não encontrado! Faça o login e tente novamente.')
    RECORD_N_FOUND_ERROR = ValueError(19 * ' ' + 'Prontuário não encontrado!')
    SUS_ERROR = ValueError(19*' '+'ERRO!\nO número do SUS só aceita número e deve conter 15 números!')
    NAME_ERROR = ValueError(19 * ' ' + 'ERRO!\nO nome do paciente deve conter de 5 à 80 letras e não deve conter números!')
    MOTHER_ERROR = ValueError('ERRO!\nNome da mãe não é obrigatório, mas caso for preenchido, deve conter de 5 à 80 letras e não conter números!')
    GENDER_ERROR = ValueError(19 * ' ' + 'ERRO!\nSexo não informado!')
    BIRTH_ERROR = ValueError(19 * ' ' + 'ERRO!\nData de nascimento não informada ou incorreta!')
    DATE_ERROR = ValueError(19 * ' ' + 'ERRO!\nData não informada ou inválida!')
    MINOR_DATE_ERROR = ValueError(19 * ' ' + 'ERRO!\nData de chegada pode ser anterior a data de saída!')
    EMPLOYEE_ERROR = ValueError(19 * ' ' + 'ERRO!\nNome do funcionário não informado ou inválido!')
    HOUR_ERROR = ValueError(19 * ' ' + 'ERRO!\nHora não informada ou inválida!')
    MINOR_HOUR_ERROR = ValueError(19 * ' ' + 'ERRO!\nDatas iguais! Nesse caso, a hora da chegada não pode ser menor que a da saída!')
    RETURNED_ERROR = ValueError(19 * ' ' + 'ERRO!\nProntuário já foi devolvido! Verifique o número do SUS.')
    NOT_RETURNED_ERROR = ValueError(19 * ' ' + 'ERRO!\nEsse prontuário ainda não foi devolvido! Verifiquei o número do SUS.')
    NOT_UPDATE_ERROR = ValueError(19 * ' ' + 'ERRO!\nNão é possível continuar, pois o prontuário ainda está sem movimentação! Verifique se o SUS está correto.')
    EMPTY_INPUT_ERROR = ValueError(19 * ' ' + 'ERRO!\nTodos os campos estão vazios!')

###################
# Regex ###########-----------------------------------------------------------------------------------------------------
###################

class Regex:
    """Classe que guarda toda regra do REGEX."""
    USER_REGEX = compile(r'[a-zA-Z0-9-_.]{4,10}$')
    PASSWORD_REGEX = compile(r'[a-z A-Z0-9-_@#*]{5,12}$')
    SUS_REGEX = compile(r'[^a-zA-Z à-úÀ-Ú]{15}$')
    NAME_REGEX = compile(r'[a-zA-Z à-úÀ-Ú]{5,80}$')
    GENDER_REGEX = compile(r'[MF]$')
    DATE_REGEX = compile(r'(([1]|[2])([0-9]{3}))-(([0][1-9])|([1][0-2]))-(([0][1-9])|([1-2][0-9])|([3][0-1]))$')
    HOUR_REGEX = compile(r'(([0][0-9])|([1][0-9])|([2][1-3])):([0-5][0-9])$')
    EMPLOYEE_REGEX = compile(r'[a-zA-Z]{2,15}$')
