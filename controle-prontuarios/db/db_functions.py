import sqlite3

# DB name: prontuarios.db
# Table name: prontuarios

# Columns prontuarios Schema --------------
# num_sus :type INTEGER PRIMARY KEY
# nome_paciente :type TEXT NOT NULL
# nome_mae :type TEXT DEFAULT NULL
# sexo :type TEXT NOT NULL
# dt_nasc :type TEXT NOT NULL
# func_saida :type TEXT DEFAULT NULL
# func_devolucao :type TEXT DEFAULT NULL
# dtHr_saida :type TEXT DEFAULT NULL
# dtHr_devolucao :type TEXT DEFAULT NULL
# usuario TEXT :type DEFAULT NULL
# is_devolvido :type INTEGER DEFAULT=-1, 0=False, 1=True

# Columns usuarios Schema -----------------
# id :type INTEGER PRIMARY KEY
# usuario :type TEXT NOT NULL
# senha :type TEXT NOT NULL

# Constantes de controle
N_DEVOLVIDO = 0
DEVOLVIDO = 1
DEFAULT_VALUE = None


class DBFunctions:
    """Classe do DB com todos os métodos necessários."""

    @staticmethod
    def insert_prontuario(num_sus, nome_paciente, sexo, dt_nasc, usuario, nome_mae=None):
        """Cadastra novo prontuário."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO prontuarios '
                           '(num_sus, nome_paciente, nome_mae, sexo, dt_nasc, usuario) '
                           'VALUES (?, ?, ?, ?, ?, ?)',
                           (int(num_sus),
                            str(nome_paciente).upper(),
                            str(nome_mae).upper(),
                            str(sexo).upper(),
                            str(dt_nasc),
                            str(usuario).upper()))
            cursor.execute('pragma foreign_keys=ON')
            conn.commit()
        except sqlite3.IntegrityError:
            # Erro: Número do SUS já cadastrado
            raise sqlite3.IntegrityError
        except ValueError:
            # Erro de tipo de dado errado
            raise ValueError
        finally:
            conn.close()

    @staticmethod
    def select_sus(num_sus):
        """Busca prontuario pelo número do mesmo."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios WHERE num_sus=?',
                           (num_sus,))
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            raise ValueError
        finally:
            conn.close()

    @staticmethod
    def select_nome(nome_paciente):
        """Busca prontuario com o nome do paciente."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE nome_paciente=?',
                           (nome_paciente,))
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            # Erro de tipo inválido
            raise ValueError
        finally:
            conn.close()

    @staticmethod
    def select_sus_nome(num_sus, nome_paciente):
        """Busca mais precisa com número do prontuario e nome do paciente."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE num_sus=? AND nome_paciente=?',
                           (num_sus, nome_paciente))
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            # Dados faltando
            return -1
        finally:
            conn.close()

    @staticmethod
    def select_devolvidos(num_sus=None):
        """Lista todos os prontuários devolvidos."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            if num_sus == DEFAULT_VALUE:
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               (DEVOLVIDO,))
            else:
                DBFunctions.select_sus(num_sus)
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def select_nao_devolvidos(num_sus=None):
        """Lista todos os prontuários não devolvidos."""
        conn = sqlite3.connect('arquivo.db')
        try:
            if num_sus == DEFAULT_VALUE:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               (N_DEVOLVIDO,))
            else:
                DBFunctions.select_sus(num_sus)
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def update_saida(num_sus, dt_hr_saida, usuario):
        """Cadastra saída do prontuario do arquivo."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET (dtHr_saida, is_devolvido, usuario)'
                           'VALUES (?, ?, ?) '
                           'WHERE num_sus=?',
                           (dt_hr_saida, N_DEVOLVIDO, usuario, num_sus))
            cursor.execute('pragma foreign_keys=ON')
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            # Um dos dados está em branco
            return -1
        finally:
            conn.close()

    @staticmethod
    def update_entregue(num_sus, dt_hr_devolucao, usuario):
        """Cadastra devolução do prontuário no arquivo."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET (dt_devolucao, is_devolvido, usuario)'
                           'VALUES (?, ?, ?) '
                           'WHERE num_sus=?',
                           (dt_hr_devolucao, DEVOLVIDO, usuario, num_sus))
            cursor.execute('pragma foreign_keys=ON')
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            # Um dos dados está em branco
            return -1
        finally:
            conn.close()

    @staticmethod
    def delete_prontuario(num_sus):
        """Deleta prontuarios."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM prontuarios '
                           'WHERE num_sus=?',
                           (num_sus,))
            cursor.execute('pragma foreign_keys=ON')
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def select_all():
        """Lista todos os já cadastrados do DB."""
        conn = sqlite3.connect('arquivo.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios')
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'Erro: {erro}')
        finally:
            conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect('arquivo.db')
    cursor = conn.cursor()
    try:
        # cursor.execute('INSERT INTO prontuarios (num_sus, nome_paciente, sexo, dt_nasc, usuario) '
        #                'VALUES (?, ?, ?, ?, ?)',
        #                (123456789123456, 'Fulano Teste da Silva', 'M', '2010-08-01', 1))
        # conn.commit()
        # cursor.execute('DROP TABLE IF EXISTS prontuarios')
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
                       'FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario))'
                       ' WITHOUT ROWID;')
        cursor.execute('pragma foreign_keys=ON')
        # cursor.execute('INSERT INTO prontuarios (num_sus, nome_paciente, sexo, dt_nasc, usuario) '
        #                'VALUES (?, ?, ?, ?, ?)',
        #                (123456789123458, 'Teste de Souza', 'M', '2010-08-01', 1))
        # conn.commit()
        cursor.execute('SELECT * FROM prontuarios')
        print(cursor.fetchall())
    except sqlite3.Error as e:
        print(e)

    # conn = sqlite3.connect('arquivo.db')
    # cursor = conn.cursor()
    # try:
    #     cursor.execute('CREATE TABLE IF NOT EXISTS usuarios ('
    #                    'id_usuario INTEGER PRIMARY KEY,'
    #                    'usuario TEXT NOT NULL UNIQUE,'
    #                    'senha TEXT NOT NULL);')
    #     cursor.execute('pragma foreign_keys=ON')
    #     cursor.execute('CREATE TABLE IF NOT EXISTS prontuarios ('
    #                    'num_sus INTEGER PRIMARY KEY,'
    #                    'nome_paciente TEXT NOT NULL,'
    #                    'nome_mae TEXT DEFAULT NULL,'
    #                    'sexo TEXT NOT NULL,'
    #                    'dt_nasc TEXT NOT NULL,'
    #                    'func_saida TEXT DEFAULT NULL,'
    #                    'func_devolucao TEXT DEFAULT NULL,'
    #                    'dtHr_saida TEXT DEFAULT NULL,'
    #                    'dtHr_devolucao TEXT DEFAULT NULL,'
    #                    'usuario TEXT DEFAULT NULL,'
    #                    'is_devolvido INTEGER DEFAULT -1,'
    #                    'FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario))'
    #                    ' WITHOUT ROWID;')
    # except sqlite3.Error as e:
    #     print(e)

    # iniciar = DBFunctions()
    # iniciar.delete_prontuario(456)

    # print(iniciar.select_all())
    # iniciar.update_saida(456202912078643, '01-11-2021 22:41')
    # print(iniciar.select_sus(456202912078643))
    # iniciar.update_entregue(456202912078643, '02-11-2021 14:22')
    # print(iniciar.select_sus(456202912078643))

    # iniciar.insert_prontuario(123456789987654, 'João', 'Breno')

    # conn = sqlite3.connect('arquivo.db')
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM prontuarios WHERE nome=:nome', ({'nome': 'laura'}))
    # print(len(cursor.fetchall()))

    # conn = sqlite3.connect('arquivo.db')
    # cursor = conn.cursor()
    # try:
    #     cursor.execute('CREATE TABLE prontuarios ('
    #                    'num_sus INTEGER PRIMARY KEY,'
    #                    'nome_paciente TEXT NOT NULL,'
    #                    'nome_mae TEXT DEFAULT NULL,'
    #                    'sexo TEXT NOT NULL,'
    #                    'dt_nasc TEXT NOT NULL,'
    #                    'func_saida TEXT DEFAULT NULL,'
    #                    'func_devolucao TEXT DEFAULT NULL,'
    #                    'dtHr_saida TEXT DEFAULT NULL,'
    #                    'dtHr_devolucao TEXT DEFAULT NULL,'
    #                    'usuario TEXT DEFAULT NULL,'
    #                    'is_devolvido INTEGER DEFAULT -1)'
    #                    'WITHOUT ROWID;')
    # except sqlite3.Error as e:
    #     print(f'ERRO: {e}')
    # finally:
    #     conn.close()

    # conn = sqlite3.connect('arquivo.db')
    # cursor = conn.cursor()
    # try:
    #     cursor.execute('DROP TABLE IF EXISTS prontuarios')
    # except sqlite3.Error as e:
    #     print(f'ERRO: {e}')
    # finally:
    #     conn.close()
