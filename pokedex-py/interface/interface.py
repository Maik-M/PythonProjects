import PySimpleGUI as sg


class Interface:
    def __init__(self):
        """Interface do programa dividida em linhas."""
        # Variáveis
        self.layout = None
        self.window = None
        self.events = None
        self.values = None

        # Layouts ---------------------------
        # Input line
        self.input_line = [sg.Text('PESQUISE O POKÉMON', key='-err-', font=('Arial Black', 10),
                                   pad=((10, 0), (10, 0)))], \
                          [sg.Input(size=(35, 1), key='pokemon_name', pad=(10, 0)),
                           sg.Button(' OK ', size=(10, 0), pad=((0, 10), (0, 0)))], \
                          [sg.Text('', expand_x=True)]

        # Sprite Square
        self.sprite_img_square_line = sg.Frame(layout=[
            [sg.Text('', pad=(46, 42), key='-img_square-'),
             sg.Image(key='-img-')]],
            title=' Sprite ', border_width=1, font=('Arial', 10))

        # Stats Line
        self.stats_line = [[sg.Text('HP:', font=('Arial Black', 7)),
                            sg.Text('', key='-hp-', font=('Arial', 7))],
                           [sg.Text('ATAQUE:', font=('Arial Black', 7)),
                            sg.Text('', key='-attack-', font=('Arial', 7))],
                           [sg.Text('DEFESA:', font=('Arial Black', 7)),
                            sg.Text('', key='-defense-', font=('Arial', 7))],
                           [sg.Text('ATAQUE+:', font=('Arial Black', 7)),
                            sg.Text('', key='-attack_plus-', font=('Arial', 7))],
                           [sg.Text('DEFESA+:', font=('Arial Black', 7)),
                            sg.Text('', key='-defense_plus-', font=('Arial', 7))],
                           [sg.Text('VELOCIDADE:', font=('Arial Black', 7)),
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
        self.type_line = [sg.Text('TIPO:', font=('Arial Black', 10)),
                          sg.Text('', key='-type_0-', font=('Arial', 10), text_color='white', visible=True),
                          sg.Text('', key='-type_1-', font=('Arial', 10), text_color='white', visible=False),
                          sg.Text('', key='-type_2-', font=('Arial', 10), text_color='white', visible=False)]

        # Abilities line
        self.abilities_line = [sg.Text('HABILIDADES', font=('Arial Black', 10), pad=((4, 0), (0, 0)))]
        self.output_abilities_line = [sg.Output(key='-abilities-', background_color='#64778d', font=('Arial', 10),
                                                text_color='white', pad=((5, 150), (0, 12)), expand_y=True)]

        # More about line
        self.more_about_line = [sg.Text('', key='-more_about-', font=('Arial', 8), text_color='white',
                                        size=(50, 1), pad=((5, 0), (0, 0)))]
