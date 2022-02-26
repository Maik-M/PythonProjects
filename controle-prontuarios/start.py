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
gui.make_new_user_window()
gui.new_user_window.hide()
while True:
    try:
        db.create_user_table()
        gui.input_login_values()
        if gui.login_events == Keys.L_NEW_USER_BUTTON:
            gui.login_window.hide()
            gui.new_user_window.un_hide()
            while True:
                try:
                    gui.input_new_user_values()
                    if gui.new_user_events == Keys.NEW_U_OK_BUTTON:
                        values = gui.return_new_user_values()
                        event = gui.make_warning_popup(Popup.NEW_USER_AGREE_MSG)
                        if event == Popup.YES:
                            db.resgister_user(values[0], values[1], values[2])
                            gui.make_popup(Popup.NEW_USER_MSG)
                        gui.clean_new_user_window()
                        gui.new_user_window.hide()
                        gui.login_window.un_hide()
                        break
                    if gui.new_user_events == Keys.NEW_U_CANCEL_BUTTON:
                        gui.clean_new_user_window()
                        gui.new_user_window.hide()
                        gui.login_window.un_hide()
                        break
                    if gui.new_user_events == sg.WINDOW_CLOSED:
                        gui.login_window.close()
                        gui.new_user_window.close()
                        break
                except ValueError as error:
                    gui.make_error_popup(error)
        if gui.login_events == Keys.L_LOGIN_BUTTON:
            db.create_record_table()
            if vf.validate_user_login(gui.login_values[Keys.L_LOGIN_INPUT], gui.login_values[Keys.L_PASSW_INPUT]):
                gui.clean_login()
                gui.login_window.hide()
                gui.make_main_window()
                gui.update_main_greetings_user()
                while True:
                    try:
                        gui.input_main_values()
                        if gui.main_events == Keys.R_REGISTER_BUTTON:
                            values = gui.return_register_values()
                            db.insert_record(values[0], values[1], values[2], values[3], values[4], values[5])
                            gui.clean_register_tab()
                            gui.make_popup(Popup.REGISTER_MSG)
                        if gui.main_events == Keys.R_CLEAN_BUTTON:
                            gui.clean_register_tab()
                        if gui.main_events == Keys.S_SEARCH_BUTTON:
                            gui.update_search_result()
                        if gui.main_events == Keys.S_CLEAN_BUTTON:
                            gui.clean_search_tab()
                        if gui.main_events == Keys.SEARCH_R_CLEAN_BUTTON:
                            gui.clean_search_result()
                        if gui.main_events == Keys.S_RETURNED_BUTTON:
                            gui.update_returned_search_result()
                        if gui.main_events == Keys.S_N_RETURNED_BUTTON:
                            gui.updaten_n_returned_search_result()
                        if gui.main_events == Keys.R_O_OUT_BUTTON:
                            values = gui.return_out_values()
                            db.update_out(values[0], values[1], values[2], values[3])
                            gui.make_popup(Popup.RECORD_OUT_MSG)
                            gui.clean_r_o_tab()
                        if gui.main_events == Keys.R_O_RETURNED_BUTTON:
                            values = gui.return_returned_values()
                            db.update_returned(values[0], values[1], values[2], values[3])
                            gui.make_popup(Popup.RECORD_RETURNED_MSG)
                            gui.clean_r_o_tab()
                        if gui.main_events == Keys.R_O_CLEAN_BUTTON:
                            gui.clean_r_o_tab()
                        if gui.main_events == Keys.EDIT_BUTTON:
                            if vf.validate_sus(gui.main_values[Keys.EDIT_DEL_SEARCH_SUS]):
                                event = gui.make_warning_popup(Popup.EDIT_MSG)
                                if event == Popup.YES:
                                    gui.return_edit_values()
                                    gui.make_popup(Popup.EDITED_MSG)
                                    gui.clean_edit_del_tab()
                        if gui.main_events == Keys.DEL_BUTTON:
                            if vf.validate_sus(gui.main_values[Keys.EDIT_DEL_SEARCH_SUS]):
                                event = gui.make_warning_popup(Popup.DELETE_MSG)
                                if event == Popup.YES:
                                    db.delete_record(gui.main_values[Keys.EDIT_DEL_SEARCH_SUS])
                                    gui.make_popup(Popup.DELETED_MSG)
                        if gui.main_events == Keys.EDIT_DEL_CLEAN_BUTTON:
                            gui.clean_edit_del_tab()
                        if gui.main_events == sg.WINDOW_CLOSED:
                            gui.login_window.close()
                            gui.new_user_window.close()
                            gui.main_window.close()
                            break
                    except ValueError as error:
                        gui.make_error_popup(error)
                    except sqlite3.IntegrityError as error:
                        gui.make_error_popup(error)
        if gui.login_events == sg.WINDOW_CLOSED:
            gui.login_window.close()
            break
    except ValueError as error:
        gui.make_error_popup(error)
