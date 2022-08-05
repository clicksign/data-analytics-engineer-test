De posse do link, entenda o repositório e se atente ao contexto em que está envolvido. No repositório você encontrará dentro do diretório data, em um arquivo compactados data.rar os arquivos .csv disponiblizados como sample de dados, esses são os únicos e exclusivos dados para a realização desse teste. Boa sorte!

**Questão 1 - Utilize Python**

Como primeiro passo do desafio, faça a leitura/importação desses arquivos via python e realize o upload/carregamento desses dados em um banco **SQLite**.

- Crie um schema chamado: **test_analytics_engineer**
- Crie as tabelas com os mesmos nomes dos arquivos .csv
- Respeite a tipagem e os nomes das colunas dos arquivos .csv

**Questão 2 - Utilize SQL**

Estabeleça uma relação entre as tabelas **Player** e  **Player_Attributes** em uma nova tabela, chamada **‘Player_Attributes_Modified’**, onde cada key do json é uma nova coluna. Faça o mesmo para a relação **Team** e **Team_Attributes**, como o nome para a tabela **‘Team_Attributes_Modified’**

Crie uma tabela chamada **Match_Modified** cuja coluna seja representada como JSON, onde as chaves precisam ser referentes às colunas da tabela Match, sendo elas : **id,match_api_id, home_team_api_id, away_team_api_id .**

**Questão 3 - Utilize SQL ou Python**

Faça uma análise exploratória dos dados no sentido de validar a qualidade dos dados destes datasets. Use sua criatividade e imaginação para buscar “sujeiras” na base de dados.

Lembre-se que queremos gerar insights com dados, então realize relações com tabelas que nos forneçam alguma informação relevante para os dados tratados analisados. Crie análises exploratórias dos dados.

**Exemplos:** 

- Qual a proporção entre jogadores destros e canhotos? Quais os seus nomes?
- Qual o nome do país com maior saldo de gols.

**Questão 4 - Utilize SQL**

Encontre uma relação de dados entre as tabelas League, Country, Team_Attributes e Player, crie uma nova tabela chamada **'Relations'**

**Exemplo:**

Esquematize uma relação entre a **altura** e **peso** dos jogadores de forma isolada, com seu rendimento. 

***Dica***: Criar 3 intervalos entre os 6 valores com maiores contagens para estes dois parâmetros.

**Questão 5 - Utiize SQL-CTE**


Semanalmente o gerente da Fifa solicita a média de gols dos times mandantes, porém como você gosta de entregar mais do que lhe pedem, você resolveu montar uma CTE para entregar outras métricas para seu gerente. Como você faria, em SQL, para salvar ou automatizar essa query? Envie-nos seu código.


**Bônus**: realize a criação de um projeto no DBT e faça análises exploratórias mais aprofundadas.
