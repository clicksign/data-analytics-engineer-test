# Solução do desafio

## Questão 1

O arquivo `questao1.py` cria a database e monta as tabelas necessárias no `schema` test_analytics_engineer.

## Questão 2

O arquivo `questao2-setup.py` é utilizado para montar as queries de criação de novas colunas a partir da extração de uma coluna JSON. Já o arquivo `questao2-exec.sql` possui os comandos necessários para criação das tabelas `Player_Attributes_Modified`, `Team_Attributes_Modified` (essas duas queries vem do resultado do setup com Python) e `Match_Modified`.

## Questão 3

O arquivo `questao3.ipynb` é um Jupyter Notebook com algumas explorações das tabelas e variáveis. As tabelas `League`, `Country` e `Team` não tinham muito o que ser avaliado, por isso não foram exploradas.

## Questão 4

No arquivo `questao4.sql`, a tabela `Relations` foi montada a partir de chaves entre League, ``Country``, ``Match``, ``Team_Attributes_Modified`` e ``Player``. A tabela ``Match`` precisou ser incluída pra utilizar as chaves `home_team_api_id` e `home_player_1` (dentre as várias possíveis dentro dessa tabela) para relacionar com as tabelas ``Team_Attributes_Modified`` (`team_api_id`) e ``Player`` (`player_api_id`), respectivamente.

## Questão 5

Para automatizar a geração de um relatório que esteja sempre com os dados atualizados, desde que as tabelas estejam atualizadas, foi criada uma view no arquivo `questao5.sql` com algumas métricas.