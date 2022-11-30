import sqlite3
import sys
import os

#python3 .\Python\create_tables.py

vSQLitePath = 'C:\\sqlite3\\db\\test_analytics_engineer.db'

print ('*** CREATE TABLES IN SQLITE DATABASE***');   
print ('------------------')

try:
    sqlCon = sqlite3.connect(vSQLitePath)
    cur = sqlCon.cursor()

    #drop das tabelas 
    cur.execute('DROP TABLE IF EXISTS Country;')
    cur.execute('DROP TABLE IF EXISTS League;')
    cur.execute('DROP TABLE IF EXISTS Match;')
    cur.execute('DROP TABLE IF EXISTS Player;')
    cur.execute('DROP TABLE IF EXISTS Player_Attributes;')
    cur.execute('DROP TABLE IF EXISTS Team;')
    cur.execute('DROP TABLE IF EXISTS Team_Attributes;')

    cur.execute('DROP TABLE IF EXISTS Match_Cards;')
    cur.execute('DROP TABLE IF EXISTS Match_Fouls;')    

    sqlCommand = ''

    #Cria tabela Country
    sqlCommand = """
                    CREATE TABLE Country ( id       INT
                                          ,name     VARCHAR2(50) 
                                         );
                """
    cur.execute(sqlCommand);
    
    #Cria tabela League
    sqlCommand = """
                    CREATE TABLE League ( id            INT
                                        , country_id    INT
                                        , name          VARCHAR2(50) 
                                        );
                """
    cur.execute(sqlCommand);
      
    #Cria tabela Player
    sqlCommand = """
                    CREATE TABLE Player (id                 INT
                                        ,player_api_id      INT
                                        ,player_name        VARCHAR2(100)
                                        ,player_fifa_api_id INT
                                        ,birthday           DATETIME
                                        ,height             FLOAT
                                        ,weight             FLOAT
                                        );
                """
    cur.execute(sqlCommand);
    
    #Cria tabela Player_Attributes
    sqlCommand = """
                    CREATE TABLE Player_Attributes ( id                 INT
                                                    ,Player_Attributes  BLOB
                                                    );
                """
    cur.execute(sqlCommand);
    
    #Cria tabela Team
    sqlCommand = """
                    CREATE TABLE Team ( id                  INT
                                       ,team_api_id         INT
                                       ,team_fifa_api_id    INT
                                       ,team_long_name      VARCHAR2(100)
                                       ,team_short_name     CHAR(3)
                                      );
                """
    cur.execute(sqlCommand);
    
    #Cria tabela Team_Attributes
    sqlCommand = """
                    CREATE TABLE Team_Attributes ( id                 INT
                                                  ,Team_Attributes    BLOB
                                                 );
    
                """
    cur.execute(sqlCommand); 

    #Cria tabela Match
    sqlCommand = """
                    CREATE TABLE Match (id						INT
                                        ,country_id             INT
                                        ,league_id              INT
                                        ,season					CHAR(9)
                                        ,stage					INT
                                        ,date					DATETIME
                                        ,match_api_id			INT
                                        ,home_team_api_id		INT
                                        ,away_team_api_id		INT
                                        ,home_team_goal			FLOAT
                                        ,away_team_goal			FLOAT
                                        ,home_player_X1			FLOAT
                                        ,home_player_X2         FLOAT
                                        ,home_player_X3         FLOAT
                                        ,home_player_X4         FLOAT
                                        ,home_player_X5         FLOAT
                                        ,home_player_X6         FLOAT
                                        ,home_player_X7         FLOAT
                                        ,home_player_X8         FLOAT
                                        ,home_player_X9         FLOAT
                                        ,home_player_X10        FLOAT
                                        ,home_player_X11        FLOAT
                                        ,away_player_X1         FLOAT
                                        ,away_player_X2         FLOAT
                                        ,away_player_X3         FLOAT
                                        ,away_player_X4         FLOAT
                                        ,away_player_X5         FLOAT
                                        ,away_player_X6         FLOAT
                                        ,away_player_X7         FLOAT
                                        ,away_player_X8         FLOAT
                                        ,away_player_X9         FLOAT
                                        ,away_player_X10        FLOAT
                                        ,away_player_X11        FLOAT
                                        ,home_player_Y1         FLOAT
                                        ,home_player_Y2         FLOAT
                                        ,home_player_Y3         FLOAT
                                        ,home_player_Y4         FLOAT
                                        ,home_player_Y5         FLOAT
                                        ,home_player_Y6         FLOAT
                                        ,home_player_Y7         FLOAT
                                        ,home_player_Y8         FLOAT
                                        ,home_player_Y9         FLOAT
                                        ,home_player_Y10        FLOAT
                                        ,home_player_Y11        FLOAT
                                        ,away_player_Y1         FLOAT
                                        ,away_player_Y2         FLOAT
                                        ,away_player_Y3         FLOAT
                                        ,away_player_Y4         FLOAT
                                        ,away_player_Y5         FLOAT
                                        ,away_player_Y6         FLOAT
                                        ,away_player_Y7         FLOAT
                                        ,away_player_Y8         FLOAT
                                        ,away_player_Y9         FLOAT
                                        ,away_player_Y10        FLOAT
                                        ,away_player_Y11        FLOAT
                                        ,home_player_1          FLOAT
                                        ,home_player_2          FLOAT
                                        ,home_player_3          FLOAT
                                        ,home_player_4          FLOAT
                                        ,home_player_5          FLOAT
                                        ,home_player_6          FLOAT
                                        ,home_player_7          FLOAT
                                        ,home_player_8          FLOAT
                                        ,home_player_9          FLOAT
                                        ,home_player_10         FLOAT
                                        ,home_player_11         FLOAT
                                        ,away_player_1          FLOAT
                                        ,away_player_2          FLOAT
                                        ,away_player_3          FLOAT
                                        ,away_player_4          FLOAT
                                        ,away_player_5          FLOAT
                                        ,away_player_6          FLOAT
                                        ,away_player_7          FLOAT
                                        ,away_player_8          FLOAT
                                        ,away_player_9          FLOAT
                                        ,away_player_10         FLOAT
                                        ,away_player_11			FLOAT
                                        ,goal					BLOB
                                        ,shoton                 BLOB
                                        ,shotoff                BLOB
                                        ,foulcommit             BLOB
                                        ,card                   BLOB
                                        ,cross                  BLOB
                                        ,corner                 BLOB
                                        ,possession             BLOB
                                        ,B365H					FLOAT
                                        ,B365D                  FLOAT
                                        ,B365A                  FLOAT
                                        ,BWH                    FLOAT
                                        ,BWD                    FLOAT
                                        ,BWA                    FLOAT
                                        ,IWH                    FLOAT
                                        ,IWD                    FLOAT
                                        ,IWA                    FLOAT
                                        ,LBH                    FLOAT
                                        ,LBD                    FLOAT
                                        ,LBA                    FLOAT
                                        ,PSH                    FLOAT
                                        ,PSD                    FLOAT
                                        ,PSA                    FLOAT
                                        ,WHH                    FLOAT
                                        ,WHD                    FLOAT
                                        ,WHA                    FLOAT
                                        ,SJH                    FLOAT
                                        ,SJD                    FLOAT
                                        ,SJA                    FLOAT
                                        ,VCH                    FLOAT
                                        ,VCD                    FLOAT
                                        ,VCA                    FLOAT
                                        ,GBH                    FLOAT
                                        ,GBD                    FLOAT
                                        ,GBA                    FLOAT
                                        ,BSH                    FLOAT
                                        ,BSD                    FLOAT
                                        ,BSA                    FLOAT
                    );
                """
    cur.execute(sqlCommand);

    #Cria tabela Match_Cards
    sqlCommand = """
                    CREATE TABLE Match_Cards (
                                             id						    INTEGER PRIMARY KEY AUTOINCREMENT
                                            , match_id					INT
                                            , team_api_id				INT
                                            , player_api_id				INT	
                                            , card_type					CHAR(1)
                                            );
    
                """
    cur.execute(sqlCommand); 

    #Cria tabela Match_Fouls
    sqlCommand = """
                    CREATE TABLE Match_Fouls (
                                         id						    INTEGER PRIMARY KEY AUTOINCREMENT
                                        , match_id					INT
                                        , team_api_id				INT    
                                        , player_api_id				INT	
                                        , type						VARCHAR(30)
                        );
    
                """
    cur.execute(sqlCommand);     
    cur.close()

except sqlite3.Error as error:
    print('Error:', error)

finally:
    if sqlCon:
        sqlCon.close()
        print('SQL connection has been closed')
        print('*-----------------------------')