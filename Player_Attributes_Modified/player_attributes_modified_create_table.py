# %%
import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, Date, Float, MetaData
from sqlalchemy.orm import Session
from Infra.database_utils import sql

# %%
class PlayerAttributesModifiedTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir da query.

        WITH CTE_Player_Attributes AS (
            SELECT
                CAST(JSON_extract(player_attributes, '$.id') AS INT) as id,
                CAST(JSON_extract(player_attributes, '$.player_fifa_api_id') AS INT) as player_fifa_api_id,
                CAST(JSON_extract(player_attributes, '$.player_api_id') AS INT) as player_api_id,
                JSON_extract(player_attributes, '$.date') as date,
                CAST(JSON_extract(player_attributes, '$.overall_rating') AS FLOAT) as overall_rating,
                CAST(JSON_extract(player_attributes, '$.potential') AS FLOAT) as potential,
                JSON_extract(player_attributes, '$.preferred_foot') as preferred_foot,
                JSON_extract(player_attributes, '$.attacking_work_rate') as attacking_work_rate,
                JSON_extract(player_attributes, '$.defensive_work_rate') as defensive_work_rate,
                CAST(JSON_extract(player_attributes, '$.crossing') AS FLOAT) as crossing,
                CAST(JSON_extract(player_attributes, '$.finishing') AS FLOAT) as finishing,
                CAST(JSON_extract(player_attributes, '$.heading_accuracy') AS FLOAT) as heading_accuracy,
                CAST(JSON_extract(player_attributes, '$.short_passing') AS FLOAT) as short_passing,
                CAST(JSON_extract(player_attributes, '$.volleys') AS FLOAT) as volleys,
                CAST(JSON_extract(player_attributes, '$.dribbling') AS FLOAT) as dribbling,
                CAST(JSON_extract(player_attributes, '$.curve') AS FLOAT) as curve,
                CAST(JSON_extract(player_attributes, '$.free_kick_accuracy') AS FLOAT) as free_kick_accuracy,
                CAST(JSON_extract(player_attributes, '$.long_passing') AS FLOAT) as long_passing,
                CAST(JSON_extract(player_attributes, '$.ball_control') AS FLOAT) as ball_control,
                CAST(JSON_extract(player_attributes, '$.acceleration') AS FLOAT) as acceleration,
                CAST(JSON_extract(player_attributes, '$.sprint_speed') AS FLOAT) as sprint_speed,
                CAST(JSON_extract(player_attributes, '$.agility') AS FLOAT) as agility,
                CAST(JSON_extract(player_attributes, '$.reactions') AS FLOAT) as reactions,
                CAST(JSON_extract(player_attributes, '$.balance') AS FLOAT) as balance,
                CAST(JSON_extract(player_attributes, '$.shot_power') AS FLOAT) as shot_power,
                CAST(JSON_extract(player_attributes, '$.jumping') AS FLOAT) as jumping,
                CAST(JSON_extract(player_attributes, '$.stamina') AS FLOAT) as stamina,
                CAST(JSON_extract(player_attributes, '$.strength') AS FLOAT) as strength,
                CAST(JSON_extract(player_attributes, '$.long_shots') AS FLOAT) as long_shots,
                CAST(JSON_extract(player_attributes, '$.aggression') AS FLOAT) as aggression,
                CAST(JSON_extract(player_attributes, '$.interceptions') AS FLOAT) as interceptions,
                CAST(JSON_extract(player_attributes, '$.positioning') AS FLOAT) as positioning,
                CAST(JSON_extract(player_attributes, '$.vision') AS FLOAT) as vision,
                CAST(JSON_extract(player_attributes, '$.penalties') AS FLOAT) as penalties,
                CAST(JSON_extract(player_attributes, '$.marking') AS FLOAT) as marking,
                CAST(JSON_extract(player_attributes, '$.standing_tackle') AS FLOAT) as standing_tackle,
                CAST(JSON_extract(player_attributes, '$.sliding_tackle') AS FLOAT) as sliding_tackle,
                CAST(JSON_extract(player_attributes, '$.gk_diving') AS FLOAT) as gk_diving,
                CAST(JSON_extract(player_attributes, '$.gk_handling') AS FLOAT) as gk_handling,
                CAST(JSON_extract(player_attributes, '$.gk_kicking') AS FLOAT) as gk_kicking,
                CAST(JSON_extract(player_attributes, '$.gk_positioning') AS FLOAT) as gk_positioning,
                CAST(JSON_extract(player_attributes, '$.gk_reflexes') AS FLOAT) as gk_reflexes
            FROM Player_Attributes
        )
        SELECT cte_p_a.*,
            Player.player_name,
            Player.birthday,
            Player.height,
            Player.weight
        FROM CTE_Player_Attributes as cte_p_a
        JOIN Player ON cte_p_a.player_fifa_api_id = Player.player_fifa_api_id
            AND cte_p_a.player_fifa_api_id = Player.player_fifa_api_id;

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Player_Attributes_Modified'):
            print("A tabela 'Player_Attributes_Modified' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        query = '''
                    WITH CTE_Player_Attributes AS (
                        SELECT
                            CAST(JSON_extract(player_attributes, '$.id') AS INT) as id,
                            CAST(JSON_extract(player_attributes, '$.player_fifa_api_id') AS INT) as player_fifa_api_id,
                            CAST(JSON_extract(player_attributes, '$.player_api_id') AS INT) as player_api_id,
                            JSON_extract(player_attributes, '$.date') as date,
                            CAST(JSON_extract(player_attributes, '$.overall_rating') AS FLOAT) as overall_rating,
                            CAST(JSON_extract(player_attributes, '$.potential') AS FLOAT) as potential,
                            JSON_extract(player_attributes, '$.preferred_foot') as preferred_foot,
                            JSON_extract(player_attributes, '$.attacking_work_rate') as attacking_work_rate,
                            JSON_extract(player_attributes, '$.defensive_work_rate') as defensive_work_rate,
                            CAST(JSON_extract(player_attributes, '$.crossing') AS FLOAT) as crossing,
                            CAST(JSON_extract(player_attributes, '$.finishing') AS FLOAT) as finishing,
                            CAST(JSON_extract(player_attributes, '$.heading_accuracy') AS FLOAT) as heading_accuracy,
                            CAST(JSON_extract(player_attributes, '$.short_passing') AS FLOAT) as short_passing,
                            CAST(JSON_extract(player_attributes, '$.volleys') AS FLOAT) as volleys,
                            CAST(JSON_extract(player_attributes, '$.dribbling') AS FLOAT) as dribbling,
                            CAST(JSON_extract(player_attributes, '$.curve') AS FLOAT) as curve,
                            CAST(JSON_extract(player_attributes, '$.free_kick_accuracy') AS FLOAT) as free_kick_accuracy,
                            CAST(JSON_extract(player_attributes, '$.long_passing') AS FLOAT) as long_passing,
                            CAST(JSON_extract(player_attributes, '$.ball_control') AS FLOAT) as ball_control,
                            CAST(JSON_extract(player_attributes, '$.acceleration') AS FLOAT) as acceleration,
                            CAST(JSON_extract(player_attributes, '$.sprint_speed') AS FLOAT) as sprint_speed,
                            CAST(JSON_extract(player_attributes, '$.agility') AS FLOAT) as agility,
                            CAST(JSON_extract(player_attributes, '$.reactions') AS FLOAT) as reactions,
                            CAST(JSON_extract(player_attributes, '$.balance') AS FLOAT) as balance,
                            CAST(JSON_extract(player_attributes, '$.shot_power') AS FLOAT) as shot_power,
                            CAST(JSON_extract(player_attributes, '$.jumping') AS FLOAT) as jumping,
                            CAST(JSON_extract(player_attributes, '$.stamina') AS FLOAT) as stamina,
                            CAST(JSON_extract(player_attributes, '$.strength') AS FLOAT) as strength,
                            CAST(JSON_extract(player_attributes, '$.long_shots') AS FLOAT) as long_shots,
                            CAST(JSON_extract(player_attributes, '$.aggression') AS FLOAT) as aggression,
                            CAST(JSON_extract(player_attributes, '$.interceptions') AS FLOAT) as interceptions,
                            CAST(JSON_extract(player_attributes, '$.positioning') AS FLOAT) as positioning,
                            CAST(JSON_extract(player_attributes, '$.vision') AS FLOAT) as vision,
                            CAST(JSON_extract(player_attributes, '$.penalties') AS FLOAT) as penalties,
                            CAST(JSON_extract(player_attributes, '$.marking') AS FLOAT) as marking,
                            CAST(JSON_extract(player_attributes, '$.standing_tackle') AS FLOAT) as standing_tackle,
                            CAST(JSON_extract(player_attributes, '$.sliding_tackle') AS FLOAT) as sliding_tackle,
                            CAST(JSON_extract(player_attributes, '$.gk_diving') AS FLOAT) as gk_diving,
                            CAST(JSON_extract(player_attributes, '$.gk_handling') AS FLOAT) as gk_handling,
                            CAST(JSON_extract(player_attributes, '$.gk_kicking') AS FLOAT) as gk_kicking,
                            CAST(JSON_extract(player_attributes, '$.gk_positioning') AS FLOAT) as gk_positioning,
                            CAST(JSON_extract(player_attributes, '$.gk_reflexes') AS FLOAT) as gk_reflexes
                        FROM Player_Attributes
                    )
                    SELECT cte_p_a.*,
                        Player.player_name,
                        Player.birthday,
                        Player.height,
                        Player.weight
                    FROM CTE_Player_Attributes as cte_p_a
                    JOIN Player ON cte_p_a.player_fifa_api_id = Player.player_fifa_api_id
                        AND cte_p_a.player_fifa_api_id = Player.player_fifa_api_id;
                '''
        
        player_attributes_modified = sql(query, self.engine)
        player_attributes_modified['date'] = pd.to_datetime(player_attributes_modified['date'])
        player_attributes_modified['birthday'] = pd.to_datetime(player_attributes_modified['birthday'])

        # Criar a tabela no banco de dados
        columns = [
            Column('id', Integer, primary_key=True),
            Column('player_fifa_api_id', Integer),
            Column('player_api_id', Integer),
            Column('date', Date),
            Column('overall_rating', Float),
            Column('potential', Float),
            Column('preferred_foot', String),
            Column('attacking_work_rate', String),
            Column('defensive_work_rate', String),
            Column('crossing', Float),
            Column('finishing', Float),
            Column('heading_accuracy', Float),
            Column('short_passing', Float),
            Column('volleys', Float),
            Column('dribbling', Float),
            Column('curve', Float),
            Column('free_kick_accuracy', Float),
            Column('long_passing', Float),
            Column('ball_control', Float),
            Column('acceleration', Float),
            Column('sprint_speed', Float),
            Column('agility', Float),
            Column('reactions', Float),
            Column('balance', Float),
            Column('shot_power', Float),
            Column('jumping', Float),
            Column('stamina', Float),
            Column('strength', Float),
            Column('long_shots', Float),
            Column('aggression', Float),
            Column('interceptions', Float),
            Column('positioning', Float),
            Column('vision', Float),
            Column('penalties', Float),
            Column('marking', Float),
            Column('standing_tackle', Float),
            Column('sliding_tackle', Float),
            Column('gk_diving', Float),
            Column('gk_handling', Float),
            Column('gk_kicking', Float),
            Column('gk_positioning', Float),
            Column('gk_reflexes', Float),
            Column('player_name', String),
            Column('birthday', Date),
            Column('height', Float),
            Column('weight', Integer)
        ]

        # Definir a estrutura da tabela usando o Table
        metadata = MetaData()
        player_attributes_modified_table = Table('Player_Attributes_Modified', metadata, *columns)
        
        # Criar a tabela no banco de dados
        metadata.create_all(self.engine)

        # Criar uma sessão
        session = Session(self.engine)

        # Inserir os dados
        data_list = player_attributes_modified.to_dict(orient='records')
        for data_row in data_list:
            x = player_attributes_modified_table.insert().values(data_row)
            session.execute(x)

        # Confirmar as alterações e fechar a sessão
        session.commit()
        session.close()
        print(f"Tabela 'Player_Attributes_Modified' criada no banco de dados. Inseridos '{len(player_attributes_modified)}' registros")

# %%