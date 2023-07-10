#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlite3

# Estabeleça uma conexão com o banco de dados
conn = sqlite3.connect('/Users/matheussilva/Banco_SQLITE/BANCO_SQLITE')

# Executando a consulta SQL 1
query_1 = '''
WITH dados_consolidados AS (
    SELECT SUM(home_team_goal) AS QTD_HOME_TEAM_GOAL,
           SUM(away_team_goal) AS QTD_AWAY_TEAM_GOAL,
           SUM(goal) AS QTD_GOAL,
           home_team_goal + away_team_goal AS QTD_HOME_AWAY,
           A.league_id AS league_id,
           A.country_id AS country_id,
           A.season as SEASON,
           A.date AS DATA
    FROM test_analytics_engineer_Match A
    GROUP BY A.league_id, A.country_id, A.season, A.date
)

-- Visão por Liga

SELECT sum(QTD_HOME_TEAM_GOAL) AS QTD_HOME_TEAM_GOAL
,sum(QTD_AWAY_TEAM_GOAL) AS QTD_AWAY_TEAM_GOAL
,sum(QTD_GOAL) AS QTD_GOAL
,AVG(QTD_HOME_AWAY) AS AVG_HOME_AWAY
,B.name 
FROM dados_consolidados A
LEFT JOIN test_analytics_engineer_League B ON B.id = A.league_id
GROUP BY B.name 
ORDER BY B.name  ASC

'''

# Executando a consulta SQL 2
query_2 = '''
WITH dados_consolidados AS (
    SELECT SUM(home_team_goal) AS QTD_HOME_TEAM_GOAL,
           SUM(away_team_goal) AS QTD_AWAY_TEAM_GOAL,
           SUM(goal) AS QTD_GOAL,
           home_team_goal + away_team_goal AS QTD_HOME_AWAY,
           A.league_id AS league_id,
           A.country_id AS country_id,
           A.season as SEASON,
           A.date AS DATA
    FROM test_analytics_engineer_Match A
    GROUP BY A.league_id, A.country_id, A.season, A.date
)

-- Visão por país

SELECT sum(QTD_HOME_TEAM_GOAL) AS QTD_HOME_TEAM_GOAL
,sum(QTD_AWAY_TEAM_GOAL) AS QTD_AWAY_TEAM_GOAL
,sum(QTD_GOAL) AS QTD_GOAL
,AVG(QTD_HOME_AWAY) AS AVG_HOME_AWAY
,C.name 
FROM dados_consolidados A
LEFT JOIN (SELECT DISTINCT id, 
CASE WHEN name = 'Bélgica' THEN 'Belgium'
	 WHEN name = 'Inglaterra' THEN 'England'
	 WHEN name = 'França' THEN 'France'
	 WHEN name = 'Alemanha' THEN 'Germany'
	 WHEN name = 'Itália' THEN 'Italy'
ELSE name END AS name
FROM test_analytics_engineer_Country) C ON C.id = A.country_id 
GROUP BY C.name 
ORDER BY C.name  ASC


'''

# Executando a consulta SQL 3
query_3 = '''
WITH dados_consolidados AS (
    SELECT SUM(home_team_goal) AS QTD_HOME_TEAM_GOAL,
           SUM(away_team_goal) AS QTD_AWAY_TEAM_GOAL,
           SUM(goal) AS QTD_GOAL,
           home_team_goal + away_team_goal AS QTD_HOME_AWAY,
           A.league_id AS league_id,
           A.country_id AS country_id,
           A.season as SEASON,
           A.date AS DATA
    FROM test_analytics_engineer_Match A
    GROUP BY A.league_id, A.country_id, A.season, A.date
)

-- Visão por temporada

SELECT sum(QTD_HOME_TEAM_GOAL) AS QTD_HOME_TEAM_GOAL
,sum(QTD_AWAY_TEAM_GOAL) AS QTD_AWAY_TEAM_GOAL
,sum(QTD_GOAL) AS QTD_GOAL
,AVG(QTD_HOME_AWAY) AS AVG_HOME_AWAY
,SEASON
FROM dados_consolidados A
GROUP BY SEASON
ORDER BY SEASON  ASC

'''

