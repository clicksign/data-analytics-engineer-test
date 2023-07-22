# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sqlalchemy import create_engine, inspect, text
import streamlit as st
import json
# %%
engine = create_engine(f'sqlite:///Data/test_analytics_engineer.db', echo=False)
def sql_df(query):
    with engine.connect() as conexao:
        consulta = conexao.execute(text(query))
        dados = consulta.fetchall()
    return pd.DataFrame(dados,columns=consulta.keys())# type:ignore

def player_attributes(query):
    player_attributes = sql_df(query)
    player_attributes['Player_Attributes'] = player_attributes['Player_Attributes'].apply(json.loads)
    player_attributes = pd.json_normalize(player_attributes['Player_Attributes'])# type:ignore
    player_attributes['id'] = player_attributes['id'].astype(int)
    player_attributes['player_fifa_api_id'] = player_attributes['player_fifa_api_id'].astype(int)
    player_attributes['player_api_id'] = player_attributes['player_api_id'].astype(int)
    player_attributes['date'] = pd.to_datetime(player_attributes['date'])
    player_attributes.dropna(inplace=True)
    return player_attributes

def main():
    st.set_page_config(layout="wide")
    st.title('Desafios propostos no test_analytics_engineer')
    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Desafio 1", "Desafio 2", "Desafio 3", "Desafio 3 - Análises", "Desafio 4", "Desafio 5"])

    with tab0:
        '''
        **Questão 1 - Utilize Python**

        - Como primeiro passo do desafio, faça a leitura/importação desses arquivos via python e realize o upload/carregamento desses dados em um banco SQLite.

            1. Crie um schema chamado: test_analytics_engineer
            2. Crie as tabelas com os mesmos nomes dos arquivos .csv
            3. Respeite a tipagem e os nomes das colunas dos arquivos .csv
        
        '''
        st.write("\n")
        '''
        Os passos da análise descritiva dos dados podem sem acompanhadas no Jupyter Notebook 'Analysis.ipynb'
        
        - Foi criado uma estrutura de pastas com o nome das tabelas para os scripts de criação.
        - Foi uma pasta chamada **Infra** com os códigos de conexão com o SQLite para criar as tabelas e consultar as queries.
        - Foi criado um notebook **analysis.ipynb** como as etapas das análises descritiva e exploratória.
        - O arquivo **test_analytics_engineer.db** usado no SQLite é gerado na pasta Data, juntamento com os arquivos **.csv** com os dados para as tabelas.
        - É utilizado a biblioteca sqlalchemy para manipular e consultar o banco.
            - Para ter acesso aos gráficos e tabelas nessa pagina certifique-se de ter gerado as tabelas com o comando Python main.py. 
        '''
        st.write("\n")
        st.markdown(
            """
            ```python
            # Para instalar as bibliotecas necessárias.

            pip install -r requirements.txt

            # Para gerar criar as tabelas no SQLite

            Python main.py
            ```
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '<span class="small-font">Tive timeout algumas vezes ao criar as tabelas no aquivo .csv com maior quantidade de dados (exclui e rodei novamente)</span>',
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown('***Trecho do código no notebook para conectar com o banco e validar as tabelas criadas.***')
        st.markdown(
            """
            ```python
            engine = create_engine(f'sqlite:///Data/test_analytics_engineer.db', echo=False)
            
            inspector = inspect(engine)
            print(inspector.get_table_names())
            
            # Retorna os nomes das tabelas criadas:
            # ['Country', 'League', 'Match', 'Match_Modified', 'Player', 'Player_Attributes', 'Player_Attributes_Modified', 'Relations', 'Team', 'Team_Attributes', 'Team_Attributes_Modified']
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown(
            """
            ```python
            query = 'SELECT * FROM Country'
            df_country = sql_df(query)
            df_country.head(), 'Team', 'Team_Attributes', 'Team_Attributes_Modified']

            query = 'SELECT * FROM League'
            df_league = sql_df(query)
            df_league.head()

            query = 'SELECT * FROM Match'
            df_match = sql_df(query)
            df_match.head()

            query = 'SELECT * FROM Player_Attributes'
            df_player_attributes = sql_df(query)
            df_player_attributes.head()

            query = 'SELECT * FROM Player'
            df_player = sql_df(query)
            df_player.head()

            query = 'SELECT * FROM Team_Attributes'
            df_team_attributes = sql_df(query)
            df_team_attributes.head()

            query = 'SELECT * FROM Team'
            df_team = sql_df(query)
            df_team.head()
            ```
            """,
            unsafe_allow_html=True
        )

    with tab1:
        '''
        **Questão 2 - Utilize SQL**

        - Estabeleça uma relação entre as tabelas Player e Player_Attributes em uma nova tabela, chamada ‘Player_Attributes_Modified’, onde cada key do json é uma nova coluna.
        - Faça o mesmo para a relação Team e Team_Attributes, como o nome para a tabela ‘Team_Attributes_Modified’

        - Crie uma tabela chamada Match_Modified cuja coluna seja representada como JSON, onde as chaves precisam ser referentes às colunas da tabela Match, sendo elas: 
            - id
            - match_api_id
            - home_team_api_id
            - away_team_api_id        
        '''
        st.write("\n")
        '''
        Os passos da análise descritiva dos dados podem sem acompanhadas no Jupyter Notebook 'analysis.ipynb'
        
        - Para criar as 3 tabelas foram lidos os dados das tabelas já existentes nos SQLite, tratados os tipos com a biblioteca Pandas.
        - Para ler o JSON utilizei o **JSON_extract** e **json_normalize** do Pandas para as análises. 
        '''
        st.write("\n")
        st.markdown('***Trecho do código no notebook para criar tabela Player_Attributes_Modified.***')
        st.markdown(
            """
            ```python
                query = '''WITH CTE_Player_Attributes AS (
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
                AND cte_p_a.player_fifa_api_id = Player.player_fifa_api_id
            '''
            player_attributes_modified = sql_df(query)
            player_attributes_modified['date'] = pd.to_datetime(player_attributes_modified['date'])
            player_attributes_modified['birthday'] = pd.to_datetime(player_attributes_modified['birthday'])
            player_attributes_modified.head()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown('***Trecho do código no notebook para criar tabela Team_Attributes_Modified.***')
        st.markdown(
            """
            ```python
                query = '''WITH CTE_Team_Attributes AS (
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
                AND cte_t_a.team_fifa_api_id = Team.team_fifa_api_id
            '''
            team_attributes_modified = sql_df(query)
            team_attributes_modified['date'] = pd.to_datetime(team_attributes_modified['date'])
            team_attributes_modified.drop_duplicates(subset=['id'], keep='first', inplace=True)
            team_attributes_modified.head()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown('***Trecho do código no notebook para converter os dados de um **DataFrame** Pandas para o formato **JSON** criar tabela Match_Modified.***')
        st.markdown(
            """
            ```python
                query = '''
                    SELECT 
                        CAST(id AS VARCHAR) AS id,
                        CAST(match_api_id AS VARCHAR) AS match_api_id,
                        CAST(home_team_api_id AS VARCHAR) AS home_team_api_id,
                        CAST(away_team_api_id AS VARCHAR) AS away_team_api_id
                    FROM Match
                '''
                df_match_modified = sql_df(query)
                df_match_modified['Match_Modified'] = df_match_modified.apply(lambda row: {
                    'id': row['id'],
                    'match_api_id': row['match_api_id'],
                    'home_team_api_id': row['home_team_api_id'],
                    'away_team_api_id': row['away_team_api_id']
                }, axis=1)

                match_modified = pd.DataFrame(df_match_modified['Match_Modified'])
                match_modified['id'] = match_modified.index.astype(str)
                match_modified = match_modified[['id', 'Match_Modified']]
                match_modified.head()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown('***Trecho do código no notebook para as novas tabelas criadas.***')
        st.markdown(
            """
            ```python
                query = 'SELECT * FROM Player_Attributes_Modified'
                df_team = sql_df(query)
                df_team.head()

                query = 'SELECT * FROM Team_Attributes_Modified'
                df_team = sql_df(query)
                df_team.head()

                query = 'SELECT * FROM Match_Modified'
                df_team = sql_df(query)
                df_team.head()
            ```
            """,
            unsafe_allow_html=True
        )

    with tab2:
        '''
        **Questão 3 - Utilize SQL ou Python**

        - Faça uma análise exploratória dos dados no sentido de validar a qualidade dos dados destes datasets.
        - Use sua criatividade e imaginação para buscar “sujeiras” na base de dados.
        - Lembre-se que queremos gerar insights com dados, então realize relações com tabelas que nos forneçam alguma informação relevante para os dados tratados analisados. Crie análises exploratórias dos dados.
        
        - Exemplos:
            - Qual a proporção entre jogadores destros e canhotos? Quais os seus nomes?
            - Qual o nome do país com maior saldo de gols.
        '''
        st.write("\n")
        '''
        - A analises e limpeza de dos dados estão presentes no Jupyter Notebook 'analysis.ipynb'
        - Tomei a liberdade de trabalhar nos dados dos arquivos **.csv** possíveis antes de criar as tabelas.
            - Country.csv, League.csv, Match.csv, Player.csv', Team.csc
        - Os que não foram possíveis criei as tabelas com os dados no formato **JSON** por conter desafios com **SQL** fazendo buscas nesse formato.
            - Player_Attributes.csv
            - Team_Attributes.csv
        '''
        st.markdown('***Trecho do código no notebook com exemplos dos ajustes nos dados.***')
        '''Temos números duplicados nulos e coluna id como float no Country.csv.'''
        st.markdown(
            """
            ```python
            country = pd.read_csv('Data/Country.csv')
            country.info()

            print('Nulos: ', match.isnull().sum())
            print('---')
            print('id duplicados: ', match.id.duplicated().sum())
            print('Duplicados: ', match.duplicated().sum())

            country.dropna(inplace=True)
            country.isnull().sum()

            country['id'] = country['id'].astype(str).str.rstrip('.0').astype(int)
            country.drop_duplicates(subset=['id'], keep='first', inplace=True)
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        '''No League.csv os dados estão corretos.'''
        st.write("\n")
        '''No Match.csv foram encontrados dados nulos e sem tipos definidos.'''
        st.markdown(
            """
            ```python
            match = pd.read_csv('Data/Match.csv')
            match.info()

            # Formatar os tipos
            match['date'] = pd.to_datetime(match['date'])
            match.date.info()
            
            # Para armazenar nas tabela não removi, para podes em outros desafios tratar os nulos nas queries.
            print('Nulos: ', country.isnull().sum())
            print('---')
            print('Ids duplicados: ', country.id.duplicated().sum())
            print('Países duplicados: ', country.name.duplicated().sum())

            # Para análises removi os dados nulos.
            match.dropna(inplace=True)
            match.isnull().sum()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        '''No Player_Attributes.csv criei a tabela com os dados no formato **JSON** por ser utilizado nos outros desafios em queries. Mas para análises utilizei o Pandas'''
        st.markdown(
            """
            ```python
            player_attributes = pd.read_csv('Data/Player_Attributes.csv')
            # Converti de json para dataframe
            player_attributes['Player_Attributes'] = player_attributes['Player_Attributes'].apply(json.loads)
            player_attributes = pd.json_normalize(player_attributes['Player_Attributes'])# type:ignore
            player_attributes.head()
            player_attributes.info()

            # formatação de tipos
            player_attributes['id'] = player_attributes['id'].astype(int)
            player_attributes['player_fifa_api_id'] = player_attributes['player_fifa_api_id'].astype(int)
            player_attributes['player_api_id'] = player_attributes['player_api_id'].astype(int)
            player_attributes['date'] = pd.to_datetime(player_attributes['date'])
            player_attributes.dtypes
            
            # Para armazenar nas tabela não removi, para podes em outros desafios tratar os nulos nas queries.
            print('Nulos: ', player_attributes.isnull().sum())
            print('---')
            print('id duplicados: ', player_attributes.id.duplicated().sum())
            print('Duplicados: ', player_attributes.duplicated().sum())

            # Para análises removi os dados nulos.
            player_attributes.dropna(inplace=True)
            player_attributes.isnull().sum()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        '''No Player.csv não tem dados nulos nem duplicados apenas uma conversão de tipo'''
        st.markdown(
            """
            ```python
            player = pd.read_csv('Data/Player.csv')
            player.info()

            # Conversão de tipos
            player['birthday'] = pd.to_datetime(player['birthday'])
            player.dtypes

            print('Nulos: ', player.isnull().sum())
            print('---')
            print('id duplicados: ', player.id.duplicated().sum())
            print('Duplicados: ', player.duplicated().sum())    
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        '''No Team_Attributes.csv criei a tabela com os dados no formato **JSON** por ser utilizado nos outros desafios em queries. Mas para análises utilizei o Pandas'''
        st.markdown(
            """
            ```python
            player_attributes = pd.read_csv('Data/Team_Attributes.csv')
            
            # Converti de json para dataframe
            team_attributes['Team_Attributes'] = team_attributes['Team_Attributes'].apply(json.loads)
            team_attributes = pd.json_normalize(team_attributes['Team_Attributes'])# type:ignore
            team_attributes.head()

            # formatação de tipos
            team_attributes['id'] = team_attributes['id'].astype(int)
            team_attributes['team_fifa_api_id'] = team_attributes['team_fifa_api_id'].astype(int)
            team_attributes['team_api_id'] = team_attributes['team_api_id'].astype(int)
            team_attributes['date'] = pd.to_datetime(team_attributes['date'])
            team_attributes['buildUpPlaySpeed'] = team_attributes['buildUpPlaySpeed'].astype(int)
            team_attributes['buildUpPlayPassing'] = team_attributes['buildUpPlayPassing'].astype(int)
            team_attributes['chanceCreationPassing'] = team_attributes['chanceCreationPassing'].astype(int)
            team_attributes['chanceCreationCrossing'] = team_attributes['chanceCreationCrossing'].astype(int)
            team_attributes['chanceCreationShooting'] = team_attributes['chanceCreationShooting'].astype(int)
            team_attributes['defencePressure'] = team_attributes['defencePressure'].astype(int)
            team_attributes['defenceAggression'] = team_attributes['defenceAggression'].astype(int)
            team_attributes['defenceTeamWidth'] = team_attributes['defenceTeamWidth'].astype(int)
            team_attributes.dtypes
            
            # Para armazenar nas tabela não removi os nunos, para podes em outros desafios tratar os nulos nas queries.
            print('Nulos: ', team_attributes.isnull().sum())
            print('---')
            print('id duplicados: ', team_attributes.id.duplicated().sum())
            print('Duplicados: ', team_attributes.duplicated().sum())

            # Para análises removi os dados nulos e duplicados.
            duplicated_ids = team_attributes[team_attributes.duplicated(subset="id", keep=False)]
            team_attributes.drop_duplicates(subset=['id'], keep='first', inplace=True)
            print('id duplicados: ', team_attributes.id.duplicated().sum())
            print('Duplicados: ', team_attributes.duplicated().sum())
            
            team_attributes.dropna(inplace=True)
            team_attributes.isnull().sum()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        '''No Team.csv removidos dado nulos e conversão de tipo'''
        st.markdown(
            """
            ```python
            team = pd.read_csv('Data/Team.csv')
            team.info()

            print('Nulos: ', team.isnull().sum())
            print('---')
            print('id duplicados: ', team.id.duplicated().sum())
            print('Duplicados: ', team.duplicated().sum())

            # Remocao do nulos e conversão do team_fifa_api_id de ponto flutuante para inteiro removendo o **.0**
            team.dropna(inplace=True)
            team['team_fifa_api_id'] = team['team_fifa_api_id'].astype(str).str.rstrip('.0').astype(int)
            ```
            """,
            unsafe_allow_html=True
        )
    with tab3:
        '''
        Alguma análises sugeridas no desafio.
        '''
        st.write("\n")
        df_player_attributes = player_attributes('SELECT * FROM Player_Attributes')
        total = len(df_player_attributes)
        total_r = df_player_attributes[df_player_attributes['preferred_foot'] == 'right'].preferred_foot.count()
        total_l = df_player_attributes[df_player_attributes['preferred_foot'] == 'left'].preferred_foot.count()
        percentual_l = total_l/ total
        percentual_r = total_r/ total
        
        st.markdown(f"Total de jogadores: {total}")
        st.markdown(f"Total de destros: {total_r}")
        st.markdown(f"Total de canhotos: {total_l}")
        st.markdown("Percentual de destros: {:.2%}".format(percentual_r))
        st.markdown("Percentual de canhotos: {:.2%}".format(percentual_l))

        labels = ['Destro', 'Canhoto']
        values = df_player_attributes['preferred_foot'].value_counts()

        pie_trace = go.Pie(labels=labels, values=values, hoverinfo='label+percent', textinfo='percent+label', 
                        marker=dict(colors=['#2937fe', '#f8d124']), hole=0.3)

        layout = go.Layout(title='Distribuição entre destros e canhotos',
                        annotations=[{'text': f"Percentual de destros: {(round(percentual_r, 2) * 100)}%",
                                        'showarrow': False, 'x': .5, 'y': 1.1
                            }], showlegend=False)

        fig4 = go.Figure(data=[pie_trace], layout=layout)
        st.plotly_chart(fig4,  use_container_width = True)
        '''Notamos que a diferença entre destros para canhotos é muito grande'''
        st.write("\n")
        '''O gráfico foi gerado no notebook de análise utilizando as análises do pré-processamento dos dados do Player_Attributes.csv.'''
        st.markdown(
            """
            ```python

            # Trecho de código anterior foi inserido na aba **Desafio 2**
            total = len(player_attributes)
            total_r = player_attributes[player_attributes['preferred_foot'] == 'right'].preferred_foot.count()
            total_l = player_attributes[player_attributes['preferred_foot'] == 'left'].preferred_foot.count()

            percentual_l = total_l/ total
            percentual_r = total_r/ total

            print("Total de dados: ", total)
            print("Total de destros: ", total_r)
            print("Total de canhotos: ", total_l)
            print("Percentual de destros: ", (round(percentual_r, 2)*100), "%")
            print("Percentual de canhotos: ", (round(percentual_l, 2)*100), "%")

            # Gráfico
            labels = ['Destro', 'Canhoto']
            values = player_attributes['preferred_foot'].value_counts()

            pie_trace = go.Pie(labels=labels, values=values, hoverinfo='label+percent', textinfo='percent+label', 
                            marker=dict(colors=['#2937fe', '#f8d124']), hole=0.3)

            layout = go.Layout(title='Distribuição entre destros e canhotos',
                            annotations=[{'text': f"Percentual de destros: {(round(percentual_r, 2) * 100)}%",
                                            'showarrow': False, 'x': .5, 'y': 1.1
                                }], showlegend=False)

            fig4 = go.Figure(data=[pie_trace], layout=layout)
            fig4.show()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        '''O gráficos gráficos abaixo foram feitos usando queries na tabelas Player_Attributes_Modified, mostrando a consistência dos dados armazenado com os **.csv**'''
        query = '''
            SELECT player_name, AVG(overall_rating) AS overall_rating, preferred_foot
            FROM Player_Attributes_Modified
            GROUP BY 1, 3
            ORDER BY AVG(overall_rating) DESC
        '''
        # Pegar os jogadores por pé preferencial e ordenar pema média maior de  overall
        player_r_l = sql_df(query)
        right_footed = player_r_l[player_r_l['preferred_foot'] == 'right'].head(5).sort_values(by='overall_rating', ascending=True)
        left_footed = player_r_l[player_r_l['preferred_foot'] == 'left'].head(5).sort_values(by='overall_rating', ascending=True)
        fig5 = make_subplots(rows=1, cols=2, subplot_titles=("Destros", "Canhotos"))

        fig5.add_trace(go.Bar(
            y=right_footed['player_name'],
            x=right_footed['overall_rating'],
            name='Média de desempenho de destros',
            marker_color='#2937fe',
            orientation='h',
            showlegend=False
        ), row=1, col=1)

        fig5.add_trace(go.Bar(
            y=left_footed['player_name'],
            x=left_footed['overall_rating'],
            name='Média de desempenho de canhotos',
            marker_color='#f8d124',
            orientation='h',
            showlegend=False
        ), row=1, col=2)

        for i in range(1, 2):
            fig5.update_xaxes(title_text='Pé preferencial', row=1, col=i)
            fig5.update_yaxes(title_text='Média de desempenho', row=1, col=i)

        fig5.update_layout(title='Desempenho dos melhores jogadores destros e canhotos')
        st.plotly_chart(fig5,  use_container_width = True)
        '''Mesmo com a diferença entre destro e canhotos a média de desempenho é bem parecida tendo os melhores jogadores do mundo divididos entre destros e canhotos.'''
        query = '''
            SELECT
                team_long_name,
                SUM(
                    buildUpPlaySpeed +
                    buildUpPlayPassing +
                    chanceCreationPassing +
                    chanceCreationCrossing +
                    chanceCreationShooting +
                    defencePressure +
                    defenceAggression
                ) AS total_organization_score
            FROM Relations
            GROUP BY 1
            ORDER BY total_organization_score DESC;
        '''
        df_best_teams = sql_df(query)

        fig6 = make_subplots(rows=1, cols=2, subplot_titles=("5 Melhores Jogadores", "5 Melhores Times"))
        player_best = player_r_l.head(5).sort_values(by='overall_rating', ascending=False)
        fig6.add_trace(go.Bar(
            x=player_best['player_name'],
            y=player_best['overall_rating'],
            name='Média de desempenho dos melhores jogadores',
            marker_color='#2937fe',
            showlegend=False
        ), row=1, col=1)

        df_best_teams = df_best_teams.head(5).sort_values(by='total_organization_score', ascending=False)
        fig6.add_trace(go.Bar(
            x=df_best_teams['team_long_name'],
            y=df_best_teams['total_organization_score'],
            name='Total de desempenho dos melhores times',
            marker_color='#f8d124',
            showlegend=False
        ), row=1, col=2)

        fig6.update_layout(title='5 Melhores jogadores')
        st.plotly_chart(fig6,  use_container_width = True)
        '''
        Notamos que dos 5 melhores jogadores em desempenho apenas os dois primeiro continuam jogando profissionalmente **Cristiano Ronaldo** e **Lionel Messi**.
        
        E os times mais famosos como Real Madri, Barcelona e Manchester City nao estão na lista do melhores times.
        '''
        st.markdown(
            """
            ```python
                # Query dos melhores jogadores e pé de preferência.
                query = '''
                    SELECT player_name, AVG(overall_rating) AS overall_rating, preferred_foot
                    FROM Player_Attributes_Modified
                    GROUP BY 1, 3
                    ORDER BY AVG(overall_rating) DESC
                '''
                player_r_l = sql_df(query)
                right_footed = player_r_l[player_r_l['preferred_foot'] == 'right'].head(6)
                left_footed = player_r_l[player_r_l['preferred_foot'] == 'left'].head(9)

                # Query para os melhores times
                query = '''
                    SELECT
                        team_long_name,
                        SUM(
                            buildUpPlaySpeed +
                            buildUpPlayPassing +
                            chanceCreationPassing +
                            chanceCreationCrossing +
                            chanceCreationShooting +
                            defencePressure +
                            defenceAggression
                        ) AS total_organization_score
                    FROM Relations
                    GROUP BY 1, 2, 3, 4
                    ORDER BY total_organization_score DESC;
                '''
                df_best_teams = sql_df(query)
                df_best_teams
                '''
            ```
            """,
            unsafe_allow_html=True
        )
        query = '''
                SELECT
                    name,
                    SUM(home_team_goal + away_team_goal) AS total_goal
                FROM Match
                JOIN Country ON Country.id = Match.country_id
                GROUP BY 1
                ORDER BY total_goal DESC
            '''
        gols = sql_df(query)
        
        fig7 =  px.bar(gols, x='name', y='total_goal',
             title='Países com maior quantidade de gols marcados.',
             labels={'total_goal': 'Quantidade de Gols', 'name': 'País'},
             color_discrete_sequence=['#2937fe'])

        st.plotly_chart(fig7,  use_container_width = True)
        '''
        Notamos que os primeiros país em saldo de gols são os países com as ligas mais ricas e com os melhores jogadores que dentem a fazer mais gols
        '''

        query = '''
            WITH cte_best AS (
                SELECT player_name
                FROM Player_Attributes_Modified
                GROUP BY 1
                ORDER BY AVG(overall_rating) DESC
                LIMIT 5
            )
            SELECT Player_Attributes_Modified.player_name, date, AVG(Player_Attributes_Modified.overall_rating) AS overall_rating
            FROM Player_Attributes_Modified
            INNER JOIN cte_best ON cte_best.player_name = Player_Attributes_Modified.player_name
            GROUP BY Player_Attributes_Modified.player_name, date
            ORDER BY overall_rating DESC
        '''
        player_h = sql_df(query)

        player_h['date'] = pd.to_datetime(player_h['date'])
        player_h = player_h.sort_values(by=['player_name', 'date'])
        traces = []
        for player_name, data in player_h.groupby('player_name'):
            trace = go.Scatter(
                x=data['date'],
                y=data['overall_rating'],
                mode='lines',
                name=player_name
            )
            traces.append(trace)

        layout = go.Layout(
            title='Evolução da média do desempenho do 5 melhores jogadores',
            xaxis=dict(title='Data de avaliação'),
            yaxis=dict(title='Desempenho'),
        )
        
        fig8 = go.Figure(data=traces, layout=layout)
        st.plotly_chart(fig8,  use_container_width = True)
        '''
        Notamos a história do desempenho dos melhores jogadores do mundo e sua constância após o inicio da carreira e antes da aposentadoria.
        '''
        '''
        Queries utilizadas para geras os gráficos acima.'''
        st.markdown(
            """
            ```python
                # Query dos países mais goleadores.
                query = '''
                        SELECT
                            name,
                            SUM(home_team_goal + away_team_goal) AS total_goal
                        FROM Match
                        JOIN Country ON Country.id = Match.country_id
                        GROUP BY 1
                        ORDER BY total_goal DESC
                    '''
                gols = sql_df(query)
                gols.head()

                # Query para evolução dos melhores jogadores
                query = '''
                    WITH cte_best AS (
                        SELECT player_name
                        FROM Player_Attributes_Modified
                        GROUP BY 1
                        ORDER BY AVG(overall_rating) DESC
                        LIMIT 5
                    )
                    SELECT Player_Attributes_Modified.player_name, date, AVG(Player_Attributes_Modified.overall_rating) AS overall_rating
                    FROM Player_Attributes_Modified
                    INNER JOIN cte_best ON cte_best.player_name = Player_Attributes_Modified.player_name
                    GROUP BY Player_Attributes_Modified.player_name, date
                    ORDER BY overall_rating DESC
                '''
                player_h = sql_df(query)
                player_h.head()
            ```
            """,
            unsafe_allow_html=True
        )

    with tab4:
        '''
        **Questão 4 - Utilize SQL**

        - Encontre uma relação de dados entre as tabelas League, Country, Team_Attributes e Player, crie uma nova tabela chamada 'Relations'

        - Exemplo:
            - Esquematize uma relação entre a altura e peso dos jogadores de forma isolada, com seu rendimento.
            - Dica: Criar 3 intervalos entre os 6 valores com maiores contagens para estes dois parâmetros.
        '''
        st.write("\n")
        '''
        Os passos da análise descritiva dos dados podem sem acompanhadas no Jupyter Notebook 'analysis.ipynb'
        
        - Para tentar encontrar uma ligação entra as tabelas sugeridas e criar a nova tabela **Relations**
        - Tomei a liberdade de pesquisar na internet de qual país e liga é cada time e vou adicionar para ligar as tabelas **Team_Attributes_Modified**, **Country** e **League**.
        - Para isso realizei um mapeamento com Pandas e utilizei a tabela **Team_Attributes_Modified** criada anteriormente unindo os dados da tabela **Team**
        - Para ler o JSON utilizei o **JSON_extract** e **json_normalize** do Pandas para as análises. 
        '''
        st.write("\n")
        st.markdown(
            '<span class="small-font">Não encontrei uma coluna para vinculo entre a tabela **Player** e as demais, sem usar dados externos.</span>',
            unsafe_allow_html=True
        )
        st.markdown('***Trecho do código no notebook para criar tabela Relations.***')
        st.markdown(
            """
            ```python
                query = 'SELECT * FROM Team_Attributes_Modified'
                df_player_attributes = sql_df(query)
                team_to_country_map = {
                    'AAR': 1,
                    'ABE': 1729,
                    # comentado trecho da query por conter muitas linhas para mapear.
                    'ZAW': 21518,
                    'ZUL': 21518
                }
                df_player_attributes["country_id"] = df_player_attributes["team_short_name"].map(team_to_country_map)# type:ignore
                query = '''
                    SELECT 
                        League.id, 
                        League.country_id,
                        League.name as league_name,
                        Country.name as country_name
                    FROM Country
                    JOIN League ON League.country_id = Country.id;
                '''
                df_league_country = sql_df(query)

                # Merge dos Dataframes pela coluna "country_id" mantendo apenas a coluna com o nome do país
                df_relations = pd.merge(df_player_attributes, df_league_country[['country_id', 'league_name', 'country_name']], left_on='country_id', right_on='country_id', how='inner')
                df_relations.head()
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown(
            '<span class="small-font">Query criada para gerar o exemplo sugerido.</span>',
            unsafe_allow_html=True
        )
        st.markdown(
            """
            ```python
                query = '''
                WITH height AS (
                    SELECT
                        height,
                        (ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) + 1) / 2 as interval,
                        ROUND(AVG(weight), 2) AS avg_weight,
                        COUNT(*) AS count_height,
                        ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) as row_number_height
                    FROM Player_Attributes_Modified
                    GROUP BY height
                    ORDER BY count_height DESC
                    LIMIT 6
                ),
                weight AS (
                    SELECT
                        weight,
                        (ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) + 1) / 2 as interval,
                        ROUND(AVG(height), 2) AS avg_height,
                        COUNT(*) AS count_weight,
                        ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) as row_number_weight
                    FROM Player_Attributes_Modified
                    GROUP BY weight
                    ORDER BY count_weight DESC
                    LIMIT 6
                )
                SELECT
                    height.interval,
                    height.height,
                    height.avg_weight,
                    height.count_height,
                    weight.weight,
                    weight.avg_height,
                    weight.count_weight
                FROM height
                JOIN weight ON height.row_number_height = weight.row_number_weight;
            '''
            df_height_weight = sql_df(query)
            df_height_weight
            ```
            """,
            unsafe_allow_html=True
        )
        query = '''
            WITH height AS (
                SELECT
                    height,
                    (ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) + 1) / 2 as interval,
                    ROUND(AVG(weight), 2) AS avg_weight,
                    COUNT(*) AS count_height,
                    AVG(overall_rating) AS overall_rating_by_height,
                    ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) as row_number_height
                FROM Player_Attributes_Modified
                GROUP BY height
                ORDER BY count_height DESC
                LIMIT 6
            ),
            weight AS (
                SELECT
                    weight,
                    (ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) + 1) / 2 as interval,
                    ROUND(AVG(height), 2) AS avg_height,
                    COUNT(*) AS count_weight,
                    AVG(overall_rating) AS overall_rating_by_weight,
                    ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) as row_number_weight
                FROM Player_Attributes_Modified
                GROUP BY weight
                ORDER BY count_weight DESC
                LIMIT 6
            )
            SELECT
                height.interval,
                height.height,
                height.avg_weight,
                height.count_height,
                height.overall_rating_by_height,
                weight.weight,
                weight.avg_height,
                weight.count_weight,
                weight.overall_rating_by_weight
            FROM height
            JOIN weight ON height.row_number_height = weight.row_number_weight;
        '''
        df_height_weight = sql_df(query)
        st.write("\n")
        st.markdown(
            '<span class="small-font">Resultado da query</span>',
            unsafe_allow_html=True
        )
        st.dataframe(df_height_weight, use_container_width=True)
        fig = make_subplots(rows=1, cols=3, subplot_titles=("Intervalo 1", "Intervalo 2", "Interval0 3"))
        # Filtrar os dados por cada intervalo
        interval1 = df_height_weight[df_height_weight['interval'] == 1]
        interval2 = df_height_weight[df_height_weight['interval'] == 2]
        interval3 = df_height_weight[df_height_weight['interval'] == 3]

        fig.add_trace(go.Bar(
            x=interval1['height'],
            y=interval1['overall_rating_by_height'],
            name='Overall Rating por Height',
            marker_color='#2937fe',
            showlegend=False
        ), row=1, col=1)

        fig.add_trace(go.Bar(
            x=interval1['weight'],
            y=interval1['overall_rating_by_weight'],
            name='Overall Rating por Weight',
            marker_color='#f8d124',
            showlegend=False
        ), row=1, col=1)

        fig.add_trace(go.Bar(
            x=interval2['height'],
            y=interval2['overall_rating_by_height'],
            name='Overall Rating por Height',
            marker_color='#2937fe',
            showlegend=False
        ), row=1, col=2)

        fig.add_trace(go.Bar(
            x=interval2['weight'],
            y=interval2['overall_rating_by_weight'],
            name='Overall Rating por Weight',
            marker_color='#f8d124',
            showlegend=False
        ), row=1, col=2)

        fig.add_trace(go.Bar(
            x=interval3['height'],
            y=interval3['overall_rating_by_height'],
            name='Overall Rating por Height',
            marker_color='#2937fe',
            showlegend=False
        ), row=1, col=3)

        fig.add_trace(go.Bar(
            x=interval3['weight'],
            y=interval3['overall_rating_by_weight'],
            name='Overall Rating por Weight',
            marker_color='#f8d124',
            showlegend=False
        ), row=1, col=3)

        for i in range(1, 4):
            fig.update_xaxes(title_text='Peso/Altura', row=1, col=i)
            fig.update_yaxes(title_text='Média de desempenho', row=1, col=i)

        fig.update_layout(title='Desempenho por Altura e Peso')
        # Segundo gráfico
        fig1 = make_subplots(rows=1, cols=3, subplot_titles=("Grupo 1", "Grupo 2", "Grupo 3"))
        fig1.add_trace(go.Bar(
            x=interval1['height'],
            y=interval1['count_height'],
            name='Quantidade por Height',
            marker_color='#2937fe'
        ), row=1, col=1)

        fig1.add_trace(go.Bar(
            x=interval1['weight'],
            y=interval1['count_weight'],
            name='Quantidade por Weight',
            marker_color='#f8d124'
        ), row=1, col=1)

        fig1.add_trace(go.Bar(
            x=interval2['height'],
            y=interval2['count_height'],
            name='Quantidade por Height',
            marker_color='#2937fe',
            showlegend=False
        ), row=1, col=2)

        fig1.add_trace(go.Bar(
            x=interval2['weight'],
            y=interval2['count_weight'],
            name='Quantidade por Weight',
            marker_color='#f8d124',
            showlegend=False
        ), row=1, col=2)

        fig1.add_trace(go.Bar(
            x=interval3['height'],
            y=interval3['count_height'],
            name='Quantidade por Height',
            marker_color='#2937fe',
            showlegend=False
        ), row=1, col=3)

        fig1.add_trace(go.Bar(
            x=interval3['weight'],
            y=interval3['count_weight'],
            name='Quantidade por Weight',
            marker_color='#f8d124',
            showlegend=False
        ), row=1, col=3)

        for i in range(1, 4):
            fig1.update_xaxes(title_text='Peso/Altura', row=1, col=i)
            fig1.update_yaxes(title_text='Quantidade', row=1, col=i)

        fig1.update_layout(title='Quantidade de Altura e Peso')
        # Plotar os gráficos
        st.plotly_chart(fig1,  use_container_width = True)
        st.plotly_chart(fig,  use_container_width = True)

        '''
        **Notamos que a média de desempenho por peso e altura é bem parecida nos 6 pesos e no grupo 1 uma altura destoa das demais mais encontrados entre os jogadores. A quantidade encontrada em 128.88**
        '''
        st.write("\n")
        query = '''
            SELECT
                team_long_name,
                team_short_name,
                country_name,
                league_name,
                SUM(
                    buildUpPlaySpeed +
                    buildUpPlayPassing +
                    chanceCreationPassing +
                    chanceCreationCrossing +
                    chanceCreationShooting +
                    defencePressure +
                    defenceAggression
                ) AS total_organization_score
            FROM Relations
            GROUP BY 1, 2, 3, 4
            ORDER BY total_organization_score DESC;
        '''
        df_best_teams = sql_df(query)
        st.markdown('Com a tabela Relations criadas podemos de visões como as apresentas resultados da query exemplo.')
        st.markdown('***Trecho do código no notebook.***')
        st.markdown(
            """
            ```python
                query = '''
                    SELECT
                        team_long_name,
                        team_short_name,
                        country_name,
                        league_name,
                        SUM(
                            buildUpPlaySpeed +
                            buildUpPlayPassing +
                            chanceCreationPassing +
                            chanceCreationCrossing +
                            chanceCreationShooting +
                            defencePressure +
                            defenceAggression
                        ) AS total_organization_score
                    FROM Relations
                    GROUP BY 1, 2, 3, 4
                    ORDER BY total_organization_score DESC;
                '''
                df_best_teams = sql_df(query)
                df_best_teams
            ```
            """,
            unsafe_allow_html=True
        )
        df_teams = df_best_teams.sort_values(by='total_organization_score', ascending=True).head(5)
        df_country_scores = df_best_teams.groupby('country_name')['total_organization_score'].sum().reset_index()
        df_country_scores = df_country_scores.sort_values(by='total_organization_score', ascending=True).head(5)

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            y=df_teams['team_long_name'],
            x=df_teams['total_organization_score'],
            name='Top 5 Times',
            orientation='h',
            text=df_teams['total_organization_score'].astype(str) + ', ' + df_teams['country_name'],
            marker=dict(color='#2937fe')
        ))

        fig2.update_layout(
            title='O desempenho dos 5 Melhores Times',
            xaxis_title='Total de desempenho',
            yaxis_title='Time',
            showlegend=False
        )

        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            y=df_country_scores['country_name'],
            x=df_country_scores['total_organization_score'],
            name='Top 5 países',
            orientation='h',
            text=df_country_scores['total_organization_score'],
            marker=dict(color='#f8d124')
        ))

        fig3.update_layout(
            title='O desempenhos dos países com o melhores times',
            xaxis_title='Total de desempenho',
            yaxis_title='País',
            showlegend=False
        )

        st.plotly_chart(fig2,  use_container_width = True)
        st.plotly_chart(fig3,  use_container_width = True)
        '''
        **Notamos que por mais que os 5 melhores times são da Espanha ou Inglaterra, esses países não aparecem no 5 país com score mais alto de todos os times.**
        Sugere muitas investigações futuras, pelo tempo não conseguirei me aprofundar.
        '''

    with tab5:          
        '''
        **Questão 5 - Utiize SQL-CTE**

        - Semanalmente o gerente da Fifa solicita a média de gols dos times mandantes, porém como você gosta de entregar mais do que lhe pedem, você resolveu montar uma CTE para entregar outras métricas para seu gerente.
        - Como você faria, em SQL, para salvar ou automatizar essa query? Envie-nos seu código.
        '''
        st.write("\n")
        '''
        - Criei uma query para automatizar e gerar um dataset semanalmente.
        - Query com média geral de gols, média de gols por time e média de gols por liga nos últimos 7 dias, para o time mandante e visitante e os respectivos times no período.
        - Foram removidos valores em que não temos informações sobre algum **home_team_api_id**
        - Setar uma data para testes da query mas a automatization sera com now() ou getdate() de dependendo do banco, utilizei o date('now') no SQLite.
        '''
        st.markdown('***Trecho do código no notebook para criar e testar a query.***')
        st.markdown(
            """
            ```python
                query = '''
                WITH dates AS (
                    SELECT date('now') AS today, date('now', '-7 days') AS seven_days_ago
                ),
                cte_match_avg AS (
                    SELECT
                        MAX(season) AS season,
                        ROUND(AVG(home_team_goal), 2) AS home_team_goal_avg,
                        ROUND(AVG(away_team_goal), 2) AS away_team_goal_avg
                    FROM Match
                    WHERE date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                        AND (home_team_api_id IS NOT NULL OR away_team_api_id IS NOT NULL)
                ),
                cte_match_by_country_avg AS (
                    SELECT
                        MAX(season) AS season,
                        ROUND(AVG(home_team_goal), 2) AS home_team_goal_avg_by_league,
                        ROUND(AVG(away_team_goal), 2) AS away_team_goal_avg_by_league,
                        league_id
                    FROM Match
                    WHERE date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                        AND (home_team_api_id IS NOT NULL OR away_team_api_id IS NOT NULL)
                    GROUP BY 4
                ),
                cte_home_teams AS (
                    SELECT
                        home_team_api_id,
                        away_team_api_id,
                        (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = home_team_api_id) AS home_team_long_name,
                        (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = away_team_api_id) AS away_team_long_name,
                        league_id,
                        MAX(season) AS season,
                        ROUND(AVG(home_team_goal), 2) AS home_team_goal_avg
                    FROM Match
                    WHERE Match.date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                        AND (
                            (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = home_team_api_id) IS NOT NULL
                        )
                    GROUP BY 1, 2, 3, 4
                ),
                cte_away_teams AS (
                    SELECT
                        home_team_api_id,
                        away_team_api_id,
                        (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = home_team_api_id) AS home_team_long_name,
                        (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = away_team_api_id) AS away_team_long_name,
                        league_id,
                        MAX(season) AS season,
                        ROUND(AVG(away_team_goal), 2) AS away_team_goal_avg
                    FROM Match
                    WHERE Match.date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                        AND (
                            (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = away_team_api_id) IS NOT NULL
                        )
                    GROUP BY 1, 2, 3, 4
                )
                SELECT
                    cte_home_teams.home_team_long_name AS home_team_long_name,
                    cte_home_teams.home_team_goal_avg AS home_team_goal_avg,
                    cte_match_by_country_avg.home_team_goal_avg_by_league,
                    (SELECT home_team_goal_avg FROM cte_match_avg) AS home_total_avg,
                    cte_home_teams.away_team_long_name AS away_team_long_name,
                    cte_away_teams.away_team_goal_avg,
                    cte_match_by_country_avg.away_team_goal_avg_by_league,
                    (SELECT away_team_goal_avg FROM cte_match_avg) AS away_total_avg
                FROM cte_home_teams
                LEFT JOIN cte_match_by_country_avg ON cte_match_by_country_avg.league_id = cte_home_teams.league_id
                LEFT JOIN cte_away_teams ON cte_away_teams.home_team_api_id =  cte_home_teams.home_team_api_id
                    AND cte_away_teams.away_team_api_id = cte_home_teams.away_team_api_id
                WHERE cte_away_teams.away_team_long_name IS NOT NULL
            '''
            df_avg_weekly = sql_df(query)
            df_avg_weekly
            ```
            """,
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown(
            '<span class="small-font">Para testar a query utilizei a data fixada 2008-08-17.</span>',
            unsafe_allow_html=True
        )
        query = '''
            WITH dates AS (
                SELECT date('2008-08-17') AS today, date('2008-08-17', '-7 days') AS seven_days_ago
            ),
            cte_match_avg AS (
                SELECT
                    MAX(season) AS season,
                    ROUND(AVG(home_team_goal), 2) AS home_team_goal_avg,
                    ROUND(AVG(away_team_goal), 2) AS away_team_goal_avg
                FROM Match
                WHERE date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                    AND (home_team_api_id IS NOT NULL OR away_team_api_id IS NOT NULL)
            ),
            cte_match_by_country_avg AS (
                SELECT
                    MAX(season) AS season,
                    ROUND(AVG(home_team_goal), 2) AS home_team_goal_avg_by_league,
                    ROUND(AVG(away_team_goal), 2) AS away_team_goal_avg_by_league,
                    league_id
                FROM Match
                WHERE date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                    AND (home_team_api_id IS NOT NULL OR away_team_api_id IS NOT NULL)
                GROUP BY 4
            ),
            cte_home_teams AS (
                SELECT
                    home_team_api_id,
                    away_team_api_id,
                    (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = home_team_api_id) AS home_team_long_name,
                    (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = away_team_api_id) AS away_team_long_name,
                    league_id,
                    MAX(season) AS season,
                    ROUND(AVG(home_team_goal), 2) AS home_team_goal_avg
                FROM Match
                WHERE Match.date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                    AND (
                        (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = home_team_api_id) IS NOT NULL
                    )
                GROUP BY 1, 2, 3, 4
            ),
            cte_away_teams AS (
                SELECT
                    home_team_api_id,
                    away_team_api_id,
                    (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = home_team_api_id) AS home_team_long_name,
                    (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = away_team_api_id) AS away_team_long_name,
                    league_id,
                    MAX(season) AS season,
                    ROUND(AVG(away_team_goal), 2) AS away_team_goal_avg
                FROM Match
                WHERE Match.date BETWEEN (SELECT seven_days_ago FROM dates) AND (SELECT today FROM dates)
                    AND (
                        (SELECT team_long_name FROM Relations WHERE Relations.team_api_id = away_team_api_id) IS NOT NULL
                    )
                GROUP BY 1, 2, 3, 4
            )
            SELECT
                cte_home_teams.home_team_long_name AS home_team_long_name,
                cte_home_teams.home_team_goal_avg AS home_team_goal_avg,
                cte_match_by_country_avg.home_team_goal_avg_by_league,
                (SELECT home_team_goal_avg FROM cte_match_avg) AS home_total_avg,
                cte_home_teams.away_team_long_name AS away_team_long_name,
                cte_away_teams.away_team_goal_avg,
                cte_match_by_country_avg.away_team_goal_avg_by_league,
                (SELECT away_team_goal_avg FROM cte_match_avg) AS away_total_avg
            FROM cte_home_teams
            LEFT JOIN cte_match_by_country_avg ON cte_match_by_country_avg.league_id = cte_home_teams.league_id
            LEFT JOIN cte_away_teams ON cte_away_teams.home_team_api_id =  cte_home_teams.home_team_api_id
                AND cte_away_teams.away_team_api_id = cte_home_teams.away_team_api_id
            WHERE cte_away_teams.away_team_long_name IS NOT NULL
        '''
        df_avg_weekly = sql_df(query)
        st.write("\n")
        st.markdown(
            '<span class="small-font">Resultado da query</span>',
            unsafe_allow_html=True
        )
        st.dataframe(df_avg_weekly, use_container_width=True)
        '''
        - Para agendar eu usaria o Azure Data Factory.
        - Criaria um pipeline conectando as bases ou api's externas, neste exemplo específico seria conectado a apenas uma única base.
        - Optaria por um **Copy date** para rodar essa query, se necessário mais trabalho nos dados poderia rodar um script.
        - Adicionaria uma trigger com um horário fixo para rodar semanalmente.
            - Sempre optei por horários de madrugada para não interferir no horário de uso dos possíveis relatórios que usem esse dataset
        - E adicionaria um retry caso algum problema, como conexão com base por exemplo.
        - *Link da documentação que utilizava nos trabalhos com DataFactory
        '''
        st.markdown(
            '<span class="small-font">*https://learn.microsoft.com/pt-br/azure/data-factory/',
            unsafe_allow_html=True
        )
        st.write("\n")
        st.markdown(
            '<span class="small-font">Um exemplo do último agendamento que fiz ja que a stack da empresa para criar agendadores nas VMs na Azure era em C#.',
            unsafe_allow_html=True
        )
        st.markdown(
            '<span class="small-font">Usava Python no time de DataScience mas agendadores somente em C#, com a expressão **cron**',
            unsafe_allow_html=True
        )
        st.markdown(
            """
            ```csharp
                [FunctionName("HttpTrigger")]
                public static async Task<IActionResult> Run(
                    [HttpTrigger(AuthorizationLevel.Function, "get", "post", Route = null)]
                    HttpRequest req, ILogger log,
                    [TimerTrigger("0 30 3 * * 1")] TimerInfo myTimer) // Executar função segundas à (3:30)
                try
                {
                    // Adicionar código para executar query, e logs

                    // Retorno
                    return new OkResult();
                }
                catch (Exception ex)
                {
                    // Retorno de algum erro com armazenar em log, conexão com banco ou na query.
                    return new StatusCodeResult();
                }
            ```
            """,
            unsafe_allow_html=True
        )
        '''
        **Link da documentação que utilizava nos trabalhos
        '''
        st.markdown(
            '<span class="small-font">**https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=python-v2%2Cin-process&pivots=programming-language-csharp',
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()