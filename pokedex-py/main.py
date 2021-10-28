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
        pokedex.update_err_window_off('CAMPO VAZIO!\n\nPOR FAVOR\nINSIRA O NOME\nDO POKÉMON.')
        pokedex.input_values()
        if pokedex.events == '-restart_button-':
            pokedex.update_err_window_on()
        elif pokedex.events == sg.WINDOW_CLOSED:
            pokedex.window.close()
            break
    except json.JSONDecodeError:
        pokedex.update_err_window_off('VERIFIQUE O\nNOME DO\nPOKÉMON\n\nREINICIE OU\nFECHE A\nJANELA')
        pokedex.input_values()
        if pokedex.events == '-restart_button-':
            pokedex.update_err_window_on()
        elif pokedex.events == sg.WINDOW_CLOSED:
            pokedex.window.close()
            break
