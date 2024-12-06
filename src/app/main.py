#importa a biblioteca sqlite3
import sqlite3
#faz a conexão com a base de dados campeonatos.db, se ela não existir cria a mesma
conexao = sqlite3.connect('campeonatos.db')
#cria o cursor que faz com que possamos executar os queries
cursor = conexao.cursor()
 
#Cria a tabela campeonatos se não existir, com as colunas id, nome e local
cursor.execute('''
CREATE TABLE IF NOT EXISTS campeonatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    local INTEGER NOT NULL
)
''')
 
#Insere na tabela campeonatos o nome e o local do campeonato
cursor.execute('INSERT INTO campeonatos (nome, local) VALUES ("João Silva", 20)')
#salva as modificações 
conexao.commit()
 
#seleciona todos os dados da tabela camponato  
cursor.execute('SELECT * FROM campeonatos')
#retorna os dados 
resultados = cursor.fetchall()
#faz um ciclo para ler os dados em resultados e os imprime
for campeonatos in resultados:
    print(campeonatos)
 
#fecha a conexão 
conexao.close()