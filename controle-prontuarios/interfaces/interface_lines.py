import PySimpleGUI as sg
from datetime import date


class MainInterfaceLines:
    """Tela principal."""

    def __init__(self):
        # Variáveis de inicialização
        self.login_layout = None
        self.login_window = None
        self.main_layout = None
        self.main_window = None

        # Elements Lines -----------------------------------------------------------------------------------------------
        # Var
        days = ([i for i in range(1, 32)])
        mounths = ({'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': 5, 'Jun': 6,
                    'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12})
        years = [int(year) for year in range(date.today().year, date.today().year - 150, -1)]

        # Login Window -------------------------------------------------------------------------------------------------
        self.login_window_greetings = [
            [sg.Text('Bem Vindo(a)!',
                     font=('Arial', 13),
                     text_color='#00345B',
                     background_color='#dcdcdc',
                     pad=((0, 0), (5, 0)))],
            [sg.Text('LOGIN',
                     font=('Arial Black', 22),
                     text_color='#00345B',
                     background_color='#dcdcdc',
                     pad=((0, 0), (0, 20)))],
        ]
        self.login_window_credentials = [
            [sg.Text('USUÁRIO',
                     font=('Arial Black', 8),
                     text_color='#00345B',
                     background_color='#dcdcdc',
                     pad=((5, 5), (5, 0)))],
            [sg.Input(key='-login-', pad=((5, 5), (0, 5)))],
            [sg.Text('SENHA',
                     font=('Arial Black', 8),
                     text_color='#00345B',
                     background_color='#dcdcdc',
                     pad=((5, 5), (10, 0)))],
            [sg.Input(key='-senha-', password_char='*', pad=((5, 5), (0, 5)))]
        ]
        self.login_window_developer = [
            [sg.Text('Desenvolvido por: Maik Marques - Github: Maik-M',
                     font=('Arial', 8),
                     text_color='#808080',
                     background_color='#dcdcdc')]
        ]

        # Main Window --------------------------------------------------------------------------------------------------
        # Register Lines
        self.resgister_line_left = [
            [sg.Text('N° SUS', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-c_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DO PACIENTE', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-c_nome-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DA MÃE', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-c_nome_mae-', pad=((5, 5), (0, 5)))]
        ]
        self.resgister_line_right = [
            [sg.Text('SEXO', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Radio('M', 'SEXO', key='-c_sexo_M-', font=('Arial', 8),
                      pad=((5, 5), (0, 5)),
                      text_color='#00345B',
                      background_color='#d1d1d1'),
             sg.Radio('F', 'SEXO', key='-c_sexo_F-', font=('Arial', 8),
                      pad=((5, 5), (0, 5)),
                      text_color='#00345B',
                      background_color='#d1d1d1')],
            [sg.Text('DATA DE NASCIMENTO', font=('Arial', 8),
                     pad=((5, 5), (5, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.OptionMenu(values=days, key='-c_nascimento_dia-',
                           default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths], key='-c_nascimento_mes-',
                           default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years, key='-c_nascimento_ano-',
                           default_value='Ano', size=(4, 1))]

        ]
        self.buttom_line_cadastro = [
            sg.Button('Cadastrar', key='-button_cadastrar-', pad=((10, 5), (13, 0))),
            sg.Button('Limpar', key='-button_limpar-', pad=((5, 5), (13, 0)))
        ]

        # Search Lines
        self.search_line = [
            [sg.Text('N° SUS', font=('Arial', 8),
                     pad=(5, 0),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-b_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME', font=('Arial', 8),
                     pad=(5, 0),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-b_nome-', pad=((5, 5), (0, 5)))],
            [sg.Text('DATA DE NASCIMENTO', font=('Arial', 8),
                     pad=(5, 0),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.OptionMenu(values=days, key='-b_nascimento_dia-',
                           default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths], key='-b_nascimento_mes-',
                           default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years, key='-b_nascimento_ano-',
                           default_value='Ano', size=(4, 1))]
        ]
        self.search_line_status = [
            [sg.Text('STATUS',
                     font=('Arial Black', 10),
                     text_color='#00345B',
                     background_color='#d1d1d1',
                     pad=((0, 0), (5, 0)))],
            [sg.Text('--------------------',
                     key='-b_status_text-',
                     font=('Arial Black', 12),
                     text_color='green',
                     background_color='#d1d1d1',
                     pad=(0, 0))],
            # [sg.Text('      NÃO\nENTREGUE',
            #          key='-b_status_text-',
            #          font=('Arial Black', 12),
            #          text_color='red',
            #          background_color='#d1d1d1',
            #          pad=(0, 0))]
        ]
        self.search_line_right_buttons = [
            [sg.Button('Buscar', key='-button_buscar-', pad=((5, 2), (0, 0))),
             sg.Button('Saída', key='-saida_button-', pad=((2, 2), (0, 0))),
             sg.Button('Chegada', key='-chegada_button-', pad=((2, 2), (0, 0))),
             sg.Button('Limpar', key='-search_button_limpar-', pad=((2, 5), (0, 0)))]
        ]

        # Output Line
        self.output_line = [
            [sg.Text('PAINEL',
                     font=('Arial Black', 10),
                     pad=((0, 0), (10, 0)),
                     text_color='#00345B',
                     background_color='#dcdcdc')],
            [sg.Listbox(values=[],
                        key='-output-',
                        font=('Arial', 10),
                        highlight_text_color='#00345B',
                        highlight_background_color='#d1d1d1',
                        size=(65, 6),
                        pad=((0, 0), (0, 0)))]
        ]
        self.output_line_buttons = [
            [sg.Button('Deletar', key='-button_deletar-', expand_x=True)],
            [sg.Button('Editar', key='-button_editar-', expand_x=True)],
            [sg.Button('Limpar', key='-button_limpar_output-', expand_x=True)]
        ]

        # Columns ------------------------------------------------------------------------------------------------------
        # Login Columns
        self.greetings_login_column = sg.Column(
            self.login_window_greetings,
            key='-greetings_login_column-',
            element_justification='center',
            background_color='#dcdcdc',
            expand_x=True,
            expand_y=True,
            pad=(5, 5)
        )
        self.credentials_login_column = sg.Column(
            self.login_window_credentials,
            key='-credentials_login_column-',
            element_justification='center',
            background_color='#dcdcdc',
            expand_x=True,
            expand_y=True,
            pad=(5, 20)
        )
        self.developer_login_column = sg.Column(
            self.login_window_developer,
            key='-developer_login_column-',
            element_justification='right',
            vertical_alignment='bottom',
            background_color='#dcdcdc',
            expand_x=True,
            expand_y=True,
            pad=((5, 5), (117, 5))
        )

        # Register Column
        self.register_left_column = sg.Column(
            self.resgister_line_left,
            key='-column_register_left-',
            background_color='#d1d1d1',
            pad=(5, 0)
        )
        self.register_right_column = sg.Column(
            self.resgister_line_right,
            key='-column_register_right-',
            element_justification='left',
            vertical_alignment='bottom',
            background_color='#d1d1d1'
        )

        # Search Column
        self.search_left_column = sg.Column(
            self.search_line,
            key='-column_search-',
            element_justification='left',
            background_color='#d1d1d1',
            pad=((5, 0), (0, 0))
        )
        self.search_right_column = sg.Column(
            self.search_line_status,
            key='-column_search_status-',
            element_justification='center',
            background_color='#d1d1d1',
            pad=(60, 0)
        )
        self.search_right_bottons_column = sg.Column(
            self.search_line_right_buttons,
            key='-column_search_right_buttons-',
            element_justification='right',
            vertical_alignment='bottom',
            background_color='#d1d1d1',
            expand_x=True,
            pad=((0, 5), (5, 7))
        )

        # Output Column
        self.output_column = sg.Column(
            self.output_line,
            key='-output_column-',
            background_color='#dcdcdc',
            pad=((0, 0), (10, 0))
        )
        self.output_column_buttons = sg.Column(
            self.output_line_buttons,
            key='-output_column_buttons-',
            background_color='#dcdcdc',
            vertical_alignment='bottom',
            pad=((27, 5), (0, 5))
        )

        # Frames -------------------------------------------------------------------------------------------------------
        # Register Frame
        self.register_frame = [
            sg.Frame(layout=[
                [self.register_left_column,
                 sg.VerticalSeparator(pad=((2, 2), (10, 1))),
                 self.register_right_column],
                self.buttom_line_cadastro
            ], title='  CADASTRAR PACIENTE  ',
                key='-register_frame-',
                font=('Arial Black', 10),
                title_color='#00345B',
                background_color='#d1d1d1',
                expand_x=True,
                border_width=2,
                size=(0, 200),
                pad=((0, 0), (10, 0))
            )
        ]

        # Search Frame
        self.search_frame = [
            sg.Frame(layout=[
                [self.search_left_column,
                 sg.VerticalSeparator(pad=(7, 5)),
                 self.search_right_column],
                [self.search_right_bottons_column]
            ], title='  BUSCAR PACIENTE  ',
                key='-search_frame-',
                font=('Arial Black', 10),
                title_color='#00345B',
                background_color='#d1d1d1',
                expand_x=True,
                border_width=2,
                size=(0, 200),
                pad=((0, 0), (10, 0))
            )
        ]

    # Fix the bug of focus doted line on TabGroup()
    @staticmethod
    def fix_doted_line():
        style = sg.ttk.Style()
        style.configure('Tab', focuscolor=sg.theme_background_color('#d1d1d1'))
