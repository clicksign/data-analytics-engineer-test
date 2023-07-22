# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, Date, Float, MetaData
from sqlalchemy.orm import Session

#%%
class PlayerTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'Player.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Player'):
            print("A tabela 'Player' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        player = pd.read_csv('Data/Player.csv')
        player['birthday'] = pd.to_datetime(player['birthday'])

        ## Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('player_api_id', Integer),
            Column('player_name', String),
            Column('player_fifa_api_id', Integer),
            Column('birthday', Date),
            Column('height', Float),
            Column('weight', Integer)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        player_table = Table('Player', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = player.to_dict(orient='records')
        for data_row in data_list:
            x = player_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Player' criada no banco de dados. Inseridos '{len(player)}' registros")

# %%