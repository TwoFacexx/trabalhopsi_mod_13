#importa a biblioteca sqlite3
import sqlite3
#faz a conexão com a base de dados campeonatos.db, se ela não existir cria a mesma
conexao = sqlite3.connect('jogos.db')
#cria o cursor que faz com que possamos executar os queries
cursor = conexao.cursor()
 
#seleciona todos os dados da tabela camponato  
cursor.execute('SELECT * FROM jogos')
#retorna os dados 
resultados=cursor.fetchall()
#faz um ciclo para ler os dados em resultados e os imprime
for i in resultados:
    print(i)

#fecha a conexão 
conexao.close()