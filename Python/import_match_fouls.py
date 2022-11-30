import sqlite3
from xml.etree import ElementTree as elements

#python3 .\Python\import_match_fouls.py



vSQLitePath = 'C:\\sqlite3\\db\\test_analytics_engineer.db'
vMatchId = 0

try:
    insertDataList = []
    
    #Conecta ao SQLite e abre o cursor
    sqlCon = sqlite3.connect(vSQLitePath)
    cur = sqlCon.cursor()
    
    #Le a tabela Match que possuem informação de cartão
    sqlCommandRead = 'SELECT id, foulcommit FROM Match WHERE foulcommit <> "" ;'
    cur.execute(sqlCommandRead)
    output = cur.fetchall()

    #Para cada linha da tabela
    for row in output:
        vMatchId = row[0]
        #print(vMatchId)
        myTuple = ()

        #Carrega os dados XML da coluna foulCommit
        root = elements.fromstring(row[1])
        levels = root.findall('.//value')

        #Para cada tag "value"
        for level in levels:

          #Verifica se possui informacao completa necessaria (jogador, time e tipo)
          if level.find('player1') != None and level.find('team') != None and level.find('type') != None :

            #Insere os valores na tupla
            myTuple =  (vMatchId, level.find('team').text,  level.find('player1').text,  level.find('type').text)
            
            #Adiciona o valor a lista
            insertDataList.append(myTuple)


    #No final, faz o insert em massa
    sqlCommandInsert = 'INSERT INTO Match_Fouls ( match_id, team_api_id, player_api_id, type) VALUES (?,?,?,?);'
    cur.executemany(sqlCommandInsert, insertDataList)
    sqlCon.commit()
    cur.close()

except sqlite3.Error as error:
    print('Error:', error)

finally:
    if sqlCon:
        sqlCon.close()
        print('SQL connection has been closed')
        print('*-----------------------------')
