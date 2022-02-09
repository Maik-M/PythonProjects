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
            [sg.Text('N° SUS',
                     font=('Arial', 8), pad=((5, 5), (0, 0)), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Input(key='-r_sus-',pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DO PACIENTE',
                     font=('Arial', 8), pad=((5, 5), (0, 0)), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Input(key='-r_nome-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DA MÃE',
                     font=('Arial', 8), pad=((5, 5), (0, 0)), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Input(key='-r_nome_mae-', pad=((5, 5), (0, 5)))]
        ]

        self._resgistration_right_line = [
            [sg.Text('SEXO',
                     font=('Arial', 8), pad=((5, 5), (0, 0)), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Radio('M', 'SEXO',
                      key='-r_sexo_M-', font=('Arial', 8), pad=((5, 5), (0, 5)), text_color='#00345B', background_color='#d1d1d1'),
             sg.Radio('F', 'SEXO',
                      key='-r_sexo_F-', font=('Arial', 8), pad=((5, 5), (0, 5)), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Text('DATA DE NASCIMENTO',
                     font=('Arial', 8), pad=((5, 5), (5, 0)), text_color='#00345B', background_color='#d1d1d1')],
            [sg.OptionMenu(values=days,
                           key='-r_nascimento_dia-', default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths],
                           key='-r_nascimento_mes-', default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years,
                           key='-r_nascimento_ano-', default_value='Ano', size=(4, 1))]

        ]
        self._registration_buttons_line = [
            sg.Button('Cadastrar',
                      key='-r_button_cadastrar-', pad=((10, 5), (13, 0))),
            sg.Button('Limpar',
                      key='-r_button_limpar-', pad=((5, 5), (13, 0)))
        ]

        # Search Lines Tab
        self._search_line = [
            [sg.Text('N° SUS',
                     font=('Arial', 8), pad=(5, 0), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Input(key='-s_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME',
                     font=('Arial', 8), pad=(5, 0), text_color='#00345B', background_color='#d1d1d1')],
            [sg.Input(key='-s_nome-', pad=((5, 5), (0, 5)))],
            [sg.Text('DATA DE NASCIMENTO',
                     font=('Arial', 8), pad=(5, 0), text_color='#00345B', background_color='#d1d1d1')],
            [sg.OptionMenu(values=days,
                           key='-s_nascimento_dia-', default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths],
                           key='-s_nascimento_mes-', default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years,
                           key='-s_nascimento_ano-',default_value='Ano', size=(4, 1))]
        ]

        self._search_buttons_line = [
            [sg.Button('Buscar', key='-s_button_buscar-', font=('Helvetica', 8), size=(13, 1), pad=((5, 5), (0, 0)))],
            [sg.Button('Limpar', key='-s_button_limpar-', font=('Helvetica', 8), size=(13, 1), pad=((5, 5), (2, 0)))],
            [sg.Text('LISTAR', font=('Arial Black', 8), text_color='#00345B', background_color='#d1d1d1', pad=((5, 5), (13, 0)))],
            [sg.Button('Entregues', key='-s_button_devolvidos-', font=('Helvetica', 8), size=(13, 1), pad=((5, 5), (2, 0)))],
            [sg.Button('Não Entregues', key='-s_button_n_devolvidos-', font=('Helvetica', 8), size=(13, 1), pad=((5, 5), (2, 0)))]
        ]

        # In/Out Lines Tab
        self._in_out_left_line = [
            [sg.Text('N° SUS DO PRONTUÁRIO',
                     font=('Arial', 8), text_color='#00345B', background_color='#d1d1d1', pad=(5, 0))],
            [sg.Input(key='-io_sus-', pad=((5, 5), (0, 5)))],
            [sg.Text('NOME DO FUNCIONÁRIO',
                     font=('Arial', 8), text_color='#00345B', background_color='#d1d1d1', pad=(5, 0))],
            [sg.Input(key='-io_funcionario-', pad=((5, 5), (0, 5)))],
            [sg.Text('DATA DE SAÍDA / CHEGADA',
                     font=('Arial', 8), text_color='#00345B', background_color='#d1d1d1', pad=(5, 0))],
            [sg.OptionMenu(values=days,
                           key='-io_dia-', default_value='Dia', size=(2, 1)),
             sg.OptionMenu(values=[mounth for mounth in mounths],
                           key='-io_mes-', default_value='Mês', size=(4, 1)),
             sg.OptionMenu(values=years,
                           key='-io_ano-', default_value='Ano', size=(4, 1))],
            [sg.Text('HORA DA SAÍDA / CHEGADA',
                     font=('Arial', 8), text_color='#00345B', background_color='#d1d1d1', pad=(5, 0))],
            [sg.Input(key='-io_hora-', size=(5, 2), pad=((5, 5), (0, 5)))]
        ]
        self._in_out_right_line = [
            [sg.Button('Saída',
                       key='-io_saida-', size=(10, 1), pad=((5, 5), (0, 10)))],
            [sg.Button('Chegada',
                       key='-io_chegada-', size=(10, 1), pad=((5, 5), (10, 10)))],
            [sg.Button('Limpar',
                       key='-io_limpar-', size=(10, 1), pad=((5, 5), (10, 10)))]
        ]

        # Search Result Line
        self._search_result_line = [
            [sg.Output(key='-search_result_output-',font=('Liberation Mono', 7), text_color='#00345B', background_color='#ffffff', expand_y=True,
                       size=(110, 19), pad=(0, 0))]
        ]


        # Edit and Delete Line
        self._edit_delete_buttons_line = [
            [sg.Button('Deletar',
                       key='-edit_delete_button_deletar-', expand_x=True)],
            [sg.Button('Editar',
                       key='-edit_delete_button_editar-', expand_x=True)],
            [sg.Button('Limpar',
                       key='-edit_delete_button_limpar-', expand_x=True)]
        ]

        # Columns ------------------------------------------------------------------------------------------------------
        # Registration Column
        self._registration_left_column = sg.Column(
            self._resgistration_left_line,
            key='-registration_left_column-', background_color='#d1d1d1', pad=(5, 0)
        )
        self._registration_right_column = sg.Column(
            self._resgistration_right_line,
            key='-registration_right_column-', element_justification='left', vertical_alignment='bottom', background_color='#d1d1d1'
        )

        # Search Column
        self._search_left_column = sg.Column(
            self._search_line,
            key='-search_left_column-', element_justification='left', background_color='#d1d1d1', pad=((5, 0), (0, 0))
        )
        self._search_right_column = sg.Column(
            self._search_buttons_line, key='-search_right_column-', element_justification='center', background_color='#d1d1d1', pad=(60, 0)
        )
        # self._search_buttons_column = sg.Column(
        #     self._search_buttons_line,
        #     key='-search_buttons_column-', element_justification='right', vertical_alignment='bottom', background_color='#d1d1d1',
        #     expand_x=True, pad=((0, 56), (5, 7))
        # )

        # In/Out Column
        self._in_out_left_column = sg.Column(
            self._in_out_left_line,
            key='-column_saida_left-', background_color='#d1d1d1', pad=((5, 0), (0, 0))
        )
        self._in_out_right_column = sg.Column(
            self._in_out_right_line,
            key='-column_entrada_right-', element_justification='center', vertical_alignment='center', background_color='#d1d1d1', pad=((63, 37), (0, 0))
        )


        # Search Result Column
        self._search_result_column = sg.Column(
            self._search_result_line,
            key='-search_result_column-', background_color='#ffffff', expand_x=True, size=(0, 206), pad=(0, 0)
        )

        # Edit and Delele Buttons Column
        self._edit_delete_buttons_column = sg.Column(
            self._edit_delete_buttons_line,
            key='-edit_delete_buttons_column-', background_color='#dcdcdc', vertical_alignment='bottom', pad=((27, 5), (0, 5))
        )

        # Frames -------------------------------------------------------------------------------------------------------
        # Registration Frame
        self._registration_frame = [
            sg.Frame(layout=[
                [self._registration_left_column,
                 sg.VerticalSeparator(pad=((2, 2), (10, 0))),
                 self._registration_right_column],
                self._registration_buttons_line
            ], title='  CADASTRAR PACIENTE  ', key='-registration_frame-', font=('Arial Black', 10), title_color='#00345B',
                background_color='#d1d1d1', expand_x=True, border_width=2, size=(0, 200), pad=((0, 0), (10, 0))
            )
        ]

        # Search Frame
        self._search_frame = [
            sg.Frame(layout=[
                [self._search_left_column,
                 sg.VerticalSeparator(pad=((7, 7), (10, 0))),
                 self._search_right_column],
            ], title='  BUSCAR PACIENTE  ', key='-find_frame-', font=('Arial Black', 10), title_color='#00345B',
                background_color='#d1d1d1', expand_x=True, border_width=2, size=(0, 200), pad=((0, 0), (10, 0))
            )
        ]

        # In/Out Frame = IO
        self._in_out_frame = [
            sg.Frame(layout=[
                [self._in_out_left_column,
                 sg.VerticalSeparator(pad=((7, 5), (10, 20))),
                 self._in_out_right_column]
            ], title='  SAÍDA E CHEGADA DE PRONTUÁIOS  ', key='-in_out_frame-', font=('Arial Black', 10), title_color='#00345b',
                background_color='#d1d1d1', expand_x=True, border_width=2, size=(0, 200), pad=((0, 0), (10, 0)))
        ]

        # Search Result Frame
        self._search_result_frame = [
            sg.Frame(layout=[
                [self._search_result_column]
        ], title='', key='-search_result_frame-', background_color='#ffffff', expand_x=True, border_width=2, size=(0, 205), pad=((0, 0), (5, 0)))
        ]

    @property
    def main_window(self):
        return self._main_window
