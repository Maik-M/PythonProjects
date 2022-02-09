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
            ], title='', background_color='#dcdcdc', expand_x=True, expand_y=True, border_width=0, pad=(0, 0)
            )
            ]
        ]
        self._login_window = sg.Window('Controle de Prontuários',
                                       self._login_layout,
                                       size=(600, 400), background_color='#dcdcdc', finalize=True)

    def make_main_window(self):
        """Faz a tela principal."""
        self._main_layout = [
            [sg.TabGroup(layout=[
                [sg.Tab(title='Cadastrar', key='-tab_cadastro-', layout=[
                    self._registration_frame
                ], background_color='#d1d1d1'),
                 sg.Tab(title='Buscar', key='-tab_busca-', layout=[
                     self._search_frame
                 ], background_color='#d1d1d1'),
                 sg.Tab(title='Saída / Chegada', key='-tab_saida_entrada-', layout=[
                     self._in_out_frame
                 ], background_color='#d1d1d1'),
                 sg.Tab(title='Editar / Excluir', key='-tab_editar_excluir-', layout=[

                 ], background_color='#d1d1d1')
                 ]
            ], key='-tab_group-', expand_x=True, pad=(0, 0), focus_color='#d1d1d1', selected_title_color='#000000',
                selected_background_color='#d1d1d1', background_color='#dcdcdc', border_width=0)],
            [sg.Text('RESULTADO DE BUSCAS',
                     font=('Arial Black', 8), text_color='white', background_color='#00354B', expand_x=True, pad=((0, 0), (15, 0))),
             sg.Button('Limpar',
                       key='-search_result_limpar-', size=(10, 1), pad=((5, 0), (15, 0)))],
            [self._search_result_frame]
        ]
        self._main_window = sg.Window('Controle de Prontuários',
                                      self._main_layout, size=(600, 500), background_color='#dcdcdc', finalize=True)

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

    ################################
    # Return Keys Values Methods ### -----------------------------------------------------------------------------------
    ################################

    def return_register_values(self):
        """Retorna valores da aba registro."""
        sus = str(self.main_values[Keys.R_INPUT_SUS])
        nome = self.main_values[Keys.R_INPUT_NOME]
        sexo = self.__return_sexo()
        dt_nasc = self.__return_formated_date(Keys.R_INPUT_NASC_ANO, Keys.R_INPUT_NASC_MES, Keys.R_INPUT_NASC_DIA)
        mae = self.main_values[Keys.R_INPUT_MAE]
        usuario = self.id_usuario
        if vf.validate_register(sus, nome, sexo, dt_nasc, mae):
            return sus, nome, sexo, dt_nasc, usuario, mae

    def __return_search_values(self):
        sus = self.main_values[Keys.S_INPUT_SUS]
        nome = self.main_values[Keys.S_INPUT_NOME]
        dt_nasc = self.__return_formated_date(Keys.S_INPUT_NASC_ANO, Keys.S_INPUT_NASC_MES, Keys.S_INPUT_NASC_DIA)
        if vf.validate_search(sus, nome, dt_nasc):
            return sus, nome, dt_nasc

    def __return_sexo(self):
        """Verifica qual opção do sexo foi selecionada e retorna o mesmo."""
        if self.main_values[Keys.R_INPUT_SEXO_F]:
            return 'F'
        elif self.main_values[Keys.R_INPUT_SEXO_M]:
            return 'M'

    def __return_formated_date(self, key_ano, key_mes, key_dia):
        """Retorna a data de nascimento formatada."""
        meses = Keys.MOUTHS
        ano = self.main_values[key_ano]
        mes = meses[self.main_values[key_mes]]
        dia = self.main_values[key_dia]
        if vf.validate_data_only(ano, mes, dia):
            date = f'{ano}-{mes}-{dia}'
            return date

    def __return_status(self, status):
        """Retorna status do prontuário de forma legível."""
        if status == Keys.N_ENTREGUE_VALUE:
            return Keys.N_ENTREGUE_STR
        elif status == Keys.ENTREGUE_VALUE:
            return Keys.ENTREGUE_STR
        elif status == Keys.SEM_MOVIMENTO_VALUE:
            return Keys.SEM_MOVIMENTO_STR

    def __return_search_result(self, sus, nome, nascimento, sexo, mae, func_retirada, func_devolucao, dt_hr_r, dt_hr_d, status):
        """Retorna toda string formatada para o usuário."""
        str_status = self.__return_status(status)
        str_dados = 'SUS: {0:<45} FUNCIONARIO RETIRADA: {1}\n' \
                    'NOME: {2:<%d} DATA / HORA RETIRADA: {3}\n' \
                    'DATA DE NASCIMENTO: {4:<%d} FUNCIONARIO DEVOLUÇÃO: {5}\n' \
                    'SEXO: {6:<%d} DATA / HORA DEVOLUÇÃO: {7}\n' \
                    'MÃE: {8:<%d}\n' \
                    'STATUS: {9}\n' \
                    '{10}\n' % (44, 30, 44, 45)
        print(str_dados.format(sus,
                               str(func_retirada).title() if func_retirada is not None else Keys.DB_NONE,
                               str(nome).title(),
                               dt_hr_r if dt_hr_r is not None else Keys.DB_NONE,
                               nascimento,
                               str(func_devolucao).title() if func_devolucao is not None else Keys.DB_NONE,
                               sexo,
                               dt_hr_d if dt_hr_d is not None else Keys.DB_NONE,
                               str(mae).title(),
                               str_status,
                               80 *'-'))

    def return_out_values(self):
        """Valida e retorna valores de saída do prontuário."""
        sus = self.main_values[Keys.IO_INPUT_SUS]
        nome_funcionario = self.main_values[Keys.IO_INPUT_FUNCIONARIO]
        dt_saida = self.__return_formated_date(Keys.IO_INPUT_ANO, Keys.IO_INPUT_MES, Keys.IO_INPUT_DIA)
        hr_saida = self.main_values[Keys.IO_INPUT_HORA]
        usuario = self.id_usuario
        if vf.validate_out(sus, nome_funcionario, dt_saida, hr_saida):
            dt_hr = f'{dt_saida} {hr_saida}'
            return sus, dt_hr, usuario, nome_funcionario

    def return_in_values(self):
        """Valida e retorna valores de entrada do prontuário."""
        sus = self.main_values[Keys.IO_INPUT_SUS]
        nome_funcionario = self.main_values[Keys.IO_INPUT_FUNCIONARIO]
        dt_devolucao = self.__return_formated_date(Keys.IO_INPUT_ANO, Keys.IO_INPUT_MES, Keys.IO_INPUT_DIA)
        hr_devolucao = self.main_values[Keys.IO_INPUT_HORA]
        usuario = self.id_usuario
        if vf.validate_in(sus, nome_funcionario, dt_devolucao, hr_devolucao):
            dt_hr = f'{dt_devolucao} {hr_devolucao}'
            return sus, dt_hr, nome_funcionario, usuario


    ##################
    # Update Methods # -------------------------------------------------------------------------------------------------
    ##################

    def update_search_result(self):
        """Retorna valores da pesquisa pro quadro de resultados."""
        dados = self.__return_search_values()
        db_return = vf.validate_search_input(dados[0], dados[1], dados[2])
        self.clean_search_result()
        for key, value in enumerate(db_return):
            self.__return_search_result(value[0], value[1], value[4], value[3], value[2], value[5], value[6], value[7], value[8], value[10])
        self.clean_search()

    def update_search_result_devolvidos(self):
        """Retorna todos os prontuários já devolvidos."""
        db_return = vf.validate_db_return_devolvidos()
        self.clean_search_result()
        for key, value in enumerate(db_return):
            self.__return_search_result(value[0], value[1], value[4], value[3], value[2], value[5], value[6], value[7], value[8], value[10])
        self.clean_search()

    def update_search_result_n_devolvidos(self):
        """Retorna todos os prontuários não devolvidos."""
        db_return = vf.validate_db_return_n_devolvidos()
        self.clean_search_result()
        for key, value in enumerate(db_return):
            self.__return_search_result(value[0], value[1], value[4], value[3], value[2], value[5], value[6], value[7], value[8], value[10])
        self.clean_search()

    # Clean var values
    def clean_search_result(self):
        """Limpa quadro de resultado de pesquisas."""
        self._main_window[Keys.SEARCH_R_OUTPUT].update(value='')

    def clean_login(self):
        """Limpa valores do Login"""
        self._login_window[Keys.L_INPUT_LOGIN].update(value='')
        self._login_window[Keys.L_INPUT_SENHA].update(value='')

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

    def clean_search(self):
        """Limpa os valores das variáveis na janela busca."""
        self._main_window[Keys.S_INPUT_SUS].update(value='')
        self._main_window[Keys.S_INPUT_NOME].update(value='')
        self._main_window[Keys.S_INPUT_NASC_DIA].update(value='Dia')
        self._main_window[Keys.S_INPUT_NASC_MES].update(value='Mês')
        self._main_window[Keys.S_INPUT_NASC_ANO].update(value='Ano')

    def clean_io(self):
        """Limpa os valores da janela Entrada / Saída."""
        self._main_window[Keys.IO_INPUT_SUS].update(value='')
        self._main_window[Keys.IO_INPUT_FUNCIONARIO].update(value='')
        self._main_window[Keys.IO_INPUT_DIA].update(value='Dia')
        self._main_window[Keys.IO_INPUT_MES].update(value='Mês')
        self._main_window[Keys.IO_INPUT_ANO].update(value='Ano')
        self._main_window[Keys.IO_INPUT_HORA].update(value='')


if __name__ == '__main__':
    start = Interface()
    start.make_main_window()
    while True:
        start.input_main_values()
        if start.main_events == Keys.S_BUTTON_BUSCAR:
            pass
        if start.main_events == sg.WIN_CLOSED:
            break
