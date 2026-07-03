import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Carregar dados
# =========================

df = pd.read_csv("nba_team_stats_00_to_23.csv")
# =========================
# Adicionar coluna de ordem da temporada  
# =========================
df["season_order"] = df["season"].str[:4].astype(int)
# =========================
# Padronizar nomes de times     
# =========================
df["Franchise"] = df["Team"].replace({
    "New Jersey Nets": "Brooklyn Nets",
    "Charlotte Bobcats": "Charlotte Hornets",
    "New Orleans Hornets": "New Orleans Pelicans",
    "New Orleans/Oklahoma City Hornets": "New Orleans Pelicans",
    "Los Angeles Clippers": "LA Clippers",
    "Vancouver Grizzlies": "Memphis Grizzlies",
    "Seattle SuperSonics": "Oklahoma City Thunder"
})
# =========================
# Métricas por jogo
# =========================
df["points_pg"] = df["points"] / df["games_played"]
df['assists_pg'] = df['assists'] / df['games_played']
df['rebounds_pg'] = df['rebounds'] / df['games_played']
df['three_pa_pg'] = (
    df['three_pointers_attempted'] /
    df['games_played']
)

df['three_pm_pg'] = (
    df['three_pointers_made'] /
    df['games_played']
)

# =========================
# Informações gerais
# =========================

print(df.shape)
print(df.columns.tolist())

# =========================
# Correlação com vitórias
# =========================

corr_wins = df.corr(numeric_only=True)['wins']

print("\nCorrelação com vitórias:\n")
print(corr_wins.sort_values(ascending=False))


# =========================
# Evolução por temporada
# =========================

season_avg = df.groupby('season').agg({
    'points_pg':'mean',
    'assists_pg':'mean',
    'rebounds_pg':'mean',
    'three_pa_pg':'mean',
    'three_pm_pg':'mean'
}).reset_index()

# ordenar cronologicamente
season_avg = season_avg.sort_values('season')

# =========================
# Assistências e Rebotes
# =========================

plt.figure(figsize=(12,6))
plt.plot(  
    season_avg['season'],
    season_avg['points_pg'],    
marker='o',
    label='Pontos por jogo' 
)
plt.plot(
    season_avg['season'],
    season_avg['assists_pg'],
    marker='o',
    label='Assistências por jogo'
)

plt.plot(
    season_avg['season'],
    season_avg['rebounds_pg'],
    marker='o',
    label='Rebotes por jogo'
)

plt.xticks(rotation=45)
plt.legend()

plt.title(
    'Evolução de Pontos, Assistências e Rebotes por Jogo'
)

plt.tight_layout()
plt.show()

# =========================
# Evolução dos arremessos de 3
# =========================

plt.figure(figsize=(12,6))

plt.plot(
    season_avg['season'],
    season_avg['three_pa_pg'],
    marker='o',
    label='Tentativas de 3 por jogo'
)

plt.plot(
    season_avg['season'],
    season_avg['three_pm_pg'],
    marker='o',
    label='Cestas de 3 por jogo'
)

plt.xticks(rotation=45)
plt.legend()

plt.title(
    'Evolução dos Arremessos de 3 Pontos por Jogo'
)

plt.tight_layout()
plt.show()
# =========================
# Correlação por temporada 
# =========================
results = []

for season in sorted(df['season'].unique()):

    temp = df[df['season'] == season]

    results.append({
        'season': season,
        'corr_3pa': temp['three_pa_pg'].corr(temp['wins']),
        'corr_3pm': temp['three_pm_pg'].corr(temp['wins'])
    })

three_corr = pd.DataFrame(results)
# =========================
# Correlação com vitórias
# =========================

plt.figure(figsize=(12,6))

plt.plot(
    three_corr['season'],
    three_corr['corr_3pa'],
    marker='o',
    label='Correlação: Tentativas de 3 x Vitórias'
)

plt.plot(
    three_corr['season'],
    three_corr['corr_3pm'],
    marker='o',
    label='Correlação: Cestas de 3 x Vitórias'
)

plt.xticks(rotation=45)
plt.legend()

plt.title(
    'Impacto das Bolas de 3 nas Vitórias ao Longo do Tempo'
)

plt.ylabel('Correlação')

plt.axhline(
    y=0,
    color='black',
    linestyle='--',
    alpha=0.5
)

plt.tight_layout()
plt.show()

# =========================
# Rebotes x Vitórias
# ========================= 
# =========================
# Correlação entre Assistências,
# Rebotes, Pontos por jogo e Vitórias
# =========================

results = []

for season in sorted(df['season'].unique()):

    temp = df[df['season'] == season]

    results.append({
        'season': season,
        'corr_assists': temp['assists_pg'].corr(temp['wins']),
        'corr_rebounds': temp['rebounds_pg'].corr(temp['wins']),
        'corr_points': temp['points_pg'].corr(temp['wins'])
    })

ar_df = pd.DataFrame(results)

print(ar_df)

plt.figure(figsize=(13,6))

plt.plot(
    ar_df['season'],
    ar_df['corr_assists'],
    marker='o',
    linewidth=2,
    label='Assistências x Vitórias'
)

plt.plot(
    ar_df['season'],
    ar_df['corr_rebounds'],
    marker='o',
    linewidth=2,
    label='Rebotes x Vitórias'
)

plt.plot(
    ar_df['season'],
    ar_df['corr_points'],
    marker='o',
    linewidth=2,
    label='Pontos por jogo x Vitórias'
)

plt.axhline(
    y=0,
    color='black',
    linestyle='--',
    alpha=0.5
)

plt.xticks(rotation=45)

plt.ylabel("Correlação")

plt.title(
    "Impacto das Estatísticas nas Vitórias ao Longo das Temporadas"
)

plt.legend()

plt.tight_layout()

plt.show()
# =========================
# Resumo das correlações       
# =========================

summary = pd.DataFrame({
    'Estatistica': [
        'Plus Minus',
        'FG%',
        '3P%',
        'Assistências',
        'Rebotes',
        'Pontos por jogo',
        'Turnovers'
    ],
    'Correlacao': [
        0.953,
        0.533,
        0.496,
        0.359,
        0.310,
        corr_wins['points_pg'],
        -0.194
    ]
})

summary = summary.sort_values(
    'Correlacao',
    ascending=False
)

print(summary)
plt.figure(figsize=(10,6))

sns.barplot(
    data=summary,
    x='Correlacao',
    y='Estatistica'
)

plt.title(
    'Estatísticas Mais Associadas às Vitórias na NBA'
)

plt.show()

df.to_csv(
    "nba_analytics_final.csv",
    index=False,
    decimal=",",
    sep=";"
)

print("Arquivo salvo com sucesso!")
