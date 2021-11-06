import sqlite3

# DB name: prontuarios.db
# Table name: prontuarios

# Columns --------------
# id :type primary key
# num_sus :type integer UNIQUE
# nome :type text NOT NULL
# sobrenome :type text DEFAULT NULL
# data_saida :type text DEFAULT NULL
# data_devolucao :type text DEFAULT NULL
# data_ultima_internacao :type text DEFAULT NULL
# is_devolvido :type integer but 0=False, 1=True DEFAULT=-1

# Constantes de controle
N_DEVOLVIDO = 0
DEVOLVIDO = 1
DEFAULT_VALUE = None


class DBFunctions:
    """Classe do DB com todos os métodos necessários."""
    @staticmethod
    def insert_prontuario(num_sus, nome, sobrenome=None):
        """Cadastra novo prontuário."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO prontuarios '
                           '(num_sus, nome, sobrenome) '
                           'VALUES (?, ?, ?)',
                           (int(num_sus),
                            str(nome).lower(),
                            str(sobrenome.lower())))
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
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios WHERE num_sus=:num_sus',
                           ({'num_sus': int(num_sus)}))
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            raise ValueError
        finally:
            conn.close()

    @staticmethod
    def select_nome(nome):
        """Busca prontuario com o nome do paciente."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE nome_paciente=:nome_paciente',
                           ({'nome_paciente': str(nome)}))
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            # Erro de tipo inválido
            raise ValueError
        finally:
            conn.close()

    @staticmethod
    def select_sus_nome(num_sus, nome):
        """Busca mais precisa com número do prontuario e nome do paciente."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios '
                           'WHERE num_sus=:num_sus AND nome_paciente=:nome_paciente',
                           ({'num_sus': int(num_sus),
                             'nome_paciente': str(nome)}))
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
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            if num_sus == DEFAULT_VALUE:
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=?',
                               ({'is_devolvido': DEVOLVIDO}))
            else:
                DBFunctions.select_sus(num_sus)
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def select_nao_devolvidos(num_sus=None):
        """Lista todos os prontuários não devolvidos."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            if num_sus == DEFAULT_VALUE:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM prontuarios '
                               'WHERE is_devolvido=:is_devolvido',
                               ({'is_devolvido': N_DEVOLVIDO}))
            else:
                DBFunctions.select_sus(num_sus)
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def update_saida(num_sus, data_saida):
        """Cadastra saída do prontuario do arquivo."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET data_saida=:data_saida, '
                           'is_devolvido=:is_devolvido '
                           'WHERE num_sus=:num_sus',
                           ({'data_saida': data_saida,
                             'is_devolvido': N_DEVOLVIDO,
                             'num_sus': num_sus}))
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        except ValueError:
            # Um dos dados está em branco
            return -1
        finally:
            conn.close()

    @staticmethod
    def update_entregue(num_sus, data_devolucao):
        """Cadastra devolução do prontuário no arquivo."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE prontuarios '
                           'SET data_devolucao=:data_devolucao, '
                           'is_devolvido=:devolvido '
                           'WHERE num_sus=:num_sus',
                           ({'data_devolucao': data_devolucao,
                             'devolvido': DEVOLVIDO,
                             'num_sus': int(num_sus)}))
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
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM prontuarios '
                           'WHERE num_sus=:num_sus',
                           ({'num_sus': num_sus}))
            conn.commit()
        except sqlite3.Error as erro:
            print(f'ERRO: {erro}')
        finally:
            conn.close()

    @staticmethod
    def select_all():
        """Lista todos os já cadastrados do DB."""
        conn = sqlite3.connect('prontuarios.db')
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM prontuarios')
            return cursor.fetchall()
        except sqlite3.Error as erro:
            print(f'Erro: {erro}')
        finally:
            conn.close()


if __name__ == '__main__':
    pass
    # iniciar = DBFunctions()
    # iniciar.delete_prontuario(456)

    # print(iniciar.select_all())
    # iniciar.update_saida(456202912078643, '01-11-2021 22:41')
    # print(iniciar.select_sus(456202912078643))
    # iniciar.update_entregue(456202912078643, '02-11-2021 14:22')
    # print(iniciar.select_sus(456202912078643))

    # iniciar.insert_prontuario(123456789987654, 'João', 'Breno')

    # conn = sqlite3.connect('prontuarios.db')
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM prontuarios WHERE nome=:nome', ({'nome': 'laura'}))
    # print(len(cursor.fetchall()))

    # conn = sqlite3.connect('prontuarios.db')
    # cursor = conn.cursor()
    # try:
    #     cursor.execute('CREATE TABLE prontuarios ('
    #                    'id INTEGER PRIMARY KEY,'
    #                    'num_sus INTEGER NOT NULL UNIQUE,'
    #                    'nome TEXT NOT NULL,'
    #                    'sobrenome TEXT DEFAULT NULL,'
    #                    'data_saida TEXT DEFAULT NULL,'
    #                    'data_devolucao TEXT DEFAULT NULL,'
    #                    'data_internacao_paciente text NULL,'
    #                    'is_devolvido INTEGER DEFAULT -1)')
    # except sqlite3.Error as e:
    #     print(f'ERRO: {e}')
    # finally:
    #     conn.close()

    # conn = sqlite3.connect('prontuarios.db')
    # cursor = conn.cursor()
    # try:
    #     cursor.execute('DROP TABLE IF EXISTS prontuarios')
    # except sqlite3.Error as e:
    #     print(f'ERRO: {e}')
    # finally:
    #     conn.close()

# 'CREATE TABLE prontuarios ('
# 'id INTEGER PRIMARY KEY,'
# 'num_sus INTEGER UNIQUE,'
# 'nome TEXT NOT NULL,'
# 'sobrenome TEXT DEFAULT "",'
# 'data_saida TEXT DEFAULT "",'
# 'data_devolucao TEXT DEFAULT "",'
# 'data_internacao_paciente text "",'
# 'is_devolvido INTEGER DEFAULT -1)'
