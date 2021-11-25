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

    F_INPUT_SUS = '-f_sus-'
    F_INPUT_NOME = '-f_nome-'
    F_INPUT_NASC_DIA = '-f_nascimento_dia-'
    F_INPUT_NASC_MES = '-f_nascimento_mes-'
    F_INPUT_NASC_ANO = '-f_nascimento_ano-'
    F_BUTTON_BUSCAR = '-f_button_buscar-'
    F_BUTTON_LIMPAR = '-f_button_limpar-'

    IO_INPUT_SUS = '-io_sus-'
    IO_INPUT_FUNCIONARIO = '-io_funcionario-'
    IO_INPUT_DIA = '-io_dia-'
    IO_INPUT_MES = '-io_mes-'
    IO_INPUT_ANO = '-io_ano-'
    IO_INPUT_HORA = '-io_hora-'
    IO_BUTTON_SAIDA = '-io_saida-'
    IO_BUTTON_CHEGADA = '-io_chegada-'
    IO_BUTTON_LIMPAR = '-io_limpar-'

    OUTPUT_BOARD = '-board-'
    BOARD_BUTTON_DELETAR = '-b_button_deletar-'
    BOARD_BUTTON_EDITAR = '-b_button_editar-'
    BOARD_BUTTON_LIMPAR = '-b_button_limpar-'

###################
# Popup ########### ----------------------------------------------------------------------------------------------------
###################

class Popup:
    """Classe que guarda todas as mensagens de aviso."""
    REGISTRO_MSG = 'Prontuário cadastrado com sucesso!'

###################
# ErrorPopup ###### ----------------------------------------------------------------------------------------------------
###################

class ErrorPopup:
    """Classe que guarda todas as mensagens de erro."""
    USUARIO_ERROR = ValueError(19*' '+'ERRO!\nO usuário pode conter: Lestrar, Números, "-", "_", ".".\nNão aceita espaço e deve conter de 4 à 10 caractéres!')
    SENHA_ERROR = ValueError(19*' '+'ERRO!\nA senha deve conter de 5 à 12 caractéres!')
    USUARIO_INVALIDO_ERROR = ValueError(19*' '+'ERRO!\nUsuário ou senha inválidos.')
    USUARIO_EXISTENTE_ERROR = ValueError('ERRO!\nUsuário já cadastrado!')
    SUS_ERROR = ValueError(19*' '+'ERRO!\nO nome do paciente deve conter de 5 à 80 letras e não deve conter números!')
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
    SEM_MOVIMENTO_ERROR = ValueError(19*' '+'ERRO!\nProntuário ainda sem movimentação!')

###################
# Regex ###########-----------------------------------------------------------------------------------------------------
###################

class Regex:
    """Classe que guarda toda regra do REGEX."""
    USUARIO_REGEX = compile(r'[a-zA-Z0-9-_.]{4,10}$')
    SENHA_REGEX = compile(r'[a-z A-Z0-9-_@#*]{5,12}$')
    SUS_REGEX = compile(r'[^a-zA-Z]{15}$')
    NOME_REGEX = compile(r'[a-zA-Z à-úÀ-Ú]{5,80}$')
    SEXO_REGEX = compile(r'[MF]$')
    DATA_REGEX = compile(r'(([1]|[2])([0-9]{3}))-(([0][1-9])|([1][0-2]))-(([0][1-9])|([1-2][0-9])|([3][0-1]))$')
    HORA_REGEX = compile(r'(([0][0-9])|([1][0-9])|([2][1-3])):([0-5][0-9])$')
    FUNCIONARIO_REGEX = compile(r'[a-zA-Z]{2,15}$')
