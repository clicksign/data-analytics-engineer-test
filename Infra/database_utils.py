# %%
import pandas as pd
from sqlalchemy import text

# %%
def sql(query, engine):
    assert query, "A query não pode ser vazia ou nula."
    with engine.connect() as conexao:
        consulta = conexao.execute(text(query))
        dados = consulta.fetchall()
    return pd.DataFrame(dados, columns=consulta.keys())

# %%