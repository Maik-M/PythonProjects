import PySimpleGUI as sg
import funcs.validate_funcs as vf
from interfaces.consts import Keys
from interfaces.login_interface_lines import LoginInterfaceLines
from interfaces.new_user_interface_lines import NewUserInterfaceLines
from interfaces.main_interface_lines import MainInterfaceLines

##################
# Class ########## -----------------------------------------------------------------------------------------------------
##################

class Interface(LoginInterfaceLines, NewUserInterfaceLines, MainInterfaceLines):
    """Monta todas as telas."""

    def __init__(self):
        LoginInterfaceLines.__init__(self)
        NewUserInterfaceLines.__init__(self)
        MainInterfaceLines.__init__(self)

        # Variáveis
        self.__login_events = None
        self.__login_values = None
        self.__new_user_events = None
        self.__new_user_values = None
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
    def new_user_events(self):
        return self.__new_user_events

    @property
    def new_user_values(self):
        return self.__new_user_values

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
        self._login_window = sg.Window('Controle de Prontuários - LOGIN',
                                       self._login_layout,
                                       size=(600, 400), titlebar_icon='./img/medicine-icon.png/', use_custom_titlebar=True,
                                       titlebar_background_color='white', titlebar_text_color='#00354B', titlebar_font=('Arial Black', 10),
                                       background_color='#dcdcdc', finalize=True)

    def make_new_user_window(self):
        """Faz a tela de cadastro de novo usuário."""
        self._new_user_layout = [
            [sg.Frame(layout=[
                [self._new_user_title_column],
                [self._new_user_credential_column],
                [self._new_user_buttons_column]
            ], title='', background_color='#dcdcdc', expand_x=True, expand_y=True, border_width=0, pad=(0, 0)
            )
            ]
        ]
        self._new_user_window = sg.Window('Controle de Prontuários - NOVO USUÁRIO',
                                          self._new_user_layout,
                                          size=(600, 400), titlebar_icon='./img/medicine-icon.png/', use_custom_titlebar=True,
                                          titlebar_background_color='white', titlebar_text_color='#00354B', titlebar_font=('Arial Black', 10),
                                          background_color='#dcdcdc', finalize=True)

    def make_main_window(self):
        """Faz a tela principal."""
        self._main_layout = [
            [self._main_greetings_column],
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
                     self._edit_delete_frame
                 ], background_color='#d1d1d1')
                 ]
            ], key='-tab_group-', expand_x=True, pad=(5, (5, 0)), focus_color='#d1d1d1', selected_title_color='#000000',
                selected_background_color='#d1d1d1', background_color='#dcdcdc', border_width=0)],
            [sg.Text('RESULTADO DE BUSCAS',
                     font=('Arial Black', 8), text_color='white', background_color='#00354B', expand_x=True, pad=((5, 5), (15, 0))),
             sg.Button('Limpar',
                       key='-clean_search_result-', size=(10, 1), pad=((5, 5), (15, 0)))],
            [self._search_result_frame]
        ]
        self._main_window = sg.Window('Controle de Prontuários',
                                      self._main_layout, size=(600, 520), titlebar_icon='./img/medicine-icon.png/', use_custom_titlebar=True,
                                      titlebar_background_color='white', titlebar_text_color='#00354B', titlebar_font=('Arial Black', 10),
                                      background_color='#dcdcdc', finalize=True)

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

    @staticmethod
    def make_warning_popup(msg):
        """Faz janela de popup de aviso de confirmação."""
        return sg.PopupYesNo(msg, font=('Arial Black', 12), background_color='#f9f9f9', text_color='#00345B',
                             button_color='#ff5858', line_width=27, no_titlebar=True)


    ###########################
    # Input Values and Events # ----------------------------------------------------------------------------------------
    ###########################

    def input_login_values(self):
        """Recebe os valores de input do login."""
        self.__login_events, self.__login_values = self._login_window.Read()

    def input_new_user_values(self):
        """Recebe os valores de input da tela novo usuário."""
        self.__new_user_events, self.__new_user_values = self._new_user_window.Read()

    def input_main_values(self):
        """Recebe os valores de input da tela principal."""
        self.__main_events, self.__main_values = self._main_window.Read()

    ################################
    # Return Keys Values Methods ### -----------------------------------------------------------------------------------
    ################################

    def return_new_user_values(self):
        user_name = self.new_user_values[Keys.NEW_U_NAME]
        user = self.new_user_values[Keys.NEW_U_LOGIN]
        password = self.new_user_values[Keys.NEW_U_PASSWORD]
        re_password = self.new_user_values[Keys.NEW_U_CONFIRM_PASS]
        if vf.validate_new_user(user_name, user, password, re_password):
            return user_name, user, password

    def return_register_values(self):
        """Retorna valores da aba registro."""
        sus_number = str(self.main_values[Keys.R_SUS_INPUT])
        patient_name = self.main_values[Keys.R_NAME_INPUT]
        gender = self.__return_gender_value(Keys.R_F_GENDER_INPUT, Keys.R_M_GENDER_INPUT)
        birth_date = self.__return_formated_date(Keys.R_YEAR_BIRTH_INPUT, Keys.R_MONTH_BIRTH_INPUT, Keys.R_DAY_BIRTH_INPUT)
        mother = self.main_values[Keys.R_MOTHER_INPUT]
        user_id = self.user_id
        if vf.validate_register(sus_number, patient_name, gender, birth_date, mother):
            return sus_number, patient_name, gender, birth_date, user_id, mother

    def __return_search_values(self):
        sus_number = self.main_values[Keys.S_SUS_INPUT]
        patient_name = self.main_values[Keys.S_NAME_INPUT]
        birth_date = self.__return_formated_date(Keys.S_YEAR_BIRTH_INPUT, Keys.S_MONTH_BIRTH_INPUT, Keys.S_DAY_BIRTH_INPUT)
        if vf.validate_search(sus_number, patient_name, birth_date):
            return sus_number, patient_name, birth_date

    def __return_gender_value(self, f_key, m_key):
        """Verifica qual opção do gender foi selecionada e retorna o mesmo."""
        if self.main_values[f_key]:
            return 'F'
        elif self.main_values[m_key]:
            return 'M'

    def __return_formated_date(self, year_key, month_key, day_key):
        """Retorna a data de nascimento formatada."""
        months = Keys.MONTHS
        year = self.main_values[year_key]
        month = months[self.main_values[month_key]]
        day = self.main_values[day_key]
        if vf.validate_only_date(year, month, day):
            date = f'{year}-{month}-{day}'
            return date

    def __return_status(self, record_status):
        """Retorna status do prontuário de forma legível."""
        if record_status == Keys.N_RETURNED_VALUE:
            return Keys.N_RETURNED_MSG
        elif record_status == Keys.RETURNED_VALUE:
            return Keys.RETURNED_MSG
        elif record_status == Keys.N_UPDATE_VALUE:
            return Keys.N_UPDATE_MSG

    def __return_search_result(self, sus_number, name, birth, gender, mother, employee_out, employee_returned, dt_hr_o, dt_hr_r, record_status, user):
        """Retorna toda string formatada para o usuário."""
        status_str = self.__return_status(record_status)
        data_str = 'SUS: {0:<45} FUNCIONARIO RETIRADA: {1}\n' \
                    'NOME: {2:<%d} DATA / HORA RETIRADA: {3}\n' \
                    'DATA DE NASCIMENTO: {4:<%d} FUNCIONARIO DEVOLUÇÃO: {5}\n' \
                    'SEXO: {6:<%d} DATA / HORA DEVOLUÇÃO: {7}\n' \
                    'MÃE: {8:<%d} MODIFICADO POR: {9}\n' \
                    'STATUS: {10}\n' \
                    '{11}\n' % (44, 30, 44, 45)
        print(data_str.format(sus_number,
                              str(employee_out).title() if employee_out is not None else Keys.DB_NONE,
                              str(name).title(),
                              dt_hr_o if dt_hr_o is not None else Keys.DB_NONE,
                              birth,
                              str(employee_returned).title() if employee_returned is not None else Keys.DB_NONE,
                              gender,
                              dt_hr_r if dt_hr_r is not None else Keys.DB_NONE,
                              str(mother).title(),
                              str(user).title(),
                              status_str,
                              80 *'-'))

    def return_out_values(self):
        """Valida e retorna valores de saída do prontuário."""
        sus_number = self.main_values[Keys.R_O_SUS_INPUT]
        employee_name = self.main_values[Keys.R_O_EMPLOYEE_INPUT]
        out_date = self.__return_formated_date(Keys.R_O_YEAR_INPUT, Keys.R_O_MONTH_INPUT, Keys.R_O_DAY_INPUT)
        out_hour = self.main_values[Keys.R_O_HOUR_INPUT]
        user = self.user_id
        if vf.validate_out(sus_number, employee_name, out_date, out_hour):
            dt_hr = f'{out_date} {out_hour}'
            return sus_number, dt_hr, user, employee_name

    def return_returned_values(self):
        """Valida e retorna valores de entrada do prontuário."""
        sus_number = self.main_values[Keys.R_O_SUS_INPUT]
        employee_name = self.main_values[Keys.R_O_EMPLOYEE_INPUT]
        returned_date = self.__return_formated_date(Keys.R_O_YEAR_INPUT, Keys.R_O_MONTH_INPUT, Keys.R_O_DAY_INPUT)
        returned_hour = self.main_values[Keys.R_O_HOUR_INPUT]
        user = self.user_id
        if vf.validate_returned(sus_number, employee_name, returned_date, returned_hour):
            dt_hr = f'{returned_date} {returned_hour}'
            return sus_number, dt_hr, employee_name, user

    def return_edit_values(self):
        sus_number = self.main_values[Keys.EDIT_DEL_SEARCH_SUS]
        patient_name = self.main_values[Keys.EDIT_NAME_INPUT]
        mother = self.main_values[Keys.EDIT_MOTHER_INPUT]
        birth_date = self.__return_formated_date(Keys.EDIT_YEAR_BIRTH_INPUT, Keys.EDIT_MONTH_BIRTH_INPUT, Keys.EDIT_DAY_BIRTH_INPUT)
        gender = self.__return_gender_value(Keys.EDIT_F_GENDER_INPUT, Keys.EDIT_M_GENDER_INPUT)
        vf.validate_edit(sus_number, patient_name, gender, birth_date, mother)


    ##################
    # Update Methods # -------------------------------------------------------------------------------------------------
    ##################

    def update_main_greetings_user(self):
        """Atualiza a saudação com o nome do usuário na tela."""
        user = vf.validate_return_user(self.user_id)
        self._main_window[Keys.MAIN_GREETINGS].update(value=f'Bem vindo(a), {str(user).upper()}!')

    def update_search_result(self):
        """Retorna valores da pesquisa pro quadro de resultados."""
        data = self.__return_search_values()
        db_return = vf.validate_search_input(data[0], data[1], data[2])
        self.clean_search_result()
        for key, value in enumerate(db_return):
            usuario = vf.validate_return_user(value[9])
            self.__return_search_result(value[0], value[1], value[4], value[3], value[2], value[5], value[6], value[7], value[8], value[10], usuario)
        self.clean_search_tab()

    def update_returned_search_result(self):
        """Retorna todos os prontuários já devolvidos."""
        db_return = vf.validate_db_return_all_returned()
        self.clean_search_result()
        for key, value in enumerate(db_return):
            usuario = vf.validate_return_user(value[9])
            self.__return_search_result(value[0], value[1], value[4], value[3], value[2], value[5], value[6], value[7], value[8], value[10], usuario)
        self.clean_search_tab()

    def updaten_n_returned_search_result(self):
        """Retorna todos os prontuários não devolvidos."""
        db_return = vf.validate_db_return_all_n_returned()
        self.clean_search_result()
        for key, value in enumerate(db_return):
            user = vf.validate_return_user(value[9])
            self.__return_search_result(value[0], value[1], value[4], value[3], value[2], value[5], value[6], value[7], value[8], value[10], user)
        self.clean_search_tab()

    # Clean var values
    def clean_new_user_window(self):
        """Limpa a tela de cadastro de novo usuário."""
        self._new_user_window[Keys.NEW_U_NAME].update(value='')
        self._new_user_window[Keys.NEW_U_LOGIN].update(value='')
        self._new_user_window[Keys.NEW_U_PASSWORD].update(value='')
        self._new_user_window[Keys.NEW_U_CONFIRM_PASS].update(value='')

    def clean_search_result(self):
        """Limpa quadro de resultado de pesquisas."""
        self._main_window[Keys.SEARCH_R_OUTPUT].update(value='')

    def clean_login(self):
        """Limpa valores do Login"""
        self._login_window[Keys.L_LOGIN_INPUT].update(value='')
        self._login_window[Keys.L_PASSW_INPUT].update(value='')

    def clean_register_tab(self):
        """Limpa todos os campos da tab cadastro."""
        self._main_window[Keys.R_SUS_INPUT].update(value='')
        self._main_window[Keys.R_NAME_INPUT].update(value='')
        self._main_window[Keys.R_MOTHER_INPUT].update(value='')
        self._main_window[Keys.R_M_GENDER_INPUT].update(value=False)
        self._main_window[Keys.R_F_GENDER_INPUT].update(value=False)
        self._main_window[Keys.R_DAY_BIRTH_INPUT].update(value='Dia')
        self._main_window[Keys.R_MONTH_BIRTH_INPUT].update(value='Mês')
        self._main_window[Keys.R_YEAR_BIRTH_INPUT].update(value='Ano')

    def clean_search_tab(self):
        """Limpa os valores das variáveis na janela busca."""
        self._main_window[Keys.S_SUS_INPUT].update(value='')
        self._main_window[Keys.S_NAME_INPUT].update(value='')
        self._main_window[Keys.S_DAY_BIRTH_INPUT].update(value='Dia')
        self._main_window[Keys.S_MONTH_BIRTH_INPUT].update(value='Mês')
        self._main_window[Keys.S_YEAR_BIRTH_INPUT].update(value='Ano')

    def clean_r_o_tab(self):
        """Limpa os valores da janela Entrada / Saída."""
        self._main_window[Keys.R_O_SUS_INPUT].update(value='')
        self._main_window[Keys.R_O_EMPLOYEE_INPUT].update(value='')
        self._main_window[Keys.R_O_DAY_INPUT].update(value='Dia')
        self._main_window[Keys.R_O_MONTH_INPUT].update(value='Mês')
        self._main_window[Keys.R_O_YEAR_INPUT].update(value='Ano')
        self._main_window[Keys.R_O_HOUR_INPUT].update(value='')

    def clean_edit_del_tab(self):
        """Limpa os valores da janela Editar / Excluir."""
        self._main_window[Keys.EDIT_DEL_SEARCH_SUS].update(value='')
        self._main_window[Keys.EDIT_NAME_INPUT].update(value='')
        self._main_window[Keys.EDIT_MOTHER_INPUT].update(value='')
        self._main_window[Keys.EDIT_M_GENDER_INPUT].update(value=False)
        self._main_window[Keys.EDIT_F_GENDER_INPUT].update(value=False)
        self._main_window[Keys.EDIT_YEAR_BIRTH_INPUT].update(value='Ano')
        self._main_window[Keys.EDIT_MONTH_BIRTH_INPUT].update(value='Mês')
        self._main_window[Keys.EDIT_DAY_BIRTH_INPUT].update(value='Dia')
