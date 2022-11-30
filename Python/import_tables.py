import csv
import sqlite3
import sys
import os

#Para importar apenas a tabela uma tabela, informar o nome nos parâmetros. Ex: Player
#python3 .\Python\import_tables.py Player  

#Para importar todos os CSVs do diretorio
#python3 .\Python\import_tables.py

vCSVPath = '..\\Data\\'
vSQLitePath = 'C:\\sqlite3\\db\\test_analytics_engineer.db'
pTable = ''

#Obtem o parâmetro informado
if len(sys.argv) > 1:
    pTable = sys.argv[1]

    
print ('=============================')
print ('*** IMPORT CSV INTO SQLITE DATABASE***')
print ('=============================')
print('')
print ('Path: ', vCSVPath);
print ('CSV name: ', pTable);
print ('------------------')

#Lista os arquivos do diretório
for vFileName in os.listdir(vCSVPath):

    if os.path.isfile(vCSVPath + vFileName):
        vTableName = os.path.splitext(vFileName)[0]          # obtem o nome sem extensão
        vExt      = os.path.splitext(vFileName)[1].upper()   # obtem a extensão do arquivo

        # se não for arquivo CSV ou 
        # se o nome do arquivo atual não for referente à tabela passada nos parametros, pula para proximo arquivo
        if  (vExt != '.CSV') or (pTable != '' and (pTable != vTableName)):
            continue

        print('Importing', vFileName)
        with open(vCSVPath + vFileName, 'r', encoding='utf-8') as csvInput:
            #carrega os dados do arquivo em um Dict
            myDict = csv.DictReader(csvInput)

            #obtem o nome as colunas e joga numa lista
            csvColsList = myDict.fieldnames

            #cria uma lista para alimentar com os dados serem inseridos
            insertDataList = []

            #Varre o dict e, usando a lista das colunas, e cria uma tupla com os valores de cada linha do csv
            for i in myDict:
                myTuple = ()
                for col in csvColsList:
                    myTuple = myTuple + (i[col],)

                #Apos varrer todas as colunas, insere a tupla na lista de dados
                #(1, 'Belgium')
                insertDataList.append(myTuple) 

            #Ao final, a Lista terá toos os dados do CSV para inserção em massa no banco de dados     
            #Ex: [(1, 'Belgium'), (1729, 'England')]
                
            #Comandos do Banco de dados
            try:
                #Conecta ao SQLite e abre o cursor
                sqlCon = sqlite3.connect(vSQLitePath)
                cur = sqlCon.cursor()

                #Cria um string com o nome dos campos separados por virgula para o insert em massa
                #Ex: id, name
                colStr = ','.join(csvColsList)
                
                #Identifiquei 2 CSV sem o nome da primeira coluna e inclui este tratamento
                if colStr[:1] == ',':
                    colStr = 'id' + colStr

                #Cria uma string de '?' separados por virgula para o insert em massa
                #Ex. Se são 2 colunas, fica: ?, ?
                paramStr = ','.join('?' for x in csvColsList)
        
                #Limpa a tabela
                cur.execute('DELETE FROM ' + vTableName + ';')

                #Cria o comando SQL para INSERT
                #Ex: INSERT INTO Country(id, name) VALUES (?,?);
                sqlCommand = 'INSERT INTO ' + vTableName + ' (' + colStr + ') VALUES (' + paramStr +');'
                #print(sqlCommand)

                #Faz inserção em massa, passando lista de dados alimentada anteriormente
                cur.executemany(sqlCommand, insertDataList)
                sqlCon.commit()
                cur.close()

            except sqlite3.Error as error:
                print('Error:', error)

            finally:
                if sqlCon:
                    sqlCon.close()
                    print('SQL connection has been closed')
                    print('-----------------------------')

print ('') 
print ('=============================')
print ('FINISHED')
print ('=============================')
print ('') 