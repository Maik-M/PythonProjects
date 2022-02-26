import PySimpleGUI as sg


class NewUserInterfaceLines:
    """Tela de registro de novo usuário."""

    def __init__(self):
        # Variaveis de inicialização

        self._new_user_layout = None
        self._new_user_window = None

        # Lines --------------------------------------------------------------------------------------------------------
        # Title Line
        self._new_user_title_line = [
            [sg.Text('DIGITE SUAS CREDENCIAIS',
                     font=('Arial Black', 9), text_color='#00345B', background_color='#dcdcdc')
             ]
        ]

        # New User Credentials
        self._new_user_credential_line = [
            [sg.Text('NOME COMPLETO',
                     font=('Arial', 8), text_color='#00345B', background_color='#dcdcdc', pad=(5, (0, 0)))],
            [sg.Input(key='-new_user_name-', pad=(5, (0, 5)))],
            [sg.Text('NOME DE USUÁRIO',
                     font=('Arial', 8), text_color='#00345B', background_color='#dcdcdc', pad=(5, (8, 0)))],
            [sg.Input(key='-new_user_login-', pad=(5, (0, 5)))],
            [sg.Text('SENHA',
                     font=('Arial', 8), text_color='#00345B', background_color='#dcdcdc', pad=(5, (8, 0)))],
            [sg.Input(key='-new_user_password-', password_char='*', pad=(5, (0, 5)))],
            [sg.Text('CONFIRMAR SENHA',
                     font=('Arial', 8), text_color='#00345B', background_color='#dcdcdc', pad=(5, (8, 0)))],
            [sg.Input(key='-new_user_confirm_password-', password_char='*', pad=(5, (0, 5)))]
        ]

        self._new_user_buttons = [
            [sg.Button('OK', key='-new_user_ok_button-', font=('Arial Black', 8), expand_x=True, pad=((5, 10), 5)),
             sg.Button('CANCELAR', key='-new_user_cancel_button-', font=('Arial Black', 8), expand_x=True, pad=((10, 5), 5))
             ]
        ]

        # Colunms ------------------------------------------------------------------------------------------------------
        self._new_user_title_column = sg.Column(
            self._new_user_title_line,
            key='-new_user_title_column-', element_justification='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=(5, (10, 5))
        )

        self._new_user_credential_column = sg.Column(
            self._new_user_credential_line,
            key='-new_user_credential_column-', element_justification='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=((15, 15), (0, 0))
        )

        self._new_user_buttons_column = sg.Column(
            self._new_user_buttons,
            key='-new_user_buttons_column-', element_justification='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=(5, (5, 10))
        )

    @property
    def new_user_window(self):
        return self._new_user_window
