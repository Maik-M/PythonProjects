import PySimpleGUI as sg
from interfaces.consts import Keys, Popup
from interfaces.interface import Interface
from db.db_functions import DBFunctions
from funcs import validate_funcs as vf


##################
# Start ########## -----------------------------------------------------------------------------------------------------
##################


gui = Interface()
db = DBFunctions()
gui.make_login_window()
while True:
    try:
        gui.input_login_values()
        if gui.login_events == Keys.L_BUTTON_ENTRAR:
            if vf.validate_login_usuario(gui.login_values[Keys.L_INPUT_LOGIN], gui.login_values[Keys.L_INPUT_SENHA]):
                gui.login_window.close()
                gui.make_main_window()
                while True:
                    try:
                        gui.input_main_values()
                        if gui.main_events == Keys.R_BUTTON_CADASTRAR:
                            if vf.validate_register(gui.return_reg()[0], gui.return_reg()[1], gui.return_reg()[2], gui.return_reg()[3], gui.return_reg()[4]):
                                if db.insert_prontuario(gui.return_reg()[0], gui.return_reg()[1], gui.return_reg()[2], gui.return_reg()[3], gui.return_reg()[4]):
                                    gui.make_popup(Popup.REGISTRO_MSG)
                        if gui.main_events == Keys.R_BUTTON_LIMPAR:
                            pass
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
                            gui.main_window.close()
                            break
                    except ValueError as error:
                        event = gui.make_error_popup(error)
                        if event == 'OK':
                            pass
                        else:
                            gui.main_window.close()
                            break
        if gui.login_events == Keys.L_BUTTON_CADASTRAR:
            break
        if gui.login_events == sg.WINDOW_CLOSED:
            break
    except ValueError as error:
        event = gui.make_error_popup(error)
        if event == 'OK':
            pass
        else:
            gui.main_window.close()
            break
