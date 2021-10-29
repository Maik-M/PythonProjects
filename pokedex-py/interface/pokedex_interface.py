import PySimpleGUI as sg

from interface.interface import Interface
from api.poke_api import PokeApi


class PokedexInterface(Interface):
    """Essa classe monta toda a interface herdada da classe Interface."""

    def __init__(self):
        super().__init__()
        self.pokemon_name = ''

        # API
        self._poke_api = PokeApi()

    def make_window(self):
        """Inicia a Janela."""
        self.layout = [
            self.input_line,
            [sg.Frame(layout=[
                [sg.Column(
                    self.sprite_img_square_line,
                    key='-left_column-', element_justification='left', pad=((0, 0), (0, 0))),
                    sg.Column(
                        self.stats_line,
                        key='-right_column-', element_justification='right', pad=((20, 5), (10, 0)))],
                self.id_line,
                self.height_weight_line,
                self.type_line,
                self.abilities_line,
                self.ability_line_0,
                self.ability_line_1,
                self.ability_line_2,
                [sg.Column([
                    self.more_about_line],
                    key='-more_about_column-', vertical_alignment='r', pad=((5, 0), (8, 0)))],
            ], title=f'  POKÉMON  ', key='-pokemon-', font=('Arial Black', 10),
                border_width=2, pad=((10, 10), (0, 10)), title_color='yellow',
                expand_x=True, expand_y=True)]
        ]
        self.window = sg.Window('Pokedex', self.layout, size=(350, 500),  # Inicia a Janela
                                titlebar_icon='./img/pokeball-icon-window.png', use_custom_titlebar=True,
                                finalize=True)

    def input_values(self):
        """Recebe os valores e eventos de clicks."""
        self.events, self.values = self.window.Read()

    def update_values(self):
        """Recebe valores e atualiza chamando o método update_window()."""
        self.pokemon_name = self.values['pokemon_name'].lower()
        self._poke_api.get_values(self.pokemon_name)
        self.update_window()

    def update_window(self):
        """Atualiza os valores da janela."""
        # Trava o quadro no tamanho da imagem até atualizar
        self.window['-img_square-'].update(visible=False)
        # Atualiza Nome do Pokémon
        self.window['-pokemon-'].update(f'  {self.pokemon_name.upper()}  ')
        # Atualiza os status
        self.window['-hp-'].update(f'{self._poke_api.stats_list[0]["base_stat"]}')
        self.window['-attack-'].update(f'{self._poke_api.stats_list[1]["base_stat"]}')
        self.window['-defense-'].update(f'{self._poke_api.stats_list[2]["base_stat"]}')
        self.window['-attack_plus-'].update(f'{self._poke_api.stats_list[3]["base_stat"]}')
        self.window['-defense_plus-'].update(f'{self._poke_api.stats_list[4]["base_stat"]}')
        self.window['-speed-'].update(f'{self._poke_api.stats_list[5]["base_stat"]}')
        # Atualiza ID
        self.window['-id-'].update(f'{self._poke_api.poke_id}')
        # Atualiza o Sprite do Pokémon
        self.window['-img-'].update(data=self._poke_api.get_sprite_image())
        # Atuliza o peso
        self.window['-height-'].update(f'{self._poke_api.height}m')
        # Atualiza os tipos do pokémon percorrendo a lista de tipos e torna o texto visível
        if len(self._poke_api.type_list) <= 2:
            self.window['-type_1-'].update('', visible=False)
            self.window['-type_2-'].update('', visible=False)
        [self.window[f'-type_{str(i)}-'].update(f'{str(value_type).capitalize()}', visible=True)
         for i, value_type in enumerate(self._poke_api.type_list)]
        # Atualiza o peso
        self.window['-weight-'].update(f'{self._poke_api.weight}kg')
        # Percorre a lista de skills, limpa o output caso esteja escrito algo e imprime as skilss
        if len(self._poke_api.abilities_list) <= 2:
            self.window['-ability_1-'].update('')
            self.window['-ability_2-'].update('')
        [self.window[f'-ability_{str(i)}-'].update(f'-- {str(ability).replace("-", " ")}')
         for i, ability in enumerate(self._poke_api.abilities_list)]
        # Atualiza o site do Pokedex
        self.window['-more_about-'].update(f'Mais sobre: https://www.pokemon.com/br/pokedex/'
                                           f'{self.pokemon_name.replace(" ", "")}/')
