import PySimpleGUI as sg
from interface_lines import MainInterfaceLines


class MainInterface(MainInterfaceLines):
    """Faz a tela principal."""

    def __init__(self):
        super().__init__()

        # Variáveis
        self.login_events = None
        self.login_values = None
        self.events = None
        self.values = None

    def make_login_window(self):
        self.login_layout = [
            [sg.Frame(layout=[
                [self.greetings_login_column],
                [self.credentials_login_column],
                [self.developer_login_column]
            ], title='',
                background_color='#dcdcdc',
                expand_x=True,
                expand_y=True,
                border_width=0,
                pad=(0, 0)
            )
            ]
        ]
        self.login_window = sg.Window('Controle de Prontuários',
                                      self.login_layout,
                                      size=(600, 400),
                                      background_color='#dcdcdc',
                                      use_default_focus=False,
                                      finalize=True)
        MainInterfaceLines.fix_doted_line()

    def input_login_values(self):
        self.login_events, self.login_values = self.login_window.Read()

    def make_window(self):
        self.main_layout = [
            [sg.TabGroup(layout=[
                [sg.Tab(title='Cadastrar', key='-tab_cadastro-', layout=[
                    self.register_frame
                ], background_color='#d1d1d1'),
                 sg.Tab(title='Buscar', key='-tab_busca-', layout=[
                     self.search_frame
                 ], background_color='#d1d1d1')
                 ]
            ], key='-tab_group-',
                expand_x=True,
                visible=False,
                pad=(0, 0),
                selected_title_color='#000000',
                selected_background_color='#d1d1d1',
                background_color='#dcdcdc',
                border_width=0)],
            [self.output_column,
             self.output_column_buttons]
        ]
        self.main_window = sg.Window('Controle de Prontuários',
                                     self.main_layout,
                                     size=(600, 400),
                                     background_color='#dcdcdc',
                                     use_default_focus=False,
                                     finalize=True)
        MainInterfaceLines.fix_doted_line()

    def input_values(self):
        self.events, self.values = self.main_window.Read()


if __name__ == '__main__':
    start = MainInterface()
    start.make_login_window()
    while True:
        start.input_login_values()
        if start.login_events == sg.WINDOW_CLOSED:
            break
