import json

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
            [sg.Button('REINICIAR', key='-restart_button-', auto_size_button=True, expand_x=True, visible=False)],
            [sg.Frame(layout=[
                [sg.Column([
                    self.sprite_img_square_line],
                    key='-left_column-', element_justification='left', pad=((0, 0), (0, 0))),
                    sg.Column(
                        self.stats_line,
                        key='-right_column-', element_justification='right', pad=((20, 5), (10, 0)))],
                self.id_line,
                self.height_weight_line,
                self.type_line,
                self.abilities_line,
                self.output_abilities_line,
                self.more_about_line,
            ], title=f'  POKÉMON  ', key='-pokemon-', font=('Arial Black', 10),
                border_width=2, pad=((10, 10), (0, 10)), title_color='yellow',
                expand_x=True, expand_y=True)]
        ]
        self.window = sg.Window('Pokedex', self.layout, size=(350, 500),  # Inicia a Janela
                                titlebar_icon='./img/pokeball-icon-window.png', use_custom_titlebar=True,
                                finalize=True)

    def update_err_window_off(self, message):
        self.window['-pokemon-'].update(visible=False)
        self.window['-ok_button-'].update(visible=False)
        self.window['pokemon_name'].update(visible=False)
        self.window['-err-'].update(f'{message}', font=('Arial Black', 25), text_color='yellow')
        self.window['-restart_button-'].update(visible=True)

    def update_err_window_on(self):
        self.window['-pokemon-'].update(visuble=True)
        self.window['pokemon_name'].update(visible=True)
        self.window['-err-'].update('PESQUISE O POKÉMON', key='-err-', font=('Arial Black', 10), text_color='white')
        self.window['-restart_button-'].update(visible=False)

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
        [self.window[f'-type_{str(i)}-'].update(f'{str(value).capitalize()}', visible=True)
         for i, value in enumerate(self._poke_api.type_list)]

        # Atualiza o peso
        self.window['-weight-'].update(f'{self._poke_api.weight}kg')

        # Percorre a lista de skills, limpa o output caso esteja escrito algo e imprime as skilss
        self.window['-abilities-'].update(value='')
        [print(f'- {ability.replace("-", " ")}') for ability in self._poke_api.abilities_list]

        # Atualiza o site do Pokedex
        self.window['-more_about-'].update(f'Mais sobre: https://www.pokemon.com/br/pokedex/'
                                           f'{self.pokemon_name.replace(" ", "")}/')

    def input_values(self):
        """Recebe os valores e eventos de clicks."""
        self.events, self.values = self.window.Read()

    def start(self):
        """Função de start com lógica para receber dados e atualizar valores da tela."""
        self.make_window()
        while True:
            try:
                while True:
                    self.input_values()
                    if self.events == '-ok_button-':
                        self.pokemon_name = self.values['pokemon_name'].lower()
                        self._poke_api.get_values(self.pokemon_name)
                        self.update_window()
                    if self.events == sg.WINDOW_CLOSED or self.events == 'Quit':
                        self.window.close()
                        break
            except KeyError:
                self.update_err_window_off('CAMPO VAZIO!\n\nPOR FAVOR\nINSIRA O NOME\nDO POKÉMON.')
                self.input_values()
                if self.events == '-restart_button-':
                    self.update_err_window_on()
            except json.JSONDecodeError:
                self.update_err_window_off('VERIFIQUE O\nNOME DO\nPOKÉMON\n\nREINICIE OU\nFECHE A\nJANELA')
                self.input_values()
                if self.events == '-restart_button-':
                    self.update_err_window_on()

            # if self.values['pokemon_name'] == '':
            #     self.window.close()
            #     self.layout = [
            #         [sg.Text('', key='-err-', font=('Arial Black', 25), justification='center', text_color='yellow',
            #                  size=(50, 5))],
            #         [sg.Button('REINICIAR', auto_size_button=True, expand_x=True)]
            #     ]
            #     self.window = sg.Window('Pokedex', self.layout, size=(500, 500), finalize=True,
            #                             titlebar_icon='./img/pokeball-icon-window.png', use_custom_titlebar=True)
            #     self.window['-err-'].update('CAMPO VAZIO!\n\nPOR FAVOR\nINSIRA O NOME\nDO POKÉMON.')
            #     self.input_values()
            #     if self.events == 'REINICIAR':
            #         self.window.close()
            #         self.start()
            # elif Exception:
            #     self.window.close()
            #     self.layout = [
            #         [sg.Text('', key='-err-', font=('Arial Black', 25), justification='center', text_color='yellow',
            #                  size=(50, 7))],
            #         [sg.Button('REINICIAR', auto_size_button=True, expand_x=True)]
            #     ]
            #     self.window = sg.Window('Pokedex', self.layout, size=(500, 500), finalize=True,
            #                             titlebar_icon='./img/pokeball-icon-window.png', use_custom_titlebar=True)
            #     self.window['-err-'].update('VERIFIQUE O\nNOME DO\nPOKÉMON'
            #                                 '\n\nREINICIE OU\nFECHE A\nJANELA')
            #     self.input_values()
            #     if self.events == 'REINICIAR':
            #         self.window.close()
            #         self.start()
