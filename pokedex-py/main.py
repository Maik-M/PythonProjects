import json
import PySimpleGUI as sg
from interface import pokedex_interface

pokedex = pokedex_interface.PokedexInterface()
pokedex.make_window()
while True:
    try:
        pokedex.input_values()
        if pokedex.events == '-ok_button-':
            pokedex.update_values()
        elif pokedex.events == sg.WINDOW_CLOSED:
            pokedex.window.close()
            break
    except KeyError:
        event = sg.popup_ok('CAMPO VAZIO!\n\nPor favor, insira\no nome do\nPokémon.', title='ERRO',
                            font=('Arial Black', 18), text_color='yellow')
        if event == 'OK':
            pass
        else:
            pokedex.window.close()
            break
    except json.JSONDecodeError:
        event = sg.popup_ok('POKÉMON NÃO\nENCONTRADO!\n\nOK: Continuar\nFECHAR: Parar', title='ERRO',
                            font=('Arial Black', 18), text_color='yellow')
        if event == 'OK':
            pass
        else:
            pokedex.window.close()
            break
