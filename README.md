Estrutura recomendada para o projeto final do módulo 15:

Este projeto foi desenvolvido para gerenciar informações sobre jogos, incluindo a criação e manipulação de dados em um banco SQLite. O sistema é organizado para permitir a criação, inserção e consulta de dados relacionados a jogos e seus atributos, além de suportar operações em outras áreas, como materiais, alunos e professores.

jogos_create.py: importa a biblioteca sqlite3, cria a base de dados jogos.db e se conecta a ela, além de também criar a tabela campeonatos (tabela mãe) com os campos de id ( INTEGER, que usa autoincrement, ou seja, o programa dá o valor para o id), o nome do jogo (TEXT) e o genero do mesmo (TEXT) usando INTEGER e TEXT como tipos de variáveis.

jogos_insert.py: importa a biblioteca sqlite3, se conecta a base de dados jogos.db e insere dados na tabela. 

jogos_select.py: importa a biblioteca sqlite3, se conecta a base e lê cada linha da tabela jogos.

epbjc/
├── src/
│   ├── app/
│   │   └── main.py
│   ├── create/
│   │   ├── jogos_create.py
│   │   └── insert/
│   │        └── jogos_insert.py
│   ├── read/
│   │   └── jogos_select.py
│   ├── update/
│   │   ├── alunos_update.py
│   │   ├── materiais_update.py
│   │   └── professores_update.py
├── sqlite-database/
│   ├── jogos.db
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
|── README.md
