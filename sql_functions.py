from mock_data import lista_atracoes
import sqlite3

def connect_to_database():
  sqliteConnection = None
  try:

    sqliteConnection = sqlite3.connect('main-database.db')
    print('Banco de dados conectado com sucesso.')
  except sqlite3.Error as e:
    print(e)

  cursor = sqliteConnection.cursor()

  sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS atracoes (
                              id INTEGER PRIMARY KEY,
                              nome TEXT NOT NULL,
                              descricao text NOT NULL,
                              tipo text NOT NULL,
                              horarios text NOT NULL
                              );'''
    
  sqlite_create_table_usuarios = '''CREATE TABLE IF NOT EXISTS usuarios (
                                    id INTEGER PRIMARY KEY,
                                    senha TEXT NOT NULL,
                                    user_id TEXT NOT NULL,
                                    user_nome TEXT NOT NULL,
                                    user_cpf TEXT NOT NULL,
                                    user_num TEXT NOT NULL
                                );'''

  cursor.execute(sqlite_create_table_usuarios)
  cursor.execute(sqlite_create_table_query)

  # create_attractions(sqliteConnection)
  sqliteConnection.commit()
    
  return sqliteConnection

def create_attractions(connection):
  cursor = connection.cursor()

  create_attraction_sql = 'INSERT INTO atracoes (nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?);'

  for atracao in lista_atracoes:
    cursor.execute(create_attraction_sql, (atracao['NOME'], atracao['DESCRICAO'], atracao['TIPO'], atracao['HORARIOS']))

  connection.commit()

def create_user(connection, user):
  cursor = connection.cursor()

  create_user_sql = 'INSERT INTO usuarios (nome, descricao, tipo, horarios) VALUES (?, ?, ?, ?);'

  cursor.execute(create_user_sql, (user['NOME'], user['DESCRICAO'], user['TIPO'], user['HORARIOS']))

  connection.commit()

def select_attractions(connection):
  cursor = connection.cursor()

  cursor.execute('SELECT * FROM atracoes')

  rows = cursor.fetchall()

  atracoes = []
  tupla_nomes = ('ID', 'NOME', 'DESCRICAO', 'TIPO', 'HORARIOS')

  for row in rows:
    atracoes.append((dict(zip(tupla_nomes, row))))

  return atracoes

def select_users(connection):
  cursor = connection.cursor()

  cursor.execute('SELECT * FROM usuarios')

  rows = cursor.fetchall()

  atracoes = []
  tupla_nomes = ('ID', 'NOME', 'DESCRICAO', 'TIPO', 'HORARIOS')

  for row in rows:
    atracoes.append((dict(zip(tupla_nomes, row))))

  return atracoes

def get_attractions(connection):
  atracoes = select_attractions(connection)

  for atracao in atracoes:
    if "," in atracao['HORARIOS']:
      atracao['HORARIOS'] = atracao['HORARIOS'].split(',')
    else:
     atracao['HORARIOS'] = atracao['HORARIOS'].split()

  return atracoes