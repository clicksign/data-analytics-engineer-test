# Configurando o WSL2 (para usuarios Windows)
- Baixe e instale o VSCode: https://code.visualstudio.com/download.
- Abra o PowerShell como administrador e execute o comando: `wsl --install`
- Configure um usuário e senha para o WSL2.
- Reinicie o computador.
- Na barra de pesquisa do Windows, digite "Ubuntu" e abra-o.
- Rode o seguinte comando para abrir o VSCode no Ubuntu: `code .`
- Instale a extensão WSL no VSCode, feche e rode novamente o comando acima no terminal do Ubuntu.

# Configuração do ambiente em WSL2 ou Linux:
- Clone o repositório, rodando o seguinte comando no terminal do VSCode: `git clone https://github.com/clicksign/data-analytics-engineer-test.git`
- Mude para a branch `Gustavo Oliveira`.
- Instale a extensão dbt Power User no VSCode, que é bastante útil para desenvolver com dbt.
- Na raiz do projeto, execute o seguinte comando no terminal do vscode para configurar o asdf: `cd config-scripts && chmod +x setup-linux-wsl2__adsf.sh && ./setup-linux-wsl2__adsf.sh && cd ..`
- Abra um novo terminal e rode o seguinte comando para terminar a configuração do asdf: `source ~/.bashrc`
- Agora rode o seguinte comando para configurar o python:`cd config-scripts && chmod +x setup-linux-wsl2__python.sh && ./setup-linux-wsl2__python.sh && cd ..`

# Rodando o projeto:
## Extração e carregamento dos dados:
- Na raiz do projeto, abra um novo terminal e execute: `poetry run python python_scripts/unzip.py`
- Em seguida, execute: `poetry run python python_scripts/extract_and_load.py`
- EXTRA: O teste unitário do script `extract_and_load.py` pode ser executado com o comando: `poetry run pytest tests/test_extract_and_load.py`

Dessa forma, os dados serão extraídos do arquivo zip e carregados no banco de dados SQLite com arquivo `test_analytics_engineer.sqlite` na raiz do projeto.

## Configuração do dbt:
- Na raiz do projeto no terminal, execute: `poetry run dbt build`

O comando acima irá criar as tabelas de staging, intermediate e mart no banco de dados SQLite, rodando os testes para cada modelo.

# Estrutura do Projeto

```
data-analytics-engineer-test/
├── analysis/
├── config-scripts/
├── data/
├── macros/
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
├── seeds/
├── python_scripts/
├── snapshots/
├── tests/
├── .gitignore
├── README.md
├── packages.yml
├── poetry.lock
├── profiles.yml
├── pyproject.toml
├── test_analytics_engineer.sqlite
└── dbt_project.yml
```

## Arquivos de Configuração

- `.gitignore`: Especifica os arquivos e pastas que devem ser ignorados pelo Git.
- `README.md`: Contém informações sobre o projeto, incluindo como configurar e executar o projeto.
- `packages.yml`: Especifica as dependências do projeto dbt.
- `profiles.yml`: Especifica as configurações de conexão com o banco de dados para o dbt.
- `pyproject.toml`: Especifica as dependências do projeto Python.
- `dbt_project.yml`: É o arquivo de configuração do projeto dbt, onde você pode definir configurações globais para seu projeto.

## Gerenciamento de Dados

- `data/`: Contém o arquivo zip do case, é a antiga Data.
- `seeds/`: Contém arquivos CSV que podem ser carregados como seeds no dbt.
- `snapshots/`: Contém snapshots, que são usados para capturar o estado de uma tabela em um determinado momento.

## Modelagem de Dados

- `analysis/`: Contém arquivos SQL que podem ser usados para análises ad-hoc ou para testar novas ideias.
- `macros/`: Contém macros personalizadas que podem ser usadas em seus modelos.
- `models/`: Contém seus modelos do dbt, organizados em subpastas de acordo com a camada de modelagem. Por exemplo, a subpasta `staging/` pode conter modelos de staging, a subpasta `intermediate/` pode conter modelos intermediários, e a subpasta `marts/` pode conter marts.

## Scripts

- `config-scripts/`: Contém scripts de configuração que podem ser usados para configurar o ambiente de desenvolvimento ou produção.
- `python_scripts/`: Contém scripts Python que podem ser usados para realizar tarefas de pré-processamento ou pós-processamento de dados.

## Testes

- `tests/`: Contém testes personalizados que podem ser usados para validar seus modelos.

## Banco de Dados

- `test_analytics_engineer.sqlite`: É um arquivo de banco de dados SQLite usado para o projeto.
