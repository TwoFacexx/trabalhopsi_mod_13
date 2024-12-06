#importa a biblioteca sqlite3
import sqlite3

#faz a conexão com a base de dados campeonatos.db, se ela não existir cria a mesma
conexao = sqlite3.connect('jogos.db')
#cria o cursor que faz com que possamos executar os queries
cursor = conexao.cursor()
 
 #Cria a tabela campeonatos se não existir, com as colunas id, nome e local
cursor.execute('''
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    local INTEGER NOT NULL
)
''')
#salva as modificações 
conexao.commit()
#fecha a conexão 
conexao.close()