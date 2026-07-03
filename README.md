# NBA Analytics Dashboard

Análise das estatísticas da NBA entre as temporadas de 2000-01 e 2023-24 utilizando Python, Machine Learning e Power BI.

O projeto tem como objetivo identificar quais estatísticas possuem maior relação com o número de vitórias das equipes e construir um dashboard interativo para exploração dos dados.


#  Dashboard

## Página 1  Visão Geral

Apresenta a evolução das principais estatísticas da NBA ao longo das temporadas.

Indicadores:

- Total de temporadas analisadas
- Número de franquias
- Média de pontos por jogo
- Média de vitórias

apresenta a evolução de:

- Pontos por jogo
- Assistências por jogo
- Rebotes por jogo


## Página 2 - O que explica as vitórias?

Análise das estatísticas mais relacionadas ao sucesso das equipes.

- FG% × Vitórias
- 3P% × Vitórias
- Assistências × Vitórias
- Rebotes × Vitórias

Principais descobertas:

- O aproveitamento nos arremessos (FG%) apresentou maior relação com vitórias do que o volume de arremessos
- Assistências mostraram maior associação com vitórias do que rebotes.
- Turnovers apresentaram correlação negativa com o número de vitórias.
- A eficiência ofensiva foi um dos principais fatores associados ao sucesso das equipes.


#  Machine Learning

Foram comparados três algoritmos para prever o número de vitórias das equipes.

-Modelo - MAE - R² 

- Regressão Linear - 6.46 - 0.528 
- Random Forest - 6.29 - 0.550 
- XGBoost - 6.30 - 0.561 

O modelo XGBoost apresentou o melhor desempenho, embora a diferença em relação aos demais modelos tenha sido pequena.


#  Principais Resultados

Correlação das estatísticas com o número de vitórias:

- Estatística  Correlação 
- Field Goal %  0.533 
- Three Point %  0.496 
- Assistências  0.359 
- Pontos por jogo  0.339 
- Rebotes  0.310 
- Turnovers  -0.194 

#  Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Power BI

#  Estrutura do Projeto

```
NBA-Analytics

── data

nba_team_stats_00_to_23.csv
nba_analytics_final.csv
prediçoes.csv
── scripts

nba.py
modelo_vitorias.py

── dashboard
   NBA dados.pbix

── images

Correlação entre bolas de 3 e vitoria.png
Estatisticas que mais explicam vitoria nba.png
Importancia de variaveis.png
Media Cestas de 3.png
Media Rebotes e assistencias.png
Rebotes e assistencia correlaçao por vitoria.png

── requirements.txt

── README.md

#  Dataset

NBA Team Statistics (2000–2024)

Fonte: Kaggle

#  Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/nba-analytics-dashboard.git

Instale as dependências:

```bash
pip install -r requirements.txt

Execute os scripts:

```bash
python scripts/nba.py

```bash
python scripts/modelo_vitorias.py

Abra o arquivo:

dashboard/NBA_Analytics.pbix

#  Possíveis Melhorias

- Incluir métricas avançadas (Offensive Rating, Defensive Rating e Pace).
- Adicionar dados de Playoffs.
- Testar novos algoritmos de Machine Learning.
- Desenvolver previsões para temporadas futuras.


#  Autor

Guilherme Melo

Projeto desenvolvido para estudo de Análise de Dados, Machine Learning e Power BI.