# Executando a consulta SQL 4
query_4 = '''
WITH dados_consolidados AS (
    SELECT SUM(home_team_goal) AS QTD_HOME_TEAM_GOAL,
           SUM(away_team_goal) AS QTD_AWAY_TEAM_GOAL,
           SUM(goal) AS QTD_GOAL,
           home_team_goal + away_team_goal AS QTD_HOME_AWAY,
           A.league_id AS league_id,
           A.country_id AS country_id,
           A.season as SEASON,
           A.date AS DATA
    FROM test_analytics_engineer_Match A
    GROUP BY A.league_id, A.country_id, A.season, A.date
)

-- Visão por ano e mês

SELECT sum(QTD_HOME_TEAM_GOAL) AS QTD_HOME_TEAM_GOAL
,sum(QTD_AWAY_TEAM_GOAL) AS QTD_AWAY_TEAM_GOAL
,sum(QTD_GOAL) AS QTD_GOAL
,AVG(QTD_HOME_AWAY) AS AVG_HOME_AWAY
,strftime('%Y-%m', a.DATA) AS ANO_MES
FROM dados_consolidados A
GROUP BY strftime('%Y-%m', a.DATA)
ORDER BY strftime('%Y-%m', a.DATA)  ASC


'''


# Executando a consulta SQL 5
query_5 = '''
WITH dados_consolidados AS (
    SELECT SUM(home_team_goal) AS QTD_HOME_TEAM_GOAL,
           SUM(away_team_goal) AS QTD_AWAY_TEAM_GOAL,
           SUM(goal) AS QTD_GOAL,
           home_team_goal + away_team_goal AS QTD_HOME_AWAY,
           A.league_id AS league_id,
           A.country_id AS country_id,
           A.season as SEASON,
           A.date AS DATA
    FROM test_analytics_engineer_Match A
    GROUP BY A.league_id, A.country_id, A.season, A.date
)

-- Visão consolidada unificada

SELECT sum(QTD_HOME_TEAM_GOAL) AS QTD_HOME_TEAM_GOAL
,sum(QTD_AWAY_TEAM_GOAL) AS QTD_AWAY_TEAM_GOAL
,sum(QTD_GOAL) AS QTD_GOAL
,AVG(QTD_HOME_AWAY) AS AVG_HOME_AWAY
,B.name 
,C.name 
,SEASON
,strftime('%Y-%m', a.DATA) AS ANO_MES

FROM dados_consolidados A
LEFT JOIN test_analytics_engineer_League B ON B.id = A.league_id
LEFT JOIN (SELECT DISTINCT id, 
CASE WHEN name = 'Bélgica' THEN 'Belgium'
	 WHEN name = 'Inglaterra' THEN 'England'
	 WHEN name = 'França' THEN 'France'
	 WHEN name = 'Alemanha' THEN 'Germany'
	 WHEN name = 'Itália' THEN 'Italy'
ELSE name END AS name
FROM test_analytics_engineer_Country) C ON C.id = A.country_id 
GROUP BY B.name 
,C.name 
,SEASON
,strftime('%Y-%m', a.DATA)
ORDER BY B.name  ASC

'''

df_1 = pd.read_sql_query(query_1, conn)
df_2 = pd.read_sql_query(query_2, conn)
df_3 = pd.read_sql_query(query_3, conn)
df_4 = pd.read_sql_query(query_4, conn)
df_5 = pd.read_sql_query(query_5, conn)


# Salve o resultado eM arquivos arquivos .CSV
df_1.to_csv('/Users/matheussilva/Base_league.csv', index=False)
df_2.to_csv('/Users/matheussilva/Base_Country.csv', index=False)
df_3.to_csv('/Users/matheussilva/Base_Season.csv', index=False)
df_4.to_csv('/Users/matheussilva/Base_YearMonth.csv', index=False)
df_5.to_csv('/Users/matheussilva/Base_Unified.csv', index=False)


# Fechando a conexão com o banco de dados
conn.close()

