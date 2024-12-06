#importa a biblioteca sqlite3
import sqlite3
#faz a conexão com a base de dados campeonatos.db, se ela não existir cria a mesma
conexao = sqlite3.connect('jogos.db')
#cria o cursor que faz com que possamos executar os queries
cursor = conexao.cursor()
 
#Insere na tabela campeonatos o nome e o local do campeonato
cursor.execute('INSERT INTO jogos (nome, genero) VALUES (?, ?)', ('The Legend of Zelda', 'Ação/Aventura'))

#salva as modificações 
conexao.commit()
#fecha a conexão 
conexao.close()