# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

#%%
class PlayerAttributesTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'Player_Attributes.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Player_Attributes'):
            print("A tabela 'Player_Attributes' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        player_attributes = pd.read_csv('Data/Player_Attributes.csv')
        player_attributes.rename(columns={'Unnamed: 0	': 'id'}, inplace=True)
        # player_attributes['Player_Attributes'] = player_attributes['Player_Attributes'].apply(json.loads)
        # player_attributes = pd.json_normalize(player_attributes['Player_Attributes'])# type:ignore
        # player_attributes['id'] = player_attributes['id'].astype(int)
        # player_attributes['player_fifa_api_id'] = player_attributes['player_fifa_api_id'].astype(int)
        # player_attributes['player_api_id'] = player_attributes['player_api_id'].astype(int)
        # player_attributes['date'] = pd.to_datetime(player_attributes['date'])

        # Criar a tabela no banco de dados
        columns = [
            Column('Unnamed: 0', Integer, primary_key=True),
            Column('Player_Attributes', String)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        player_attributes_table = Table('Player_Attributes', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = player_attributes.to_dict(orient='records')
        for data_row in data_list:
            x = player_attributes_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Player_Attributes' criada no banco de dados. Inseridos '{len(player_attributes)}' registros")

# %%