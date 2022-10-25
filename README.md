# **Introdução:**
Olá pessoal, tudo bem? Aqui vou fazer alguns comentários pertinentes às resoluções e dificuldades obtidas durante o processo de realização do teste.

# **Informações dos dados:**

Os dados que você precisará para completar este desafio está armazenado na pasta **data** deste repositório. Assim como na realização do teste, será necessário fazer a extração do arquivo comprimido "Data.rar". O código utilizado para a resolução do teste está presente no notebook 'Analytic Engineer Test'

# **Questão 1 - Utilize Python**

Como primeiro passo do desafio, faça a leitura/importação desses arquivos via python e realize o upload/carregamento desses dados em um banco SQLite.

Crie um schema chamado: test_analytics_engineer
Crie as tabelas com os mesmos nomes dos arquivos .csv
Respeite a tipagem e os nomes das colunas dos arquivos .csv

## **Considerações:**

Foi uma questão tranquila de ser executada, para ela utilizei somente a biblioteca sqlite3 no python para a criação do banco e da conexão com ele.

Questão 2 - Utilize SQL

Estabeleça uma relação entre as tabelas Player e Player_Attributes em uma nova tabela, chamada ‘Player_Attributes_Modified’, onde cada key do json é uma nova coluna. Faça o mesmo para a relação Team e Team_Attributes, como o nome para a tabela ‘Team_Attributes_Modified’

Crie uma tabela chamada Match_Modified cuja coluna seja representada como JSON, onde as chaves precisam ser referentes às colunas da tabela Match, sendo elas : id,match_api_id, home_team_api_id, away_team_api_id .

## **Considerações:**

Foi uma questão que tive um pouco de dificuldade no começo por nunca ter utilizado funções de extração de JSON dentro do SQL, como pedia a questão, então foi necessário consultar e pesquisar pela documentação do SQLite para usar a função 'json_extract'. Ainda assim, quando usava a função ela retornava um erro de 'malformed JSON' e após investigar, percebia que devido ao fato de algumas linhas do JSON serem 'NaN' então utilizei a função 'json_extract' junto com a 'replace' e a partir daí não houve mais nenhum problema na execução do código para realizar o join entre as tabelas.

Questão 3 - Utilize SQL ou Python

Faça uma análise exploratória dos dados no sentido de validar a qualidade dos dados destes datasets. Use sua criatividade e imaginação para buscar “sujeiras” na base de dados.

Lembre-se que queremos gerar insights com dados, então realize relações com tabelas que nos forneçam alguma informação relevante para os dados tratados analisados. Crie análises exploratórias dos dados.

## **Considerações:**
Essa questão foi bem legal de ser feita, queria ter entregado ainda mais, mas não tinha certeza do que significava cada atributo dos datasets ('Match.csv') não aprofundei a análise, como exemplo eu não sabia em qual parte das tags HTML deveria ser feita a extração das colunas **'goal','shoton','shotoff','foulcommit','card', 'cross', 'corner', 'possession'**

Questão 4 - Utilize SQL

Encontre uma relação de dados entre as tabelas League, Country, Team_Attributes e Player, crie uma nova tabela chamada 'Relations'

## **Considerações:**

Para essa questão fiz um join direto entre as tabelas Team, League, Country com a Match e para fazer a relação de cada Player, eu precisava criar uma tabela virtual para cada jogador. Na questão fiz para 3 e expliquei em comentários que se necessário para os 22 jogadores (time da casa e time de fora) era só seguir o padrão.

Questão 5 - Utiize SQL-CTE

Semanalmente o gerente da Fifa solicita a média de gols dos times mandantes, porém como você gosta de entregar mais do que lhe pedem, você resolveu montar uma CTE para entregar outras métricas para seu gerente. Como você faria, em SQL, para salvar ou automatizar essa query? Envie-nos seu código.


