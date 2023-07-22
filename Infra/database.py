# %%
import os
from sqlalchemy import create_engine

# def create_connection(db_name):
#     """
#     Cria uma conexão com um banco de dados SQLite.

#     Args:
#         nome_banco (str): O nome do banco de dados.

#     Returns:
#         engine: Objeto de conexão com o banco de dados.
#     """
# %%
class DatabaseConnection:
    def __init__(self, nome_banco):
        assert nome_banco, "O nome do banco não pode ser vazio ou nulo."
        self.nome_banco = nome_banco

        # Verifica se a pasta 'Data' existe, caso contrário, a cria
        if not os.path.exists('Data'):
            os.makedirs('Data')

        self.engine = create_engine(f'sqlite:///Data/{self.nome_banco}.db', echo=False)

    def get_engine(self):
        """
        Retorna o objeto de conexão com o banco de dados.

        Returns:
            engine: Objeto de conexão com o banco de dados.
        """
        return self.engine