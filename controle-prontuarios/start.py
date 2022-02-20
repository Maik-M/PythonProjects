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
                gui.clean_login()
                gui.login_window.hide()
                gui.make_main_window()
                while True:
                    try:
                        gui.input_main_values()
                        if gui.main_events == Keys.R_BUTTON_CADASTRAR:
                            dados = gui.return_register_values()
                            db.insert_prontuario(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
                            gui.clean_tab_cadastro()
                            gui.make_popup(Popup.REGISTRO_MSG)
                        if gui.main_events == Keys.R_BUTTON_LIMPAR:
                            gui.clean_tab_cadastro()
                        if gui.main_events == Keys.S_BUTTON_BUSCAR:
                            gui.update_search_result()
                        if gui.main_events == Keys.S_BUTTON_LIMPAR:
                            gui.clean_search()
                        if gui.main_events == Keys.SEARCH_R_BUTTON_LIMPAR:
                            gui.clean_search_result()
                        if gui.main_events == Keys.S_BUTTON_DEVOLVIDOS:
                            gui.update_search_result_devolvidos()
                        if gui.main_events == Keys.S_BUTTON_N_DEVOLVIDOS:
                            gui.update_search_result_n_devolvidos()
                        if gui.main_events == Keys.IO_BUTTON_SAIDA:
                            dados = gui.return_out_values()
                            db.update_saida(dados[0], dados[1], dados[2], dados[3])
                            gui.make_popup(Popup.SAIDA_PRONTUARIO_MSG)
                            gui.clean_io()
                        if gui.main_events == Keys.IO_BUTTON_CHEGADA:
                            dados = gui.return_in_values()
                            db.update_entregue(dados[0], dados[1], dados[2], dados[3])
                            gui.make_popup(Popup.DEVOLUCAO_PRONTUARIO_MSG)
                            gui.clean_io()
                        if gui.main_events == Keys.IO_BUTTON_LIMPAR:
                            gui.clean_io()
                        if gui.main_events == Keys.EDIT_BUTTON:
                            if vf.validate_sus(gui.main_values[Keys.EDIT_DEL_SEARCH_SUS]):
                                event = gui.make_warning_popup(Popup.EDITAR_MSG)
                                if event == Popup.YES:
                                    gui.return_edit_values()
                                    gui.make_popup(Popup.EDITADO_MSG)
                                    gui.clean_edit_del()
                        if gui.main_events == Keys.DEL_BUTTON:
                            if vf.validate_sus(gui.main_values[Keys.EDIT_DEL_SEARCH_SUS]):
                                event = gui.make_warning_popup(Popup.EXCLUIR_MSG)
                                if event == Popup.YES:
                                    db.delete_prontuario(gui.main_values[Keys.EDIT_DEL_SEARCH_SUS])
                                    gui.make_popup(Popup.EXCLUIDO_MSG)
                        if gui.main_events == Keys.EDIT_DEL_LIMPAR_BUTTON:
                            gui.clean_edit_del()
                        if gui.main_events == sg.WINDOW_CLOSED:
                            gui.login_window.close()
                            gui.main_window.close()
                            break
                    except ValueError as error:
                        gui.make_error_popup(error)
                    except sqlite3.IntegrityError as error:
                        gui.make_error_popup(error)
        if gui.login_events == Keys.L_BUTTON_CADASTRAR:
            pass
        if gui.login_events == sg.WINDOW_CLOSED:
            break
    except ValueError as error:
        gui.make_error_popup(error)
