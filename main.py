from Infra.database import DatabaseConnection
from Country.country_create_table import CountryTable
from League.league_create_table import LeagueTable
from Match.match_create_table import MatchTable
from Player.player_create_table import PlayerTable
from Team.team_create_table import TeamTable
from Player_Attributes.player_attributes_create_table import PlayerAttributesTable
from Team_Attributes.team_attributes_create_table import TeamAttributesTable
from Match_Modified.match_modified_create_table import MatchModifiedTable
from Team_Attributes_Modified.team_attributes_modified_create_table import TeamAttributesModifiedTable
from Player_Attributes_Modified.player_attributes_modified_create_table import PlayerAttributesModifiedTable
from Relations.relations_create_table import RelationsTable

def main():
    db_connection = DatabaseConnection('test_analytics_engineer')
    engine = db_connection.get_engine()

    """
    Função principal que cria a tabela 'Country' no banco de dados.
    """
    country_table = CountryTable(engine)
    country_table.create_table()
    """
    Função principal que cria a tabela 'League' no banco de dados.
    """
    league_table = LeagueTable(engine)
    league_table.create_table()
    """
    Função principal que cria a tabela 'Match' no banco de dados.
    """
    match_table = MatchTable(engine)
    match_table.create_table()
    """
    Função principal que cria a tabela 'Player_Attributes' no banco de dados.
    """
    player_attributes_table = PlayerAttributesTable(engine)
    player_attributes_table.create_table()
    """
    Função principal que cria a tabela 'Player' no banco de dados.
    """
    player_table = PlayerTable(engine)
    player_table.create_table()
    """
    Função principal que cria a tabela 'Team_Attributes' no banco de dados.
    """
    team_attributes_table = TeamAttributesTable(engine)
    team_attributes_table.create_table()
    """
    Função principal que cria a tabela 'Team' no banco de dados.
    """
    team_table = TeamTable(engine)
    team_table.create_table()
    """
    Função principal que cria a tabela 'Match_Modified' no banco de dados.
    """
    match_modified_table = MatchModifiedTable(engine)
    match_modified_table.create_table()
    """
    Função principal que cria a tabela 'Team_Attributes_Modified' no banco de dados.
    """
    team_attributes_modified_table = TeamAttributesModifiedTable(engine)
    team_attributes_modified_table.create_table()
    """
    Função principal que cria a tabela 'Player_Attributes_Modified' no banco de dados.
    """
    player_attributes_modified_table = PlayerAttributesModifiedTable(engine)
    player_attributes_modified_table.create_table()
    """
    Função principal que cria a tabela 'Relations' no banco de dados.
    """
    relations_table = RelationsTable(engine)
    relations_table.create_table()


if __name__ == "__main__":
    main()
