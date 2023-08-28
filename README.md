# Configurando o WSL2 (para usuários Windows)
- Baixe e instale o VSCode: https://code.visualstudio.com/download.
- Abra o PowerShell como administrador e execute o comando: `wsl --install`
- Reinicie o computador.
- Se o Ubuntu não inicializar automaticamente, va na barra de pesquisa do Windows, busque por Ubuntu e abra-o.
- Configure um usuário e senha - e lembre bem dessa senha que ela poderá ser pedida para alguns comandos.
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
- Na raiz do projeto, abra um novo terminal e execute: `poetry run python python_scripts/unzip.py` para extrair os arquivos `.csv` de `data/Data.rar` para a pasta `data/extracted_files/Data`.
- Em seguida, execute: `poetry run python python_scripts/extract_and_load.py`.
- EXTRA: O teste unitário do script `extract_and_load.py` pode ser executado com o comando: `poetry run python_scripts/test_extract_and_load.py`.

Dessa forma, os dados serão extraídos do arquivo `.rar` e carregados no banco de dados SQLite com arquivo `test_analytics_engineer.sqlite` na raiz do projeto. O script é flexível o bastante para que você possa adicionar novos arquivos `.csv` na pasta `data/extracted_files/Data` e eles serão carregados no banco de dados com tabelas de mesmo nome.

Obs: Os arquivos `.csv` poderiam ser diretamente importados para o banco ao colocar na pasta seeds, mas preferi fazer dessa forma para simular um processo de ELT.

## Configuração do dbt:
- Na raiz do projeto no terminal, execute: `poetry run dbt build`

O comando acima irá executar os modelos do dbt e criar as tabelas de staging, intermediate e mart no banco de dados SQLite, rodando os testes para cada modelo.

## Documentação do dbt:
- Na raiz do projeto no terminal, execute: `poetry run dbt docs generate` para gerar a documentação do dbt.
- Em seguida, execute: `poetry run dbt docs serve --port 9090` para visualizar a documentação do dbt no link http://localhost:9090/ no navegador.

# Estrutura do Projeto

