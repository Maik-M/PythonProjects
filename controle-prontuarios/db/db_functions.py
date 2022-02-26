import sqlite3
from funcs import password_funcs as hashing

# Constantes de controle
N_RETURNED = 0
RETURNED = 1
DEFAULT_VALUE = None


class DBFunctions:
    """Classe do DB com todos os métodos necessários."""

    ###################
    # Prontuários #####-------------------------------------------------------------------------------------------------
    ###################
    @staticmethod
    def create_record_table():
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS prontuarios ('
                           'num_sus INTEGER PRIMARY KEY,'
                           'nome_paciente TEXT NOT NULL,'
                           'nome_mae TEXT DEFAULT NULL,'
                           'sexo TEXT NOT NULL,'
                           'dt_nasc TEXT NOT NULL,'
                           'func_saida TEXT DEFAULT NULL,'
                           'func_devolucao TEXT DEFAULT NULL,'
                           'dtHr_saida TEXT DEFAULT NULL,'
                           'dtHr_devolucao TEXT DEFAULT NULL,'
                           'usuario INTEGER NOT NULL,'
                           'is_devolvido INTEGER DEFAULT -1,'
                           'FOREIGN KEY (usuario) REFERENCES usuarios (usuario_id))'
                           ' WITHOUT ROWID;')
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def insert_record(sus_number, patient_name, gender, birth_date, user, mother=None):
        """Cadastra novo prontuário."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            DBFunctions.create_record_table()
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('INSERT INTO prontuarios '
                           '(num_sus, nome_paciente, nome_mae, sexo, dt_nasc, usuario) '
                           'VALUES (?, ?, ?, ?, ?, ?)',
                           (int(sus_number), str(patient_name).upper(), str(mother).upper(), str(gender).upper(), str(birth_date), int(user)))
            conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError(19*' '+'ERRO!\nAlgo de errado aconteceu!\n'
                                         'Verifique se o prontuário já está cadastrado ou se algum campo está em branco.')
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_sus(sus_number):
        """Busca prontuario pelo número do SUS."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios WHERE num_sus=?',
                           (int(sus_number),))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_name(patient_name):
        """Busca prontuario com o nome do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE nome_paciente LIKE ? OR nome_paciente=?',
                           (f'{str(patient_name).upper()}%', str(patient_name).upper()))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_sus_name(sus_number, patient_name):
        """Busca mais precisa com número do prontuario e nome do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE num_sus=? AND nome_paciente=?',
                           (int(sus_number), str(patient_name).upper()))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_birth(birth_date):
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE dt_nasc LIKE ? OR dt_nasc=?',
                           (f'{str(birth_date)}%', str(birth_date)))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_returned(sus_number=None):
        """Lista todos os prontuários devolvidos."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            if sus_number == DEFAULT_VALUE:
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               (RETURNED,))
                return cursor.fetchall()
            else:
                DBFunctions.select_sus(sus_number)
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def select_n_returned(sus_number=None):
        """Lista todos os prontuários não devolvidos."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            if sus_number == DEFAULT_VALUE:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               (N_RETURNED,))
                return cursor.fetchall()
            else:
                DBFunctions.select_sus(sus_number)
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def update_out(sus_number, dt_hr_out, user, employee):
        """Cadastra saída do prontuario do arquivo."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('UPDATE prontuarios '
                           'SET func_saida=?, func_devolucao=?, dtHr_saida=?, dtHr_devolucao=?, is_devolvido=?, usuario=? '
                           'WHERE sus_number=?',
                           (str(employee).upper(), None, str(dt_hr_out), None, N_RETURNED, int(user), int(sus_number)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def update_returned(sus_number, dt_hr_returned, employee_returned, user):
        """Cadastra devolução do prontuário no arquivo."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('UPDATE prontuarios '
                           'SET func_devolucao=?, dtHr_devolucao=?, is_devolvido=?, usuario=? '
                           'WHERE num_sus=?',
                           (str(employee_returned).upper(), str(dt_hr_returned), RETURNED, int(user), int(sus_number)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def update_name(patient_name, sus_number):
        """Atualiza o nome do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET nome_paciente=? '
                           'WHERE num_sus=?',
                           (str(patient_name).upper(), int(sus_number)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def update_mother(mother, sus_number):
        """Atualiza o nome da mae do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET nome_mae=? '
                           'WHERE num_sus=?',
                           (str(mother).upper(), int(sus_number)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def update_gender(gender, sus_number):
        """Atualiza o gender do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET sexo=? '
                           'WHERE num_sus=?',
                           (str(gender).upper(), int(sus_number)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def update_birth(birth_date, sus_number):
        """Atualiza a data de nascimento do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET dt_nasc=? '
                           'WHERE num_sus=?',
                           (str(birth_date), int(sus_number)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def delete_record(sus_number):
        """Deleta prontuarios."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('DELETE FROM prontuarios '
                           'WHERE num_sus=?',
                           (int(sus_number),))
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def select_all_records():
        """Lista todos os já cadastrados do DB."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('SELECT * FROM prontuarios')
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    ###################
    # Usuários ########-------------------------------------------------------------------------------------------------
    ###################
    @staticmethod
    def create_user_table():
        """Cria tabela usuarios de não existir."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('CREATE TABLE IF NOT EXISTS usuarios ('
                           'usuario_id INTEGER PRIMARY KEY,'
                           'nome_usuario TEXT NOT NULL,'
                           'usuario TEXT UNIQUE NOT NULL,'
                           'senha TEXT NOT NULL,'
                           'salt TEXT NOT NULL)')
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def resgister_user(user_name, user, password):
        """Cadastra novo usuário."""
        hash_password, salt = hashing.hashing_password(password)
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            DBFunctions.create_user_table()
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('INSERT INTO usuarios (nome_usuario, usuario, senha, salt) '
                           'VALUES (?, ?, ?, ?)',
                           (str(user_name).upper(), str(user), str(hash_password), str(salt)))
            conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError('ERRO: Usuário já cadastrado!')
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def delete_user(user):
        """Deleta usuário criado (só o adm pode fazer isso)."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('DELETE FROM usuarios '
                           'WHERE usuario=?',
                           (str(user,)))
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def select_user(user):
        """Retorna os dados do usuário passado."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('SELECT * FROM usuarios '
                           'WHERE usuario=?',
                           (str(user),))
            return cursor.fetchone()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def select_user_id(user_id):
        """Retorna os dados do usuário passado pelo ID."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('SELECT * FROM usuarios '
                           'WHERE usuario_id=?',
                           (int(user_id),))
            return cursor.fetchone()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def update_password(user_name, new_password):
        """Atualiza a senha do usuário."""
        hash_password, salt = hashing.hashing_password(new_password)
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            # DBFunctions.create_table_usuarios()
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('UPDATE usuarios '
                           'SET senha=?, salt=? '
                           'WHERE usuario=?',
                           (str(hash_password), str(salt), str(user_name)))
            conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError('ERRO: Usuário já cadastrado!')
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_all_users():
        """Retorna lista de todos usuários cadastradaos (só o adm tem acesso)."""
        conn = sqlite3.connect('../db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('SELECT * FROM usuarios')
            print(cursor.fetchall())
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()
