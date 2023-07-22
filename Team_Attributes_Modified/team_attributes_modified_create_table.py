# %%
import pandas as pd
from sqlalchemy import inspect
from Infra.database_utils import sql

# %%
class TeamAttributesModifiedTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir da query.

        WITH CTE_Team_Attributes AS (
            SELECT
                CAST(JSON_extract(Team_Attributes, '$.id') AS INT) as id,
                CAST(JSON_extract(Team_Attributes, '$.team_fifa_api_id') AS INT) as team_fifa_api_id,
                CAST(JSON_extract(Team_Attributes, '$.team_api_id') AS INT) as team_api_id,
                JSON_extract(Team_Attributes, '$.date') as date,
                CAST(JSON_extract(Team_Attributes, '$.buildUpPlaySpeed') AS INT) as buildUpPlaySpeed,
                JSON_extract(Team_Attributes, '$.buildUpPlaySpeedClass') as buildUpPlaySpeedClass,
                CAST(JSON_extract(Team_Attributes, '$.buildUpPlayDribbling') AS FLOAT) as buildUpPlayDribbling,
                JSON_extract(Team_Attributes, '$.buildUpPlayDribblingClass') as buildUpPlayDribblingClass,
                CAST(JSON_extract(Team_Attributes, '$.buildUpPlayPassing') AS INT) as buildUpPlayPassing,
                JSON_extract(Team_Attributes, '$.buildUpPlayPassingClass') as buildUpPlayPassingClass,
                JSON_extract(Team_Attributes, '$.buildUpPlayPositioningClass') as buildUpPlayPositioningClass,
                CAST(JSON_extract(Team_Attributes, '$.chanceCreationPassing') AS INT) as chanceCreationPassing,
                JSON_extract(Team_Attributes, '$.chanceCreationPassingClass') as chanceCreationPassingClass,
                CAST(JSON_extract(Team_Attributes, '$.chanceCreationCrossing') AS INT) as chanceCreationCrossing,
                JSON_extract(Team_Attributes, '$.chanceCreationCrossingClass') as chanceCreationCrossingClass,
                CAST(JSON_extract(Team_Attributes, '$.chanceCreationShooting') AS INT) as chanceCreationShooting,
                JSON_extract(Team_Attributes, '$.chanceCreationShootingClass') as chanceCreationShootingClass,
                JSON_extract(Team_Attributes, '$.chanceCreationPositioningClass') as chanceCreationPositioningClass,
                CAST(JSON_extract(Team_Attributes, '$.defencePressure') AS INT) as defencePressure,
                JSON_extract(Team_Attributes, '$.defencePressureClass') as defencePressureClass,
                CAST(JSON_extract(Team_Attributes, '$.defenceAggression') AS INT) as defenceAggression,
                JSON_extract(Team_Attributes, '$.defenceAggressionClass') as defenceAggressionClass,
                CAST(JSON_extract(Team_Attributes, '$.defenceTeamWidth') AS INT) as defenceTeamWidth,
                JSON_extract(Team_Attributes, '$.defenceTeamWidthClass') as defenceTeamWidthClass,
                JSON_extract(Team_Attributes, '$.defenceDefenderLineClass') as defenceDefenderLineClass
            FROM Team_Attributes
        )
        SELECT cte_t_a.*,
            Team.team_long_name,
            Team.team_short_name
        FROM CTE_Team_Attributes as cte_t_a
        JOIN Team ON cte_t_a.team_api_id = Team.team_api_id
            AND cte_t_a.team_fifa_api_id = Team.team_fifa_api_id;

        Args:
            nome_tabela (str): O nome da tabela a ser criada.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Team_Attributes_Modified'):
            print("A tabela 'Team_Attributes_Modified' já existe no banco de dados.")

        # Decisões tomadas com base na análise do Jupyter Notebook 'Analysis.ipynb'
        query = '''
                WITH CTE_Team_Attributes AS (
                    SELECT
                        CAST(JSON_extract(Team_Attributes, '$.id') AS INT) as id,
                        CAST(JSON_extract(Team_Attributes, '$.team_fifa_api_id') AS INT) as team_fifa_api_id,
                        CAST(JSON_extract(Team_Attributes, '$.team_api_id') AS INT) as team_api_id,
                        JSON_extract(Team_Attributes, '$.date') as date,
                        CAST(JSON_extract(Team_Attributes, '$.buildUpPlaySpeed') AS INT) as buildUpPlaySpeed,
                        JSON_extract(Team_Attributes, '$.buildUpPlaySpeedClass') as buildUpPlaySpeedClass,
                        CAST(JSON_extract(Team_Attributes, '$.buildUpPlayDribbling') AS FLOAT) as buildUpPlayDribbling,
                        JSON_extract(Team_Attributes, '$.buildUpPlayDribblingClass') as buildUpPlayDribblingClass,
                        CAST(JSON_extract(Team_Attributes, '$.buildUpPlayPassing') AS INT) as buildUpPlayPassing,
                        JSON_extract(Team_Attributes, '$.buildUpPlayPassingClass') as buildUpPlayPassingClass,
                        JSON_extract(Team_Attributes, '$.buildUpPlayPositioningClass') as buildUpPlayPositioningClass,
                        CAST(JSON_extract(Team_Attributes, '$.chanceCreationPassing') AS INT) as chanceCreationPassing,
                        JSON_extract(Team_Attributes, '$.chanceCreationPassingClass') as chanceCreationPassingClass,
                        CAST(JSON_extract(Team_Attributes, '$.chanceCreationCrossing') AS INT) as chanceCreationCrossing,
                        JSON_extract(Team_Attributes, '$.chanceCreationCrossingClass') as chanceCreationCrossingClass,
                        CAST(JSON_extract(Team_Attributes, '$.chanceCreationShooting') AS INT) as chanceCreationShooting,
                        JSON_extract(Team_Attributes, '$.chanceCreationShootingClass') as chanceCreationShootingClass,
                        JSON_extract(Team_Attributes, '$.chanceCreationPositioningClass') as chanceCreationPositioningClass,
                        CAST(JSON_extract(Team_Attributes, '$.defencePressure') AS INT) as defencePressure,
                        JSON_extract(Team_Attributes, '$.defencePressureClass') as defencePressureClass,
                        CAST(JSON_extract(Team_Attributes, '$.defenceAggression') AS INT) as defenceAggression,
                        JSON_extract(Team_Attributes, '$.defenceAggressionClass') as defenceAggressionClass,
                        CAST(JSON_extract(Team_Attributes, '$.defenceTeamWidth') AS INT) as defenceTeamWidth,
                        JSON_extract(Team_Attributes, '$.defenceTeamWidthClass') as defenceTeamWidthClass,
                        JSON_extract(Team_Attributes, '$.defenceDefenderLineClass') as defenceDefenderLineClass
                    FROM Team_Attributes
                )
                SELECT cte_t_a.*,
                    Team.team_long_name,
                    Team.team_short_name
                FROM CTE_Team_Attributes as cte_t_a
                JOIN Team ON cte_t_a.team_api_id = Team.team_api_id
                    AND cte_t_a.team_fifa_api_id = Team.team_fifa_api_id;
            '''
        
        team_attributes_modified = sql(query, self.engine)
        team_attributes_modified['date'] = pd.to_datetime(team_attributes_modified['date'])
        team_attributes_modified.drop_duplicates(subset=['id'], keep='first', inplace=True)

        # Criar a tabela no banco de dados
        team_attributes_modified.to_sql('Team_Attributes_Modified', self.engine, index=False, if_exists='replace')
        print(f"Tabela 'Team_Attributes_Modified' criada no banco de dados. Inseridos '{len(team_attributes_modified)}' registros")

# %%