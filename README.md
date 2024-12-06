Estrutura recomendada para o projeto final do módulo 15:

O trabalho foi realizado para a gestão de campeonatos e suas principais informações.

campeonatos_create.py: importa a biblioteca sqlite3 cria a base de dados campeonatos.db e se conecta a ela, além de também criar a tabela campeonatos (tabela mãe) com os campos de id ( INT, que usa autoincrement, ou seja, o programa dá o valor para o id), o nome do campeonato (TEXT) e o local onde o campeonato ocorre (TEXT) usando INT e TEXT como tipos de variáveis.

maiores_campeoes_create.py: importa a biblioteca sqlite3 se conecta a base de dados campeonatos.db, além de também criar a tabela maior_campeao com os campos de id ( INT, que usa autoincrement, ou seja, o programa dá o valor para o id), o nome do maior campeão (TEXT), e o campeonato (TEXT) usando INT e TEXT como tipos de variáveis.

numero_de_participantes_create.py: importa a biblioteca sqlite3 se conecta a base de dados campeonatos.db, além de também criar a tabela numero_participantes com os campos de id ( INT, que usa autoincrement, ou seja, o programa dá o valor para o id), o número de participantes (TEXT) e o campeonato (TEXT) usando INT e TEXT como tipos de variáveis.

campeonatos_insert.py: importa a biblioteca sqlite3 se conecta a base de dados campeonatos.db, cria a lista campeonatos com 50 dados e insere na tabela campeonatos os valores de nome e local que vai buscar a lista campeonatos. 

maiores_campeoes_insert.py: importa a biblioteca sqlite3 se conecta a base de dados campeonatos.db, cria a lista maiores_campeoes com 50 dados e insere na tabela campeonatos os valores dos nomes dos maiores campeões e o nome do campeonato que vai buscar a lista maiores_campeoes. 

numero_de_participantes_insert.py: importa a biblioteca sqlite3, se conecta a base de dados campeonatos.db, cria a lista numero_participantes com 50 dados e insere na tabela campeonatos os valores do número de participantes e o nome do campeonato que vai buscar a lista numero_participantes. 

campeonatos_read.py: importa a biblioteca sqlite3, se conecta a base de dados campeonatos.db e seleciona todos os dados da tabela campeonatos, após isso, utiliza um ciclo for para ler todos os dados e imprime eles.

maiores_campeoes_read.py: importa a biblioteca sqlite3, se conecta a base de dados campeonatos.db e seleciona todos os dados da tabela maior_campeao, após isso, utiliza um ciclo for para ler todos os dados da tabela e imprime eles.

numero_de_participantes_read.py: importa a biblioteca sqlite3, se conecta a base de dados campeonatos.db e seleciona todos os dados da tabela numero_participantes, após isso, utiliza um ciclo for para ler todos os dados da tabela e imprime eles.

epbjc/
├── src/
│   ├── app/
│   │   └── main.py
│   ├── create/
│   │   ├── alunos_create.py
|   |   ├── campeonatos_create.py
|   |   ├── maiores_campeoes_create.py
|   |   ├── numero_de_participantes_create.py
│   │   ├── materiais_create.py
│   │   ├── professores_create.py
|   |   └── insert/
|   |        ├── campeonatos_insert.py
|   |        ├── maiores_campeoes_insert.py
|   |        └── numero_de_participantes_insert.py
|   |   
│   ├── read/
│   │   ├── alunos_read.py
|   |   ├── campeonatos_read.py
|   |   ├── maiores_campeoes_read.py
|   |   ├── numero_de_participantes_read.py
│   │   ├── materiais_read.py
│   │   └── professores_read.py
│   ├── update/
│   │   ├── alunos_update.py
│   │   ├── materiais_update.py
│   │   └── professores_update.py
│   └── delete/
|       ├── alunos_delete.py
|       ├── materiais_delete.py
|       └── professores_delete.py
├── sqlite-database/
│   ├── epbjc.db
│   ├── epbjc_backup_1.db
│   ├── epbjc_backup_2.db
│   └── epbjc_backup_3.db
├── migracao/
│   ├── 
│   ├── 
│   ├── 
│   └── 
├── testes/
│   ├── 
│   ├── 
│   ├── 
│   └── 
├── README.md
├── campeonatos.db
├── maiores_campeoes.db
└── numero_participantes.db