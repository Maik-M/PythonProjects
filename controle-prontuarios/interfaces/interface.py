import PySimpleGUI as sg
import funcs.validate_funcs as vf
from interfaces.consts import Keys
from interfaces.login_interface_lines import LoginInterfaceLines
from interfaces.main_interface_lines import MainInterfaceLines

##################
# Class ########## -----------------------------------------------------------------------------------------------------
##################

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

    #######################
    # Getters and Setters # --------------------------------------------------------------------------------------------
    #######################

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

    ###################
    # Windows ######### ------------------------------------------------------------------------------------------------
    ###################

    def make_login_window(self):
        """Faz a tela de login."""
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
                                       finalize=True)

    def make_main_window(self):
        """Faz a tela principal."""
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
                focus_color='#d1d1d1',
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
                                      finalize=True)

    @staticmethod
    def make_popup(msg):
        """Faz a janela de popup de aviso."""
        return sg.PopupOK(msg, font=('Arial Black', 12), background_color='#f9f9f9', text_color='#00345B',
                          button_color='#ff5858', line_width=27, no_titlebar=True)

    @staticmethod
    def make_error_popup(error):
        """Faz a janela de popup de erro."""
        return sg.PopupOK(error, font=('Arial Black', 12), background_color='#f9f9f9', text_color='#ff5858',
                          button_color='#ff5858', line_width=27, no_titlebar=True)


    ###########################
    # Input Values and Events # ----------------------------------------------------------------------------------------
    ###########################

    def input_login_values(self):
        """Recebe os valores de input do login."""
        self.__login_events, self.__login_values = self._login_window.Read()

    def input_main_values(self):
        """Recebe os valores de input da tela principal."""
        self.__main_events, self.__main_values = self._main_window.Read()

    ###########################
    # Return Values Methods ### ----------------------------------------------------------------------------------------
    ###########################

    def return_reg(self):
        """Retorna valores da aba registro."""
        sus = str(self.main_values[Keys.R_INPUT_SUS])
        nome = self.main_values[Keys.R_INPUT_NOME]
        sexo = self.return_sexo()
        dt_nasc = self.return_formated_nasc()
        mae = self.main_values[Keys.R_INPUT_MAE]
        usuario = self.id_usuario
        if vf.validate_register(sus, nome, sexo, dt_nasc, mae):
            return sus, nome, sexo, dt_nasc, usuario, mae

    def return_sexo(self):
        """Verifica qual opção do sexo foi selecionada e retorna o mesmo."""
        if self.main_values[Keys.R_INPUT_SEXO_F]:
            return 'F'
        elif self.main_values[Keys.R_INPUT_SEXO_M]:
            return 'M'

    def return_formated_nasc(self):
        """Retorna a data formatada."""
        meses = {'Jan': '01', 'Fev': '02', 'Mar': '03', 'Abr': '04', 'Mai': '05', 'Jun': '06',
                    'Jul': '07', 'Ago': '08', 'Set': '09', 'Out': '10', 'Nov': '11', 'Dez': '12'}
        ano = self.main_values[Keys.R_INPUT_NASC_ANO]
        mes = meses[self.main_values[Keys.R_INPUT_NASC_MES]]
        dia = self.main_values[Keys.R_INPUT_NASC_DIA]
        dt_nasc = f'{ano}-{mes}-{dia}'
        return dt_nasc

    ##################
    # Update Methods # -------------------------------------------------------------------------------------------------
    ##################

    def clean_tab_cadastro(self):
        """Limpa todos os campos da tab cadastro."""
        self._main_window[Keys.R_INPUT_SUS].update(value='')
        self._main_window[Keys.R_INPUT_NOME].update(value='')
        self._main_window[Keys.R_INPUT_MAE].update(value='')
        self._main_window[Keys.R_INPUT_SEXO_M].update(value=False)
        self._main_window[Keys.R_INPUT_SEXO_F].update(value=False)
        self._main_window[Keys.R_INPUT_NASC_DIA].update(value='Dia')
        self._main_window[Keys.R_INPUT_NASC_MES].update(value='Mês')
        self._main_window[Keys.R_INPUT_NASC_ANO].update(value='Ano')

    def update_main_window(self):
        """Atualiza as valores da tela principal."""
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
