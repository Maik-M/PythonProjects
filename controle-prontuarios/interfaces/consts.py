from re import compile


##################
# Keys ########### -----------------------------------------------------------------------------------------------------
##################

class Keys:
    """Classe que guarda todas a keys da interface."""
    L_INPUT_LOGIN = '-login-'
    L_INPUT_SENHA = '-senha-'
    L_BUTTON_ENTRAR = '-entrar-'
    L_BUTTON_CADASTRAR = '-cadastrar-'

    R_INPUT_NOME = '-r_nome-'
    R_INPUT_SUS = '-r_sus-'
    R_INPUT_MAE = '-r_nome_mae-'
    R_INPUT_SEXO_M = '-r_sexo_M-'
    R_INPUT_SEXO_F = '-r_sexo_F-'
    R_INPUT_NASC_DIA = '-r_nascimento_dia-'
    R_INPUT_NASC_MES = '-r_nascimento_mes-'
    R_INPUT_NASC_ANO = '-r_nascimento_ano-'
    R_BUTTON_CADASTRAR = '-r_button_cadastrar-'
    R_BUTTON_LIMPAR = '-r_button_limpar-'

    S_INPUT_SUS = '-s_sus-'
    S_INPUT_NOME = '-s_nome-'
    S_INPUT_NASC_DIA = '-s_nascimento_dia-'
    S_INPUT_NASC_MES = '-s_nascimento_mes-'
    S_INPUT_NASC_ANO = '-s_nascimento_ano-'
    S_BUTTON_BUSCAR = '-s_button_buscar-'
    S_BUTTON_LIMPAR = '-s_button_limpar-'
    S_BUTTON_DEVOLVIDOS = '-s_button_devolvidos-'
    S_BUTTON_N_DEVOLVIDOS = '-s_button_n_devolvidos-'

    IO_INPUT_SUS = '-io_sus-'
    IO_INPUT_FUNCIONARIO = '-io_funcionario-'
    IO_INPUT_DIA = '-io_dia-'
    IO_INPUT_MES = '-io_mes-'
    IO_INPUT_ANO = '-io_ano-'
    IO_INPUT_HORA = '-io_hora-'
    IO_BUTTON_SAIDA = '-io_saida-'
    IO_BUTTON_CHEGADA = '-io_chegada-'
    IO_BUTTON_LIMPAR = '-io_limpar-'

    EDIT_DEL_SEARCH_SUS = '-edit_del_search_sus-'
    EDIT_NOME = '-edit_nome-'
    EDIT_MAE = '-edit_nome_mae-'
    EDIT_SEXO_M = '-edit_sexo_M-'
    EDIT_SEXO_F = '-edit_sexo_F-'
    EDIT_NASC_DIA = '-edit_nascimento_dia-'
    EDIT_NASC_MES = '-edit_nascimento_mes-'
    EDIT_NASC_ANO = '-edit_nascimento_ano-'
    EDIT_BUTTON = '-edit_button-'
    DEL_BUTTON = '-delete_button-'
    EDIT_DEL_LIMPAR_BUTTON = '-edit_delete_limpar-'


    SEARCH_R_OUTPUT = '-search_result_output-'
    SEARCH_R_BUTTON_LIMPAR = '-search_result_limpar-'

    N_ENTREGUE_VALUE = 0
    ENTREGUE_VALUE = 1
    SEM_MOVIMENTO_VALUE = -1
    N_ENTREGUE_STR = 'NÃO ENTREGUE'
    ENTREGUE_STR = 'ENTREGUE'
    SEM_MOVIMENTO_STR = 'SEM MOVIMENTO'
    DB_NONE = '-----'


    MOUTHS = {'Jan': '01', 'Fev': '02', 'Mar': '03', 'Abr': '04', 'Mai': '05', 'Jun': '06',
                    'Jul': '07', 'Ago': '08', 'Set': '09', 'Out': '10', 'Nov': '11', 'Dez': '12', 'Mês': 'Mês'}

###################
# Popup ########### ----------------------------------------------------------------------------------------------------
###################

