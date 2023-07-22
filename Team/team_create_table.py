# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

#%%
class TeamTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'Team.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Team'):
            print("A tabela 'Team' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        team = pd.read_csv('Data/Team.csv')
        team.dropna(inplace=True)
        team['team_fifa_api_id'] = team['team_fifa_api_id'].astype(str).str.rstrip('.0').astype(int)

        # Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('team_api_id', Integer),
            Column('team_fifa_api_id', Integer),
            Column('team_long_name', String),
            Column('team_short_name', String)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        team_table = Table('Team', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = team.to_dict(orient='records')
        for data_row in data_list:
            x = team_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Team' criada no banco de dados. Inseridos '{len(team)}' registros")

# %%