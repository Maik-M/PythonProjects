import PySimpleGUI as sg
from login_interface_lines import LoginInterfaceLines
from main_interface_lines import MainInterfaceLines

# Keys -----------------------------------------------------------------------------------------------------------------
R_INPUT_NOME = '-r_nome-'
R_INPUT_SUS = '-r_sus-'
R_INPUT_MAE = '-r_nome_mae-'
R_INPUT_SEXO = 'SEXO'
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
# ----------------------------------------------------------------------------------------------------------------------


class Interface(LoginInterfaceLines, MainInterfaceLines):
    """Monta todas as telas."""

    def __init__(self):
        LoginInterfaceLines.__init__(self)
        MainInterfaceLines.__init__(self)

        # Variáveis
        self.__login_events = None
        self.__login_values = None
        self.__main_events = None
        self.__main_values = None

    # Getters ----------------------------------------------------------------------------------------------------------
    @property
    def login_events(self):
        return self.__login_events

    @property
    def login_values(self):
        return self.__login_values

    @property
    def main_events(self):
        return self.__main_events

    @property
    def main_values(self):
        return self.__main_values

    # Windows ----------------------------------------------------------------------------------------------------------
    def make_login_window(self):
        self._login_layout = [
            [sg.Frame(layout=[
                [self._greetings_login_column],
                [self._credentials_login_column],
                [self._login_button_entrar_column],
                [self._login_button_cadastrar_column],
                [self._developer_login_column]
            ], title='',
                background_color='#dcdcdc',
                expand_x=True,
                expand_y=True,
                border_width=0,
                pad=(0, 0)
            )
            ]
        ]
        self._login_window = sg.Window('Controle de Prontuários',
                                       self._login_layout,
                                       size=(600, 400),
                                       background_color='#dcdcdc',
                                       use_default_focus=False,
                                       finalize=True)

    def make_main_window(self):
        self._main_layout = [
            [sg.TabGroup(layout=[
                [sg.Tab(title='Cadastrar', key='-tab_cadastro-', layout=[
                    self._registration_frame
                ], background_color='#d1d1d1'),
                 sg.Tab(title='Buscar', key='-tab_busca-', layout=[
                     self._find_frame
                 ], background_color='#d1d1d1'),
                 sg.Tab(title='Saída / Entrada', key='-tab_saida_entrada-', layout=[
                     self._in_out_frame
                 ], background_color='#d1d1d1')
                 ]
            ], key='-tab_group-',
                expand_x=True,
                pad=(0, 0),
                selected_title_color='#000000',
                selected_background_color='#d1d1d1',
                background_color='#dcdcdc',
                border_width=0)],
            [self._board_column,
             self._board_buttons_column]
        ]
        self._main_window = sg.Window('Controle de Prontuários',
                                      self._main_layout,
                                      size=(600, 400),
                                      background_color='#dcdcdc',
                                      use_default_focus=False,
                                      finalize=True)

    # Input Values and Events ------------------------------------------------------------------------------------------
    def input_login_values(self):
        self.__login_events, self.__login_values = self._login_window.Read()

    def input_main_values(self):
        self.__main_events, self.__main_values = self._main_window.Read()

    # Update Methods --------------------------------------------------------------------------------------------------
    def update_main_window(self):
        pass


if __name__ == '__main__':
    start = Interface()
    start.make_login_window()
    start.input_login_values()
    if start.login_events == '-entrar-':
        start.login_window.close()
        start.make_main_window()
        while True:
            start.input_main_values()
            if start.main_events == R_BUTTON_CADASTRAR:
                print(start.main_values)
            if start.main_events == sg.WINDOW_CLOSED:
                break
