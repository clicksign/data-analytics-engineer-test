# **Resumo do teste**

Criei esse documento para explicar o passo-a-passo que segui para realizar os exercícios.

# **Passo-a-passo**

Os dados que você precisará para completar este desafio está armazenado na pasta **data** deste repositório. Este diretório contém os seguintes arquivos:

1. Realizei o import dos arquivos .csv via python e pandas, preferi realizar o tratamento se necessário no sql, subindo o dado "cru", como falamos, para o banco.
2. Realizei o tratamento usando replaces de campos que estavam como texto em colunas que deveriam ser tipo númerico ou similar. Sem o replace estava dando erro de extração do JSON e alterações assim são válidas para garantirmos que possamos subir os dados no banco.
3. Realizei algumas análises exploratórias afim de verificar números dentro do data set, por exemplo, quantidade de gols por países e se tinhamos todos os países dentro da tabela Country para realizar essas somas. 
4. A parte do relacionamento com para criar a tabela Relations, tentei realizar o UNPIVOT da Tabela Match mas parece que não é suportada a função no banco, busquei um relacionamento que fizesse sentido para usar as 4 tabelas. Não entendi muito bem o exemplo que me deram, e acredito por isso não o apliquei. Acredito que se tivesse sido em outro tipo de banco conseguiria fazer o UNPIVOT e realizar a relação de forma mais simples.
5. Procurei criar métricas que são usadas em programas de futebol quando falamos de temporadas. Buscando a soma e media de gols dentro e fora de casa.
6. Não consegui realizar como queria a criação do projeto BÔNUS em DBT por conta do prazo e compromissos particulares que acabaram se cruzando, mas compartilho com vocês o link do meu projeto de conclusão do curso que fiz recentemente de Analytics Engineer modelado em DBT, onde será possível visualizar os modelos criados, as statings(tabelas tratadas ou de dev) e os modelos finais.

# **BÔNUS** 
link repositório: https://github.com/niltoncurso01/dbt_projeto_final

Agradeço a oportunidade do teste!
Muito obrigado.

Nilton Xavier
