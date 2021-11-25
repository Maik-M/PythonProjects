import sqlite3
import PySimpleGUI as sg
from interfaces.consts import Keys, Popup
from interfaces.interface import Interface
from db.db_functions import DBFunctions
from funcs import validate_funcs as vf

########################################################################################################################
# AQUI INCIA TUDO DO SISTEMA. ESSE É O ARQUIVO DE INICIALIZAÇÃO DO SOFTWARE ############################################
########################################################################################################################

gui = Interface()
db = DBFunctions()
gui.make_login_window()
while True:
    try:
        gui.input_login_values()
        if gui.login_events == Keys.L_BUTTON_ENTRAR:
            if vf.validate_login_usuario(gui.login_values[Keys.L_INPUT_LOGIN], gui.login_values[Keys.L_INPUT_SENHA]):
                gui.login_window.hide()
                gui.make_main_window()
                while True:
                    try:
                        gui.input_main_values()
                        if gui.main_events == Keys.R_BUTTON_CADASTRAR:
                            dados = gui.return_reg()
                            db.insert_prontuario(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
                            gui.make_popup(Popup.REGISTRO_MSG)
                        if gui.main_events == Keys.R_BUTTON_LIMPAR:
                            gui.clean_tab_cadastro()
                        if gui.main_events == Keys.F_BUTTON_BUSCAR:
                            pass
                        if gui.main_events == Keys.F_BUTTON_LIMPAR:
                            pass
                        if gui.main_events == Keys.IO_BUTTON_SAIDA:
                            pass
                        if gui.main_events == Keys.IO_BUTTON_CHEGADA:
                            pass
                        if gui.main_events == Keys.IO_BUTTON_LIMPAR:
                            pass
                        if gui.main_events == sg.WINDOW_CLOSED:
                            gui.login_window.close()
                            gui.main_window.close()
                            break
                    except ValueError as error:
                        event = gui.make_error_popup(error)
                    except sqlite3.IntegrityError as error:
                        event = gui.make_error_popup(error)
        if gui.login_events == Keys.L_BUTTON_CADASTRAR:
            pass
        if gui.login_events == sg.WINDOW_CLOSED:
            break
    except ValueError as error:
        event = gui.make_error_popup(error)