class Popup:
    """Classe que guarda todas as mensagens de aviso."""
    REGISTRO_MSG = 'Prontuário cadastrado com sucesso!'
    SAIDA_PRONTUARIO_MSG = 'Você deu retirada no pronturio!'
    DEVOLUCAO_PRONTUARIO_MSG = 'Você deu baixa no prontuário. Eles está de volta ao arquivo.'
    EDITAR_MSG = 'Você realmente deseja editar o prontuário?'
    EDITADO_MSG = 'Dados alterados com sucesso!'
    EXCLUIR_MSG = 'Você realmente deseja excluir o prontuário?'
    EXCLUIDO_MSG = 'Prontuário excluído com sucesso!'

    YES = 'Yes'
    NO = 'No'

###################
# ErrorPopup ###### ----------------------------------------------------------------------------------------------------
###################

class ErrorPopup:
    """Classe que guarda todas as mensagens de erro."""
    USUARIO_ERROR = ValueError(19*' '+'ERRO!\nO usuário pode conter: Letras, Números, "-", "_", ".".\nNão aceita espaço e deve conter de 4 à 10 caractéres!')
    SENHA_ERROR = ValueError(19*' '+'ERRO!\nA senha deve conter de 5 à 12 caractéres!')
    USUARIO_INVALIDO_ERROR = ValueError(19*' '+'ERRO!\nUsuário ou senha inválidos.')
    USUARIO_EXISTENTE_ERROR = ValueError(19*' '+'ERRO!\nUsuário já cadastrado!')
    N_ENCONTRADO_ERROR = ValueError(19*' '+'Prontuário não encontrado!')
    SUS_ERROR = ValueError(19*' '+'ERRO!\nO número do SUS só aceita número e deve conter 15 números!')
    NOME_ERROR = ValueError(19*' '+'ERRO!\nO nome do paciente deve conter de 5 à 80 letras e não deve conter números!')
    MAE_ERROR = ValueError('ERRO!\nNome da mãe não é obrigatório, mas caso for preenchido, deve conter de 5 à 80 letras e não conter números!')
    SEXO_ERROR = ValueError(19*' '+'ERRO!\nSexo não informado!')
    NASC_ERROR = ValueError(19*' '+'ERRO!\nData de nascimento não informada ou incorreta!')
    DATA_ERROR = ValueError(19*' '+'ERRO!\nData não informada ou inválida!')
    DATA_MENOR_ERROR = ValueError(19*' '+'ERRO!\nData de chegada pode ser anterior a data de saída!')
    FUNCIONARIO_ERROR = ValueError(19*' '+'ERRO!\nNome do funcionário não informado ou inválido!')
    HORA_ERROR = ValueError(19*' '+'ERRO!\nHora não informada ou inválida!')
    HORA_MENOR_ERROR = ValueError(19*' '+'ERRO!\nDatas iguais! Nesse caso, a hora da chegada não pode ser menor que a da saída!')
    DEVOLVIDO_ERROR = ValueError(19*' '+'ERRO!\nProntuário já foi devolvido! Verifique o número do SUS.')
    NAO_DEVOLVIDO_ERROR = ValueError(19*' '+'ERRO!\nEsse prontuário ainda não foi devolvido! Verifiquei o número do SUS.')
    SEM_MOVIMENTO_ERROR = ValueError(19*' '+'ERRO!\nNão é possível continuar, pois o prontuário ainda está sem movimentação! Verifique se o SUS está correto.')
    INPUT_EM_BRANCO = ValueError(19*' '+'ERRO!\nTodos os campos estão vazios!')

###################
# Regex ###########-----------------------------------------------------------------------------------------------------
###################

class Regex:
    """Classe que guarda toda regra do REGEX."""
    USUARIO_REGEX = compile(r'[a-zA-Z0-9-_.]{4,10}$')
    SENHA_REGEX = compile(r'[a-z A-Z0-9-_@#*]{5,12}$')
    SUS_REGEX = compile(r'[^a-zA-Z à-úÀ-Ú]{15}$')
    NOME_REGEX = compile(r'[a-zA-Z à-úÀ-Ú]{5,80}$')
    SEXO_REGEX = compile(r'[MF]$')
    DATA_REGEX = compile(r'(([1]|[2])([0-9]{3}))-(([0][1-9])|([1][0-2]))-(([0][1-9])|([1-2][0-9])|([3][0-1]))$')
    HORA_REGEX = compile(r'(([0][0-9])|([1][0-9])|([2][1-3])):([0-5][0-9])$')
    FUNCIONARIO_REGEX = compile(r'[a-zA-Z]{2,15}$')
