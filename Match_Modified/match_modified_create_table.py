# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session
from Infra.database_utils import sql
import json

# %%
class MatchModifiedTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir da query.

        SELECT id,
            match_api_id,
            home_team_api_id,
            away_team_api_id
        FROM Match

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Match_Modified'):
            print("A tabela 'Match_Modified' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        query = '''
                    SELECT 
                        CAST(id AS VARCHAR) AS id,
                        CAST(match_api_id AS VARCHAR) AS match_api_id,
                        CAST(home_team_api_id AS VARCHAR) AS home_team_api_id,
                        CAST(away_team_api_id AS VARCHAR) AS away_team_api_id
                    FROM Match
                '''
        df_match_modified = sql(query, self.engine)

        df_match_modified['Match_Modified'] = df_match_modified.apply(lambda row: {
            'id': row['id'],
            'match_api_id': row['match_api_id'],
            'home_team_api_id': row['home_team_api_id'],
            'away_team_api_id': row['away_team_api_id']
        }, axis=1)

        match_modified = pd.DataFrame(df_match_modified['Match_Modified'])
        match_modified['id'] = match_modified.index.astype(str)
        match_modified = match_modified[['id', 'Match_Modified']]
        match_modified['Match_Modified'] = match_modified['Match_Modified'].apply(json.dumps)

        # Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('Match_Modified', String)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        match_modified_table = Table('Match_Modified', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = match_modified.to_dict(orient='records')
        for data_row in data_list:
            x = match_modified_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Match_Modified' criada no banco de dados. Inseridos '{len(match_modified)}' registros")

# %%