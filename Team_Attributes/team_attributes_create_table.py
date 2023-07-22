# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

#%%
class TeamAttributesTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'Team_Attributes.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Team_Attributes'):
            print("A tabela 'Team_Attributes' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        team_attributes = pd.read_csv('Data/Team_Attributes.csv')
        team_attributes.rename(columns={'Unnamed: 0	': 'id'}, inplace=True)
        # team_attributes['Team_Attributes'] = team_attributes['Team_Attributes'].apply(json.loads)
        # team_attributes = pd.json_normalize(team_attributes['Team_Attributes'])# type:ignore
        # team_attributes['id'] = team_attributes['id'].astype(int)
        # team_attributes['team_fifa_api_id'] = team_attributes['team_fifa_api_id'].astype(int)
        # team_attributes['team_api_id'] = team_attributes['team_api_id'].astype(int)
        # team_attributes['date'] = pd.to_datetime(team_attributes['date'])
        # team_attributes['buildUpPlaySpeed'] = team_attributes['buildUpPlaySpeed'].astype(int)
        # team_attributes['buildUpPlayPassing'] = team_attributes['buildUpPlayPassing'].astype(int)
        # team_attributes['chanceCreationPassing'] = team_attributes['chanceCreationPassing'].astype(int)
        # team_attributes['chanceCreationCrossing'] = team_attributes['chanceCreationCrossing'].astype(int)
        # team_attributes['chanceCreationShooting'] = team_attributes['chanceCreationShooting'].astype(int)
        # team_attributes['defencePressure'] = team_attributes['defencePressure'].astype(int)
        # team_attributes['defenceAggression'] = team_attributes['defenceAggression'].astype(int)
        # team_attributes['defenceTeamWidth'] = team_attributes['defenceTeamWidth'].astype(int)
        # team_attributes.drop_duplicates(subset=['id'], keep='first', inplace=True)

        # Criar a tabela no banco de dados
        columns = [
            Column('Unnamed: 0', Integer, primary_key=True),
            Column('Team_Attributes', String)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        team_attributes_table = Table('Team_Attributes', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = team_attributes.to_dict(orient='records')
        for data_row in data_list:
            x = team_attributes_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Team_Attributes' criada no banco de dados. Inseridos '{len(team_attributes)}' registros")

# %%