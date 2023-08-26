# Configuração do ambiente em WSL2 ou Linux:
- Clone o repositório.
- Na raiz do projeto, execute o comando: `cd config-scripts && chmod +x setup-linux-wsl2.sh && ./setup-linux-wsl2.sh && cd ..`

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
