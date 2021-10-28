import PySimpleGUI as sg


class Interface:
    def __init__(self):
        """Interface do programa dividida em linhas."""
        # Variáveis
        self.layout = []
        self.window = None
        self.events = None
        self.values = None

        # Layouts ---------------------------
        # Input line
        self.input_line = [[sg.Text('PESQUISE O POKÉMON', key='-err-', font=('Arial Black', 10),
                                    pad=((10, 0), (10, 0)))],
                           [sg.Input(size=(35, 1), key='pokemon_name', pad=(10, 0)),
                            sg.Button(' OK ', key='-ok_button-', size=(10, 0), pad=((0, 10), (0, 0)))],
                           [sg.Text('', expand_x=True)]]

        # Sprite Square
        self.sprite_img_square_line = [[sg.Frame(layout=[
            [sg.Text('', pad=(46, 42), key='-img_square-'),
             sg.Image(key='-img-')]],
            title=' Sprite ', key='-f_1-', border_width=1, font=('Arial', 10))]]

        # Stats Line
        self.stats_line = [[sg.Text('HP:', key='-s_1-', font=('Arial Black', 7)),
                            sg.Text('', key='-hp-', font=('Arial', 7))],
                           [sg.Text('ATAQUE:', key='-s_2-', font=('Arial Black', 7)),
                            sg.Text('', key='-attack-', font=('Arial', 7))],
                           [sg.Text('DEFESA:', key='-s_3-', font=('Arial Black', 7)),
                            sg.Text('', key='-defense-', font=('Arial', 7))],
                           [sg.Text('ATAQUE+:', key='s_4', font=('Arial Black', 7)),
                            sg.Text('', key='-attack_plus-', font=('Arial', 7))],
                           [sg.Text('DEFESA+:', key='s_5', font=('Arial Black', 7)),
                            sg.Text('', key='-defense_plus-', font=('Arial', 7))],
                           [sg.Text('VELOCIDADE:', key='s_6', font=('Arial Black', 7)),
                            sg.Text('', key='-speed-', font=('Arial', 7))]]

        # ID Line
        self.id_line = [sg.Text('ID:', key='-id_text-', font=('Arial Black', 10)),
                        sg.Text('', key='-id-', font=('Arial', 10))]

        # Height and weight line
        self.height_weight_line = [sg.Text('ALTURA:', key='-height_text-', font=('Arial Black', 10)),
                                   sg.Text('', key='-height-', font=('Arial', 10), size=(4, 1)),
                                   sg.Text(f'PESO:', key='-weight_text-', font=('Arial Black', 10)),
                                   sg.Text('', key='-weight-', font=('Arial', 10))]

        # Type line
        self.type_line = [sg.Text('TIPO:', key='-t_1-', font=('Arial Black', 10)),
                          sg.Text('', key='-type_0-', font=('Arial', 10), text_color='white', visible=True),
                          sg.Text('', key='-type_1-', font=('Arial', 10), text_color='white', visible=False),
                          sg.Text('', key='-type_2-', font=('Arial', 10), text_color='white', visible=False)]

        # Abilities line
        self.abilities_line = [sg.Text('LISTA DE HABILIDADES', key='-a_1-', font=('Arial Black', 10),
                                       pad=((5, 0), (15, 0)))]
        self.ability_line_0 = [sg.Text('', key='-ability_0-', font=('Arial', 10), pad=((5, 0), (0, 0)), visible=True)]
        self.ability_line_1 = [sg.Text('', key='-ability_1-', font=('Arial', 10), pad=((5, 0), (0, 0)), visible=True)]
        self.ability_line_2 = [sg.Text('', key='-ability_2-', font=('Arial', 10), pad=((5, 0), (0, 0)), visible=True)]

        # More about line
        self.more_about_line = [sg.Text('', key='-more_about-', font=('Arial', 8), text_color='white',
                                        size=(50, 1), pad=((0, 0), (0, 0)))]

        self.err_layout = [
            [sg.Text('', key='-err-', font=('Arial Black', 25), justification='center', text_color='yellow',
                     size=(50, 5))],
            [sg.Button('REINICIAR', auto_size_button=True, expand_x=True)]
        ]
