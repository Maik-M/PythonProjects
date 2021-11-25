import PySimpleGUI as sg
from datetime import date


class MainInterfaceLines:
    """Tela principal."""

    def __init__(self):
        # Variáveis de inicialização
        self._main_layout = None
        self._main_window = None

        # Elements Lines -----------------------------------------------------------------------------------------------
        # Var
        days = [i for i in range(1, 32)]
        mounths = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
        years = [int(year) for year in range(date.today().year, date.today().year - 150, -1)]

        # Lines --------------------------------------------------------------------------------------------------------
        # Registration Lines Tab
        self._resgistration_left_line = [
            [sg.Text('N° SUS', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-r_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DO PACIENTE', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-r_nome-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DA MÃE', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-r_nome_mae-', pad=((5, 5), (0, 5)))]
        ]
        self._resgistration_right_line = [
            [sg.Text('SEXO', font=('Arial', 8),
                     pad=((5, 5), (0, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Radio('M', 'SEXO', key='-r_sexo_M-', font=('Arial', 8),
                      pad=((5, 5), (0, 5)),
                      text_color='#00345B',
                      background_color='#d1d1d1'),
             sg.Radio('F', 'SEXO', key='-r_sexo_F-', font=('Arial', 8),
                      pad=((5, 5), (0, 5)),
                      text_color='#00345B',
                      background_color='#d1d1d1')],
            [sg.Text('DATA DE NASCIMENTO', font=('Arial', 8),
                     pad=((5, 5), (5, 0)),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.OptionMenu(values=days, key='-r_nascimento_dia-',
                           default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths], key='-r_nascimento_mes-',
                           default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years, key='-r_nascimento_ano-',
                           default_value='Ano', size=(4, 1))]

        ]
        self._registration_buttons_line = [
            sg.Button('Cadastrar', key='-r_button_cadastrar-', pad=((10, 5), (13, 0))),
            sg.Button('Limpar', key='-r_button_limpar-', pad=((5, 5), (13, 0)))
        ]

        # Find Lines Tab
        self._find_line = [
            [sg.Text('N° SUS', font=('Arial', 8),
                     pad=(5, 0),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-f_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME', font=('Arial', 8),
                     pad=(5, 0),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.Input(key='-f_nome-', pad=((5, 5), (0, 5)))],
            [sg.Text('DATA DE NASCIMENTO', font=('Arial', 8),
                     pad=(5, 0),
                     text_color='#00345B',
                     background_color='#d1d1d1')],
            [sg.OptionMenu(values=days, key='-f_nascimento_dia-',
                           default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths], key='-f_nascimento_mes-',
                           default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years, key='-f_nascimento_ano-',
                           default_value='Ano', size=(4, 1))]
        ]
        self._find_status_line = [
            [sg.Text('STATUS',
                     font=('Arial Black', 10),
                     text_color='#00345B',
                     background_color='#d1d1d1',
                     pad=((0, 0), (5, 0)))],
            [sg.Text('--------------------',
                     key='-f_status_text-',
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
        self._find_buttons_line = [
            [sg.Button('Buscar', key='-f_button_buscar-', pad=((5, 2), (0, 0))),
             sg.Button('Limpar', key='-f_button_limpar-', pad=((2, 5), (0, 0)))]
        ]

        # In/Out Lines Tab
        self._in_out_left_line = [
            [sg.Text('N° SUS DO PRONTUÁRIO', font=('Arial', 8),
                     text_color='#00345B',
                     background_color='#d1d1d1',
                     pad=(5, 0))],
            [sg.Input(key='-io_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DO FUNCIONÁRIO', font=('Arial', 8),
                     text_color='#00345B',
                     background_color='#d1d1d1',
                     pad=(5, 0))],
            [sg.Input(key='-io_funcionario-', pad=((5, 5), (0, 5)))],
            [sg.Text('DATA DE SAÍDA / ENTRADA', font=('Arial', 8),
                     text_color='#00345B',
                     background_color='#d1d1d1',
                     pad=(5, 0))],
            [sg.OptionMenu(values=days, key='-io_dia-',
                           default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths], key='-io_mes-',
                           default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years, key='-io_ano-',
                           default_value='Ano', size=(4, 1))],
            [sg.Text('HORA DA SAÍDA / ENTRADA', font=('Arial', 8),
                     text_color='#00345B',
                     background_color='#d1d1d1',
                     pad=(5, 0))],
            [sg.Input(key='-io_hora-', size=(5, 2),
                      pad=((5, 5), (0, 5)))]
        ]
        self._in_out_right_line = [
            [sg.Button('Saída', key='-io_saida-', size=(10, 1), pad=((5, 5), (0, 10)))],
            [sg.Button('Chegada', key='-io_chegada-', size=(10, 1), pad=((5, 5), (10, 10)))],
            [sg.Button('Limpar', key='-io_limpar-', size=(10, 1), pad=((5, 5), (10, 10)))]
        ]

        # Board Line
        self._board_line = [
            [sg.Text('PAINEL',
                     font=('Arial Black', 10),
                     pad=((0, 0), (10, 0)),
                     text_color='#00345B',
                     background_color='#dcdcdc')],
            [sg.Listbox(values=[['Maria', 'Atonia'], ['Carlos', 'Maria']],
                        key='-board-',
                        font=('Arial', 10),
                        select_mode=1,
                        enable_events=True,
                        highlight_text_color='#00345B',
                        highlight_background_color='#d1d1d1',
                        size=(65, 6),
                        pad=((0, 0), (0, 0)))]
        ]
        self._board_buttons_line = [
            [sg.Button('Deletar', key='-b_button_deletar-', expand_x=True)],
            [sg.Button('Editar', key='-b_button_editar-', expand_x=True)],
            [sg.Button('Limpar', key='-b_button_limpar-', expand_x=True)]
        ]

        # Columns ------------------------------------------------------------------------------------------------------
        # Registration Column
        self._registration_left_column = sg.Column(
            self._resgistration_left_line,
            key='-registration_left_column-',
            background_color='#d1d1d1',
            pad=(5, 0)
        )
        self._registration_right_column = sg.Column(
            self._resgistration_right_line,
            key='-registration_right_column-',
            element_justification='left',
            vertical_alignment='bottom',
            background_color='#d1d1d1'
        )

        # Find Column
        self._find_left_column = sg.Column(
            self._find_line,
            key='-find_left_column-',
            element_justification='left',
            background_color='#d1d1d1',
            pad=((5, 0), (0, 0))
        )
        self._find_right_column = sg.Column(
            self._find_status_line,
            key='-find_right_column-',
            element_justification='center',
            background_color='#d1d1d1',
            pad=(60, 0)
        )
        self._find_buttons_column = sg.Column(
            self._find_buttons_line,
            key='-find_buttons_column-',
            element_justification='right',
            vertical_alignment='bottom',
            background_color='#d1d1d1',
            expand_x=True,
            pad=((0, 56), (5, 7))
        )

        # In/Out Column
        self._in_out_left_column = sg.Column(
            self._in_out_left_line,
            key='-column_saida_left-',
            background_color='#d1d1d1',
            pad=((5, 0), (0, 0))
        )
        self._in_out_right_column = sg.Column(
            self._in_out_right_line,
            key='-column_entrada_right-',
            element_justification='center',
            vertical_alignment='center',
            background_color='#d1d1d1',
            pad=((63, 37), (0, 0))
        )

        # Output Column
        self._board_column = sg.Column(
            self._board_line,
            key='-board_column-',
            background_color='#dcdcdc',
            pad=((0, 0), (10, 0))
        )
        self._board_buttons_column = sg.Column(
            self._board_buttons_line,
            key='-board_buttons_column-',
            background_color='#dcdcdc',
            vertical_alignment='bottom',
            pad=((27, 5), (0, 5))
        )

        # Frames -------------------------------------------------------------------------------------------------------
        # Registration Frame
        self._registration_frame = [
            sg.Frame(layout=[
                [self._registration_left_column,
                 sg.VerticalSeparator(pad=((2, 2), (10, 0))),
                 self._registration_right_column],
                self._registration_buttons_line
            ], title='  CADASTRAR PACIENTE  ',
                key='-registration_frame-',
                font=('Arial Black', 10),
                title_color='#00345B',
                background_color='#d1d1d1',
                expand_x=True,
                border_width=2,
                size=(0, 200),
                pad=((0, 0), (10, 0))
            )
        ]

        # Find Frame
        self._find_frame = [
            sg.Frame(layout=[
                [self._find_left_column,
                 sg.VerticalSeparator(pad=((7, 7), (10, 0))),
                 self._find_right_column],
                [self._find_buttons_column]
            ], title='  BUSCAR PACIENTE  ',
                key='-find_frame-',
                font=('Arial Black', 10),
                title_color='#00345B',
                background_color='#d1d1d1',
                expand_x=True,
                border_width=2,
                size=(0, 200),
                pad=((0, 0), (10, 0))
            )
        ]

        # In/Out Frame = IO
        self._in_out_frame = [
            sg.Frame(layout=[
                [self._in_out_left_column,
                 sg.VerticalSeparator(pad=((7, 5), (10, 20))),
                 self._in_out_right_column]
            ], title='  SAÍDA E ENTRADA DE PRONTUÁIOS  ',
                key='-in_out_frame-',
                font=('Arial Black', 10),
                title_color='#00345b',
                background_color='#d1d1d1',
                expand_x=True,
                border_width=2,
                size=(0, 200),
                pad=((0, 0), (10, 0)))
        ]

    @property
    def main_window(self):
        return self._main_window
