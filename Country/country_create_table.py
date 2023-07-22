# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

#%%
class CountryTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'Country.csv'.

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Country'):
            print("A tabela 'Country' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        country = pd.read_csv('Data/Country.csv')
        country.dropna(inplace=True)
        country['id'] = country['id'].astype(str).str.rstrip('.0').astype(int)
        country.drop_duplicates(subset=['id'], keep='first', inplace=True)

        # Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('name', String)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        country_table = Table('Country', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = country.to_dict(orient='records')
        for data_row in data_list:
            x = country_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Country' criada no banco de dados. Inseridos '{len(country)}' registros")

# %%