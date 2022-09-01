import sqlite3
import pandas as pd
# Conexão com o sqlite
# Conectando com o objeto
conn = sqlite3.connect('test_analytics_engineer.db')

# cursor 
c = conn.cursor()

# Cria a tabela Country e grave os dados em uma tabela sqlite
c.execute("CREATE TABLE IF NOT EXISTS Country (id integer, name text)")
country = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\Country.csv')
country.to_sql('Country', conn, if_exists='replace', index = False)
conn.commit()


# Cria a tabela League e grave os dados em uma tabela sqlite
c.execute("CREATE TABLE IF NOT EXISTS League (id integer, country_id integer, name text)")
league = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\League.csv')
league.to_sql('League', conn, if_exists='replace', index = False)
conn.commit()


# Cria a tabela Match e grave os dados em uma tabela sqlite
c.execute("""
            CREATE TABLE IF NOT EXISTS Match
                (id integer,country_id integer, league_id integer, season text, stage text, date text, match_api_id integer,home_team_api_id integer,
                 away_team_api_id integer, home_team_goal integer, away_team_goal integer, home_player_X1 integer,home_player_X2 integer, 
                 home_player_X3 integer, home_player_X4 integer, home_player_X5 integer, home_player_X6 integer, home_player_X7 integer, 
                 home_player_X8 integer, home_player_X9 integer, home_player_X10 integer, home_player_X11 integer, away_player_X1 integer, 
                 away_player_X2 integer, away_player_X3 integer, away_player_X4 integer, away_player_X5 integer, away_player_X6 integer, 
                 away_player_X7 integer, away_player_X8 integer, away_player_X9 integer, away_player_X10 integer, away_player_X11 integer, 
                 home_player_Y1 integer, home_player_Y2 integer, home_player_Y3 integer, home_player_Y4 integer, home_player_Y5 integer,
                 home_player_Y6 integer, home_player_Y7 integer, home_player_Y8 integer, home_player_Y9 integer, home_player_Y10 integer, 
                 home_player_Y11 integer, away_player_Y1 integer, away_player_Y2 integer, away_player_Y3 integer, away_player_Y4 integer,
                 away_player_Y5 integer, away_player_Y6 integer, away_player_Y7 integer, away_player_Y8 integer, away_player_Y9 integer, 
                 away_player_Y10 integer, away_player_Y11 integer, home_player_1 integer, home_player_2 integer, home_player_3 integer, 
                 home_player_4 integer, home_player_5 integer, home_player_6 integer, home_player_7 integer, home_player_8 integer, 
                 home_player_9 integer, home_player_10 integer, home_player_11 integer, away_player_1 integer, away_player_2 integer, 
                 away_player_3 integer, away_player_4 integer, away_player_5 integer, away_player_6 integer, away_player_7 integer, 
                 away_player_8 integer, away_player_9 integer, away_player_10 integer, away_player_11 integer, goal text, shoton text, 
                 shotoff text, foulcommit text, card text, cross text, corner text, possession text, B365H real, B365D real, B365A real, 
                 BWH real, BWD real, BWA real, IWH real, IWD real, IWA real, LBH real, LBD real, LBA real, PSH real, PSD real, 
                 PSA real, WHH real, WHD real, WHA real, SJH real, SJD real, SJA real, VCH real, VCD real, VCA real, GBH real, 
                 GBD real, GBA real, BSH real, BSD real, BSA real)
        """)
match = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\Match.csv')
match.to_sql('Match', conn, if_exists='replace', index = False)
conn.commit()


# Cria a tabela Player e grave os dados em uma tabela sqlite
c.execute("CREATE TABLE IF NOT EXISTS Player (id integer, player_api_id integer, player_name text, player_fifa_api_id integer, birthday text, height real, weight integer)")
player = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\Player.csv')
player.to_sql('Player', conn, if_exists='replace', index = False)
conn.commit()


# Cria a tabela Player_Attributes e grave os dados em uma tabela sqlite
c.execute("CREATE TABLE IF NOT EXISTS Player_Attributes (id integer , Player_Attributes text)")
player_attributes = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\Player_Attributes.csv')
player_attributes.to_sql('Player_Attributes', conn, if_exists='replace', index = False)
conn.commit()

# Cria a tabela Team e grave os dados em uma tabela sqlite
c.execute("CREATE TABLE IF NOT EXISTS Team (id integer, team_api_id integer, team_fifa_api_id integer, team_long_name text,team_short_name text)")
team = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\Team.csv')
team.to_sql('Team', conn, if_exists='replace', index = False)
conn.commit()

# Cria a tabela Team_Attributes e grave os dados em uma tabela sqlite
c.execute("CREATE TABLE IF NOT EXISTS Team_Attributes (id integer , Team_Attributes text)")
team_attributes = pd.read_csv(r'D:\data-analytics-engineer-test-main\data-analytics-engineer-test-main\Data\Data\Data\Team_Attributes.csv')
team_attributes.to_sql('Team_Attributes', conn, if_exists='replace', index = False)
conn.commit()


# Fecha a conexão.
c.close()