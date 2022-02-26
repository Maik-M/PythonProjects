import PySimpleGUI as sg


class LoginInterfaceLines:
    """Tela de login."""

    def __init__(self):
        self._login_layout = None
        self._login_window = None
        self.__id_usuario = None

        # Lines --------------------------------------------------------------------------------------------------------
        self._login_window_greetings = [
            [sg.Text('Bem Vindo(a)!',
                     font=('Arial', 13), text_color='#00345B', background_color='#dcdcdc', pad=((0, 0), (5, 0)))],
            [sg.Text('LOGIN',
                     font=('Arial Black', 22), text_color='#00345B', background_color='#dcdcdc', pad=((0, 0), (0, 20)))],
        ]

        self._login_window_credentials = [
            [sg.Text('USUÁRIO',
                     font=('Arial Black', 8), text_color='#00345B', background_color='#dcdcdc', pad=((5, 5), (5, 0)))],
            [sg.Input(key='-login-', pad=((5, 5), (0, 5)))],
            [sg.Text('SENHA',
                     font=('Arial Black', 8), text_color='#00345B', background_color='#dcdcdc', pad=((5, 5), (10, 0)))],
            [sg.Input(key='-password-', password_char='*', pad=((5, 5), (0, 5)))],
        ]
        self._login_button_entrar = [
            [sg.Button('Entrar',
                       key='-login_button-', font=('Arial Black', 8), expand_x=True, pad=(0, 0))]
        ]
        self._login_button_cadastrar = [
            [sg.Text('Não possui cadastro?',
                     font=('Arial', 7), text_color='#00345b', background_color='#dcdcdc', pad=((0, 2), (5, 5))),
             sg.Button('Cadastrar',
                       key='-new_user_button-', border_width=0, font=('Arial Black', 7), button_color=('#00345b', '#dcdcdc'),
                       mouseover_colors=('#ff1f1f', '#dcdcdc'), pad=((0, 0), (5, 5)))]
        ]
        self._login_window_developer = [
            [sg.Text('Desenvolvido por: Maik Marques - Github: Maik-M',
                     font=('Arial', 8), text_color='#808080', background_color='#dcdcdc')]
        ]

        # Columns ------------------------------------------------------------------------------------------------------
        # Login Columns
        self._greetings_login_column = sg.Column(
            self._login_window_greetings,
            key='-greetings_login_column-', element_justification='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=(5, 5)
        )

        self._credentials_login_column = sg.Column(
            self._login_window_credentials,
            key='-credentials_login_column-', element_justification='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=((5, 5), (5, 0))
        )

        self._login_button_entrar_column = sg.Column(
            self._login_button_entrar,
            key='-login_button_ok_column-', element_justification='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=((131, 131), (27, 5))
        )
        self._login_button_cadastrar_column = sg.Column(
            self._login_button_cadastrar,
            key='-login_button_cadastrar_column-', element_justification='center', vertical_alignment='center', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=((130, 130), (0, 5))
        )
        self._developer_login_column = sg.Column(
            self._login_window_developer,
            key='-developer_login_column-', element_justification='center', vertical_alignment='bottom', background_color='#dcdcdc',
            expand_x=True, expand_y=True, pad=((5, 5), (65, 0))
        )

    @property
    def login_window(self):
        return self._login_window

    @property
    def user_id(self):
        return self.__id_usuario

    @user_id.setter
    def user_id(self, usuario):
        self.__id_usuario = usuario