```
data-analytics-engineer-test/
├── analyses/
│   └──repeated_team_names/
├── config-scripts/
├── data/
├── macros/
├── models/
│   ├── staging/
│   ├── intermediate/
│   ├── marts/
|   └── sources.yml
├── seeds/
├── python_scripts/
├── snapshots/
├── tests/
├── .gitignore
├── .pre-commit-config.yaml
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
- `pyproject.toml`: Especifica as dependências do projeto Python.
- `.pre-commit-config.yaml`: É o arquivo de configuração do pre-commit, onde você pode definir hooks para serem executados antes de cada commit.
### Configuração do dbt
- `dbt_project.yml`: É o arquivo de configuração do projeto dbt, onde você pode definir configurações globais para seu projeto.
- `packages.yml`: Especifica as dependências do projeto dbt.
- `profiles.yml`: Especifica as configurações de conexão com o banco de dados para o dbt.
- `sources.yml`: É o arquivo de configuração do dbt, onde você pode definir as fontes de dados do seu projeto.

## Gerenciamento de Dados

- `data/`: Contém o arquivo zip do case, é a antiga Data.
- `seeds/`: Contém arquivos CSV que podem ser carregados como seeds no dbt.
- `snapshots/`: Contém snapshots, que são usados para capturar o estado de uma tabela em um determinado momento.

## Modelagem de Dados

- `analyses/`: Contém arquivos SQL que podem ser usados para análises ad-hoc ou para testar novas ideias. Uma dessas análises está na pasta `repeated_team_names/`, que contém arquivos SQL com o objetivo de entender o motivo de terem nomes de times duplicados na tabela de Teams.
- `macros/`: Contém macros personalizadas que podem ser usadas em seus modelos.
- `models/`: Contém seus modelos do dbt, organizados em subpastas de acordo com a camada de modelagem. Por exemplo, a subpasta `staging/` pode conter modelos de staging, a subpasta `intermediate/` pode conter modelos intermediários, e a subpasta `marts/` pode conter marts.

## Scripts

- `config-scripts/`: Contém scripts de configuração que podem ser usados para configurar o ambiente de desenvolvimento ou produção.
- `python_scripts/`: Contém scripts Python que podem ser usados para realizar tarefas de pré-processamento ou pós-processamento de dados.

## Testes

- `tests/`: Contém testes personalizados que podem ser usados para validar seus modelos.

## Banco de Dados

- `test_analytics_engineer.sqlite`: É um arquivo de banco de dados SQLite usado para o projeto.

# Questões do teste

O case foi inteiramente desenvolvido usando sheel, python e dbt. Foquei em usar nomenclaturas condizentes com as boas práticas do dbt e desenvolver os códigos com boas práticas de engenharia de software.
A seguir, respondo as questões do teste:

## 1. Utilize Python para extrair e enviar os dados para um banco SQLite com nome das tabelas iguais aos nomes dos arquivos

Foi feito com os scripts `python_scripts/unzip.py` e `python_scripts/extract_and_load.py`. Como optei por um ELT, deixei a tipagem e os tratamentos de dados para o dbt nos modelos de staging.

## 2. Utilize SQL para criar tabelas modified

A conversão de JSON para tabela foi feito direto nos modelos de staging `stg_player_attributes` e `stg_team_attributes`. Já a união das tabelas foi feita como intermediate model `int_player_attributes_modified` e `int_team_attributes_modified`. A criação da tabela com JSON foi feita no modelo `int_match_modified`.

## 3. Validar qualidade de dados e buscar "sujeiras"

Esse processo foi inteiramente feito com o auxílio do dbt. Criei diversos testes no dbt de não nulos, distintos e testes de chaves estrangeiras para todos modelos de staging. Adicionei descrição nas colunas e tabelas para facilitar a compreensão do que cada coluna e tabela representa. Com esses testes, o dbt me retorna um SQL do que está com problema e eu posso corrigir os dados. Fiz também algumas análises exploratorias respondendo as perguntas de exemplo e explorei a não unicidade de nomes de times e `team_fifa_api_id` chegando à conclusão de que há alguns países com dois times nacionais não oficiais pela FIFA, isso é evidente devido a existência de jogos entre eles, e com o mesmo nome. Mas tendo que escolher somente um quando as partidas são pela FIFA.

## 4. Tabela Relations

Como não identifiquei outliers nos dados de pesos e alturas, decidi ter uma abordagem mais geral para o problema. Encontrei o intervalo entre os pesos/alturas máximos e mínimos e dividi em 3 partes esse intervalo. Caso o peso/altura esteja na primeira parte, ele é considerado leve/baixo, caso esteja na segunda parte, ele é considerado médio e caso esteja na terceira parte, ele é considerado pesado/alto. A tabela foi criada com um modelo mart `relations`.

## 5. Solicitação do gerente da FIFA

Respondendo ao pedido do gerente da FIFA, desenvolvi um modelo mart incremental no dbt para disponibilizar os dados solicitados, ampliando a análise com métricas adicionais. Para facilitar a fusão de dados, utilizei a data truncada para a semana e o ID do time como chaves de junção. Introduzi a tag `weekly` para permitir a execução automatizada desse modelo em intervalos semanais. O modelo específico que contempla essas transformações é o `home_team_performance_weekly`.

Com o intuito de automatizar o processo, sugiro a implementação do Airflow, uma plataforma que possibilita agendar e gerenciar fluxos de trabalho de maneira eficiente e escolher a tag `weekly` como gatilho para a execução do modelo.

Inicialmente, busquei incluir informações adicionais sobre as partidas, mas infelizmente, muitas colunas relevantes possuíam formatação inadequada. Para corrigir essa questão, seria necessário reestruturar a coleta de dados por meio de web scraping. Diante dessa limitação, optei por focar nas colunas `home_team_api_id`, `away_team_api_id`, `home_team_goal` e `away_team_goal`, que estavam disponíveis e prontas para uso.

No entanto, aprimorei a análise incorporando as seguintes métricas às estatísticas das equipes:

- **Total de Gols Semanais**: Soma dos gols marcados em casa e fora em cada semana.
- **Total de Partidas Semanais**: Contagem do número total de partidas disputadas por cada equipe em cada semana.
- **Diferença de Gols Semanais**: Diferença entre gols marcados e gols sofridos por cada equipe em cada semana.
- **Média de Gols Semanais**: Média de gols marcados por partida para cada equipe em cada semana.
- **Número de Vitórias Semanais**: Contagem de vezes que cada equipe venceu em uma semana.
- **Número de Empates Semanais**: Contagem de vezes que cada equipe empatou em uma semana.
- **Número de Derrotas Semanais**: Contagem de vezes que cada equipe perdeu em uma semana.
- **Taxa de Vitórias Semanais**: Proporção de vitórias em relação ao total de partidas jogadas em cada semana.

Essas métricas adicionais proporcionam uma visão mais abrangente do desempenho das equipes ao longo das semanas, permitindo análises mais detalhadas e insights valiosos para a gestão de equipes no cenário esportivo.

## 6. Criação de um projeto no dbt

Foi feito durante o desenvolvimento do projeto.

# Melhorias

- Implementar o Airflow para fazer a orquestração do processo de extração e carregamento.
- Desenvolver todos os modelos de staging de forma incremental, para que não seja necessário carregar todos os dados novamente.
- Desenvolver ciência de dados para responder as perguntas do case, fazer análises, clusterizações de jogadores similares e fazer previsões.
- Refazer o processo de web scraping para extrair dados de forma que não tenhamos problemas com falta de dados em colunas, ou dados com má formatação ou formato de html.
