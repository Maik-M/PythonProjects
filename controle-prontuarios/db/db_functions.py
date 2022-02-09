import sqlite3
from funcs import password_funcs as hashing

# DB name: prontuarios.db
# Table name: prontuarios
# Table name: usuarios

# Columns prontuarios Schema --------------
# num_sus INTEGER PRIMARY KEY
# nome_paciente TEXT NOT NULL
# nome_mae TEXT DEFAULT NULL
# sexo TEXT NOT NULL
# dt_nasc TEXT NOT NULL
# func_saida TEXT DEFAULT NULL
# func_devolucao TEXT DEFAULT NULL
# dtHr_saida TEXT DEFAULT NULL
# dtHr_devolucao TEXT DEFAULT NULL
# usuario INTEGER NOT NULL
# is_devolvido INTEGER DEFAULT -1

# Columns usuarios Schema -----------------
# id_usuario INTEGER PRIMARY KEY
# nome_usuario TEXT NOT NULL
# usuario TEXT UNIQUE NOT NULL
# senha TEXT NOT NULL
# salt TEXT NOT NULL

# Constantes de controle
N_DEVOLVIDO = 0
DEVOLVIDO = 1
DEFAULT_VALUE = None


class DBFunctions:
    """Classe do DB com todos os métodos necessários."""

    ###################
    # Prontuários #####-------------------------------------------------------------------------------------------------
    ###################
    @staticmethod
    def create_table_prontuarios():
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
    def insert_prontuario(num_sus, nome_paciente, sexo, dt_nasc, usuario, nome_mae=None):
        """Cadastra novo prontuário."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            DBFunctions.create_table_prontuarios()
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('INSERT INTO prontuarios '
                           '(num_sus, nome_paciente, nome_mae, sexo, dt_nasc, usuario) '
                           'VALUES (?, ?, ?, ?, ?, ?)',
                           (int(num_sus), str(nome_paciente).upper(), str(nome_mae).upper(), str(sexo).upper(), str(dt_nasc), int(usuario)))
            conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError(19*' '+'ERRO!\nAlgo de errado aconteceu!\n'
                                         'Verifique se o prontuário já está cadastrado ou se algum campo está em branco.')
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_sus(num_sus):
        """Busca prontuario pelo número do mesmo."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios WHERE num_sus=?',
                           (int(num_sus),))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_nome(nome_paciente):
        """Busca prontuario com o nome do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE nome_paciente LIKE ? OR nome_paciente=?',
                           (f'{str(nome_paciente).upper()}%', str(nome_paciente).upper()))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_sus_nome(num_sus, nome_paciente):
        """Busca mais precisa com número do prontuario e nome do paciente."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE num_sus=? AND nome_paciente=?',
                           (int(num_sus), str(nome_paciente).upper()))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_nasc(dt_nasc):
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE dt_nasc LIKE ? OR dt_nasc=?',
                           (f'{str(dt_nasc)}%', str(dt_nasc)))
            return cursor.fetchall()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def select_devolvidos(num_sus=None):
        """Lista todos os prontuários devolvidos."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            if num_sus == DEFAULT_VALUE:
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               (DEVOLVIDO,))
                return cursor.fetchall()
            else:
                DBFunctions.select_sus(num_sus)
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def select_nao_devolvidos(num_sus=None):
        """Lista todos os prontuários não devolvidos."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            if num_sus == DEFAULT_VALUE:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               (N_DEVOLVIDO,))
                return cursor.fetchall()
            else:
                DBFunctions.select_sus(num_sus)
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def update_saida(num_sus, dt_hr_saida, usuario, funcionario):
        """Cadastra saída do prontuario do arquivo."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('UPDATE prontuarios '
                           'SET func_saida=?, dtHr_saida=?, is_devolvido=?, usuario=? '
                           'WHERE num_sus=?',
                           (str(funcionario).upper(), str(dt_hr_saida), N_DEVOLVIDO, int(usuario), int(num_sus)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def update_entregue(num_sus, dt_hr_devolucao, func_devolucao, usuario):
        """Cadastra devolução do prontuário no arquivo."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('UPDATE prontuarios '
                           'SET func_devolucao=?, dtHr_devolucao=?, is_devolvido=?, usuario=? '
                           'WHERE num_sus=?',
                           (str(func_devolucao).upper(), str(dt_hr_devolucao), DEVOLVIDO, int(usuario), int(num_sus)))
            conn.commit()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def delete_prontuario(num_sus):
        """Deleta prontuarios."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('DELETE FROM prontuarios '
                           'WHERE num_sus=?',
                           (int(num_sus),))
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def select_all_prontuarios():
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
    def create_table_usuarios():
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
    def resgister_usuario(nome_usuario, usuario, senha):
        """Cadastra novo usuário."""
        hash_senha, salt = hashing.hashing_password(senha)
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            DBFunctions.create_table_usuarios()
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('INSERT INTO usuarios (nome_usuario, usuario, senha, salt) '
                           'VALUES (?, ?, ?, ?)',
                           (str(nome_usuario), str(usuario), str(hash_senha), str(salt)))
            conn.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError('ERRO: Usuário já cadastrado!')
        except ValueError as error:
            raise error
        finally:
            conn.close()

    @staticmethod
    def delete_usuario(usuario):
        """Deleta usuário criado (só o adm pode fazer isso)."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('DELETE FROM usuarios '
                           'WHERE usuario=?',
                           (str(usuario,)))
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def select_usuario(usuario):
        """Retorna os dados do usuário passado."""
        conn = sqlite3.connect('./db/arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('pragma foreign_keys=ON')
            cursor.execute('SELECT * FROM usuarios '
                           'WHERE usuario=?',
                           (str(usuario),))
            return cursor.fetchone()
        except sqlite3.Error as BD_Error:
            raise BD_Error
        finally:
            conn.close()

    @staticmethod
    def select_all_usuarios():
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


if __name__ == '__main__':
    pass
    # db = DBFunctions()
    # conn = sqlite3.connect('arquivo.db')
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM prontuarios')
    # dados = cursor.fetchall()
    # for key, value in enumerate(dados):
    #     [print(i) for i in value if key is not None]
    # print(db.select_all_usuarios())
    # db.resgister_usuario('Maik Marques', 'Maik4521', 'A1515151sss')
    # hash_senha = hashing.hashing_validate_password('', usuario[3])
    # if usuario[2] == hash_senha:
    #     print(True)
    # else:
    #     print(False)
    # conn = sqlite3.connect('arquivo.db')
    # cursor = conn.cursor()
    # try:
    # cursor.execute('INSERT INTO prontuarios (num_sus, nome_paciente, sexo, dt_nasc, usuario) '
    #                'VALUES (?, ?, ?, ?, ?)',
    #                (123456789123456, 'Fulano Teste da Silva', 'M', '2010-08-01', 1))
    # conn.commit()
    # cursor.execute('DROP TABLE IF EXISTS prontuarios')
    # cursor.execute('CREATE TABLE IF NOT EXISTS prontuarios ('A1515151sss
    #                'num_sus INTEGER PRIMARY KEY,'
    #                'nome_paciente TEXT NOT NULL,'
    #                'nome_mae TEXT DEFAULT NULL,'
    #                'sexo TEXT NOT NULL,'
    #                'dt_nasc TEXT NOT NULL,'
    #                'func_saida TEXT DEFAULT NULL,'
    #                'func_devolucao TEXT DEFAULT NULL,'
    #                'dtHr_saida TEXT DEFAULT NULL,'
    #                'dtHr_devolucao TEXT DEFAULT NULL,'
    #                'usuario INTEGER NOT NULL,'
    #                'is_devolvido INTEGER DEFAULT -1,'
    #                'FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario))'
    #                ' WITHOUT ROWID;')
    # cursor.execute('pragma foreign_keys=ON')
    # cursor.execute('CREATE TABLE IF NOT EXISTS usuarios ('
    #                'usuario_id INTEGER PRIMARY KEY,'
    #                'usuario TEXT NOT NULL,'
    #                'senha TEXT NOT NULL,'
    #                'salt TEXT NOT NULL)')
    # cursor.execute('INSERT INTO prontuarios (num_sus, nome_paciente, sexo, dt_nasc, usuario) '
    #                'VALUES (?, ?, ?, ?, ?)',
    #                (123456789123458, 'Teste de Souza', 'M', '2010-08-01', 1))
    # conn.commit()
    #     cursor.execute('SELECT * FROM usuarios')
    #     print(cursor.fetchall())
    # except sqlite3.ErrorPopup as e:
    #     print(e)
