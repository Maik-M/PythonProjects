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

    R_O_SUS_INPUT = '-ro_sus-'
    R_O_EMPLOYEE_INPUT = '-ro_employee-'
    R_O_DAY_INPUT = '-ro_day-'
    R_O_MONTH_INPUT = '-ro_month-'
    R_O_YEAR_INPUT = '-ro_year-'
    R_O_HOUR_INPUT = '-ro_hour-'
    R_O_OUT_BUTTON = '-out_button-'
    R_O_RETURNED_BUTTON = '-returned_button-'
    R_O_CLEAN_BUTTON = '-ro_clean_button-'

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
    N_RETURNED_MSG = 'N??O ENTREGUE'
    RETURNED_MSG = 'ENTREGUE'
    N_UPDATE_MSG = 'SEM MOVIMENTO'
    DB_NONE = '-----'


    MONTHS = {'Jan': '01', 'Fev': '02', 'Mar': '03', 'Abr': '04', 'Mai': '05', 'Jun': '06',
                    'Jul': '07', 'Ago': '08', 'Set': '09', 'Out': '10', 'Nov': '11', 'Dez': '12', 'M??s': 'M??s'}

###################
# Popup ########### ----------------------------------------------------------------------------------------------------
###################

class Popup:
    """Classe que guarda todas as mensagens de aviso."""
    NEW_USER_AGREE_MSG = 'Voc?? deseja realmente cadastrar um novo usu??rio?'
    NEW_USER_MSG = 'Usu??rio cadastrado com sucesso! Agora, fa??a o login.'
    REGISTER_MSG = 'Prontu??rio cadastrado com sucesso!'
    RECORD_OUT_MSG = 'Voc?? deu retirada no pronturio!'
    RECORD_RETURNED_MSG = 'Voc?? deu baixa no prontu??rio. Eles est?? de volta ao arquivo.'
    EDIT_MSG = 'Voc?? realmente deseja editar o prontu??rio?'
    EDITED_MSG = 'Dados alterados com sucesso!'
    DELETE_MSG = 'Voc?? realmente deseja excluir o prontu??rio?'
    DELETED_MSG = 'Prontu??rio exclu??do com sucesso!'

    YES = 'Yes'
    NO = 'No'

###################
# ErrorPopup ###### ----------------------------------------------------------------------------------------------------
###################

class ErrorPopup:
    """Classe que guarda todas as mensagens de erro."""
    SHORT_NAME_ERROR = ValueError(19 * ' ' + 'ERRO!\nNome do usu??rio muito pequeno! Por favor, digite o nome completo.')
    USER_ERROR = ValueError(19 * ' ' + 'ERRO!\nO usu??rio pode conter: Letras, N??meros, "-", "_", ".".\nN??o aceita espa??o e deve conter de 4 ?? 10 caract??res!')
    PASSW_ERROR = ValueError(19 * ' ' + 'ERRO!\nA senha deve conter de 5 ?? 12 caract??res!')
    PASSW_ERROR_2 = ValueError(19 * ' ' + 'ERRO!\nAs senhas digitadas n??o conferem! Tente novamente')
    INVALID_USER_ERROR = ValueError(19 * ' ' + 'ERRO!\nUsu??rio ou senha inv??lidos.')
    USER_EXIST_ERROR = ValueError(19 * ' ' + 'ERRO!\nUsu??rio j?? cadastrado! Tente outro.')
    USER_N_FOUND_ERROR = ValueError(19 * ' ' + 'ERRO!\nUsu??rio n??o encontrado! Fa??a o login e tente novamente.')
    RECORD_N_FOUND_ERROR = ValueError(19 * ' ' + 'Prontu??rio n??o encontrado!')
    SUS_ERROR = ValueError(19*' '+'ERRO!\nO n??mero do SUS s?? aceita n??mero e deve conter 15 n??meros!')
    NAME_ERROR = ValueError(19 * ' ' + 'ERRO!\nO nome do paciente deve conter de 5 ?? 80 letras e n??o deve conter n??meros!')
    MOTHER_ERROR = ValueError('ERRO!\nNome da m??e n??o ?? obrigat??rio, mas caso for preenchido, deve conter de 5 ?? 80 letras e n??o conter n??meros!')
    GENDER_ERROR = ValueError(19 * ' ' + 'ERRO!\nSexo n??o informado!')
    BIRTH_ERROR = ValueError(19 * ' ' + 'ERRO!\nData de nascimento n??o informada ou incorreta!')
    DATE_ERROR = ValueError(19 * ' ' + 'ERRO!\nData n??o informada ou inv??lida!')
    MINOR_DATE_ERROR = ValueError(19 * ' ' + 'ERRO!\nData de chegada pode ser anterior a data de sa??da!')
    EMPLOYEE_ERROR = ValueError(19 * ' ' + 'ERRO!\nNome do funcion??rio n??o informado ou inv??lido!')
    HOUR_ERROR = ValueError(19 * ' ' + 'ERRO!\nHora n??o informada ou inv??lida!')
    MINOR_HOUR_ERROR = ValueError(19 * ' ' + 'ERRO!\nDatas iguais! Nesse caso, a hora da chegada n??o pode ser menor que a da sa??da!')
    RETURNED_ERROR = ValueError(19 * ' ' + 'ERRO!\nProntu??rio j?? foi devolvido! Verifique o n??mero do SUS.')
    NOT_RETURNED_ERROR = ValueError(19 * ' ' + 'ERRO!\nEsse prontu??rio ainda n??o foi devolvido! Verifiquei o n??mero do SUS.')
    NOT_UPDATE_ERROR = ValueError(19 * ' ' + 'ERRO!\nN??o ?? poss??vel continuar, pois o prontu??rio ainda est?? sem movimenta????o! Verifique se o SUS est?? correto.')
    EMPTY_INPUT_ERROR = ValueError(19 * ' ' + 'ERRO!\nTodos os campos est??o vazios!')

###################
# Regex ###########-----------------------------------------------------------------------------------------------------
###################

class Regex:
    """Classe que guarda toda regra do REGEX."""
    USER_REGEX = compile(r'[a-zA-Z0-9-_.]{4,10}$')
    PASSWORD_REGEX = compile(r'[a-z A-Z0-9-_@#*]{5,12}$')
    SUS_REGEX = compile(r'[^a-zA-Z ??-????-??]{15}$')
    NAME_REGEX = compile(r'[a-zA-Z ??-????-??]{5,80}$')
    GENDER_REGEX = compile(r'[MF]$')
    DATE_REGEX = compile(r'(([1]|[2])([0-9]{3}))-(([0][1-9])|([1][0-2]))-(([0][1-9])|([1-2][0-9])|([3][0-1]))$')
    HOUR_REGEX = compile(r'(([0][0-9])|([1][0-9])|([2][1-3])):([0-5][0-9])$')
    EMPLOYEE_REGEX = compile(r'[a-z A-Z]{2,50}$')
