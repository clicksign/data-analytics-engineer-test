# **Desafio - Analytics Engineer**

Neste branch está minha ideia de resolução para os desafios propostos, dispostos em um esquema de pastas.

**Pastas**

- Pasta Raiz
  - Infra
    - database
    - database_utils
  - Data
    - .csv
    - test_analytics_engineer.db
  - Country
  - League
  - Match
  - Match_Modified
  - Player
  - Player_Attributes
  - Player_Attributes_Modified
  - Relations
  - Team_attributes
  - Team_attributes_Modified

---
- Infra com os scripts de conexão com banco para cria as tabelas e realizar as queries.

- Data com os arquivos .csv, o arquivo do SQLite e os .pdf gerados da pagina, gerada com streamlit.
  - Subi apenas a pasta .rar por causa do tamanho aceito no github

- Cada pasta esta com o script de criação das tabelas.

- Tem um arquivo uptyter Notebook Analysis.ipynb que pelo qual pode-se acompanhar todos os passos das análises.
---


## Run no projeto

**Recomento**

Instalar as dependência

> pip install -r requirements.txt

Criar as tabelas

> Python main.py

👍 👍

**Recomento fortemente pois além de poder acompanhar o trabalho passo a passo pelo Juptyter Notebook Analysis.ipynb o Streamlit ira rodar a pagina com os resultados oferecendo uma experiencia muito mais rica.**

> streamlit run test_analytics_engineer.py

Obs: Para o Streamlit carregar todas os gráficos interativos é preciso rodar os comandos anteriores para gerar os arquivos e o SQLite, não vou subir ele pois pode dar algum erro ao fazer a leitura local.

👍 👍


### **Bibliotecas**

Utilizei as
- pandas
- plotly.express
- plotly.graph_objects
- plotly.subplots
  - make_subplots
- from sqlalchemy
  - inspect, 
  - Table,
  - Column, 
  - Integer,
  - String,
  - Float,
  - Data,
  - MetaData
- sqlalchemy.orm
  - Session
- streamlit
- json
- os

Bom proveito com os resultados. 😀

Obs: Tive um problema em executar o Python main.py pois ao criar as tabelas com os arquivo maiores tive timeout. Mas ao excluir o arquivo do SQLite e rondar novamente não tive problemas. 👍

Informo que devido ao período de 3 dias para concluir a questão bonus não fiz demandaria mais tempo para entender sobre a ferramenta e a sintaxe do DBT, ja que não tenho familiaridade. 😞