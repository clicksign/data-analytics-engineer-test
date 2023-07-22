# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, Date, MetaData, Float
from sqlalchemy.orm import Session

#%%
class MatchTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'Match.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Match'):
            print("A tabela 'Match' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        match = pd.read_csv('Data/Match.csv')
        match['date'] = pd.to_datetime(match['date'])

        # Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('country_id', Integer),
            Column('league_id', Integer),
            Column('season', String),
            Column('stage', Integer),
            Column('date', Date),
            Column('match_api_id', Integer),
            Column('home_team_api_id', Integer),
            Column('away_team_api_id', Integer),
            Column('home_team_goal', Integer),
            Column('away_team_goal', Integer),
            Column('home_player_X1', Float),
            Column('home_player_X2', Float),
            Column('home_player_X3', Float),
            Column('home_player_X4', Float),
            Column('home_player_X5', Float),
            Column('home_player_X6', Float),
            Column('home_player_X7', Float),
            Column('home_player_X8', Float),
            Column('home_player_X9', Float),
            Column('home_player_X10', Float),
            Column('home_player_X11', Float),
            Column('away_player_X1', Float),
            Column('away_player_X2', Float),
            Column('away_player_X3', Float),
            Column('away_player_X4', Float),
            Column('away_player_X5', Float),
            Column('away_player_X6', Float),
            Column('away_player_X7', Float),
            Column('away_player_X8', Float),
            Column('away_player_X9', Float),
            Column('away_player_X10', Float),
            Column('away_player_X11', Float),
            Column('home_player_Y1', Float),
            Column('home_player_Y2', Float),
            Column('home_player_Y3', Float),
            Column('home_player_Y4', Float),
            Column('home_player_Y5', Float),
            Column('home_player_Y6', Float),
            Column('home_player_Y7', Float),
            Column('home_player_Y8', Float),
            Column('home_player_Y9', Float),
            Column('home_player_Y10', Float),
            Column('home_player_Y11', Float),
            Column('away_player_Y1', Float),
            Column('away_player_Y2', Float),
            Column('away_player_Y3', Float),
            Column('away_player_Y4', Float),
            Column('away_player_Y5', Float),
            Column('away_player_Y6', Float),
            Column('away_player_Y7', Float),
            Column('away_player_Y8', Float),
            Column('away_player_Y9', Float),
            Column('away_player_Y10', Float),
            Column('away_player_Y11', Float),
            Column('home_player_1', Float),
            Column('home_player_2', Float),
            Column('home_player_3', Float),
            Column('home_player_4', Float),
            Column('home_player_5', Float),
            Column('home_player_6', Float),
            Column('home_player_7', Float),
            Column('home_player_8', Float),
            Column('home_player_9', Float),
            Column('home_player_10', Float),
            Column('home_player_11', Float),
            Column('away_player_1', Float),
            Column('away_player_2', Float),
            Column('away_player_3', Float),
            Column('away_player_4', Float),
            Column('away_player_5', Float),
            Column('away_player_6', Float),
            Column('away_player_7', Float),
            Column('away_player_8', Float),
            Column('away_player_9', Float),
            Column('away_player_10', Float),
            Column('away_player_11', Float),
            Column('goal', String),
            Column('shoton', String),
            Column('shotoff', String),
            Column('foulcommit', String),
            Column('card', String),
            Column('cross', String),
            Column('corner', String),
            Column('possession', String),
            Column('B365H', Float),
            Column('B365D', Float),
            Column('B365A', Float),
            Column('BWH', Float),
            Column('BWD', Float),
            Column('BWA', Float),
            Column('IWH', Float),
            Column('IWD', Float),
            Column('IWA', Float),
            Column('LBH', Float),
            Column('LBD', Float),
            Column('LBA', Float),
            Column('PSH', Float),
            Column('PSD', Float),
            Column('PSA', Float),
            Column('WHH', Float),
            Column('WHD', Float),
            Column('WHA', Float),
            Column('SJH', Float),
            Column('SJD', Float),
            Column('SJA', Float),
            Column('VCH', Float),
            Column('VCD', Float),
            Column('VCA', Float),
            Column('GBH', Float),
            Column('GBD', Float),
            Column('GBA', Float),
            Column('BSH', Float),
            Column('BSD', Float),
            Column('BSA', Float)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        match_table = Table('Match', metadata, *columns)
        
       # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = match.to_dict(orient='records')
        for data_row in data_list:
            x = match_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Match' criada no banco de dados. Inseridos '{len(match)}' registros")

# %%