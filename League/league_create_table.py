# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

#%%
class LeagueTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'League.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('League'):
            print("A tabela 'League' já existe no banco de dados.")

        league = pd.read_csv('Data/League.csv')

        # Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('country_id', Integer),
            Column('name', String)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        league_table = Table('League', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = league.to_dict(orient='records')
        for data_row in data_list:
            x = league_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'League' criada no banco de dados. Inseridos '{len(league)}' registros")
# %%