import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from xgboost import XGBRegressor

# ==================================================
# Carregar dados
# ==================================================



# Métricas por jogo
df = pd.read_csv(
    "nba_analytics_final.csv",
    sep=";",
    decimal=","
)

print(df.columns.tolist())
# ==================================================
# Features e Target
# ==================================================

features = [
    'field_goal_percentage',
    'three_point_percentage',
    'free_throw_percentage',
    'assists_pg',
    'rebounds_pg',
    'points_pg',
    'turnovers',
    'steals',
    'blocks'
]

X = df[features]
y = df['wins']

# ==================================================
# Separar treino e teste
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==================================================
# REGRESSÃO LINEAR
# ==================================================

linear = LinearRegression()

linear.fit(X_train, y_train)

pred_linear = linear.predict(X_test)

mae_linear = mean_absolute_error(y_test, pred_linear)
r2_linear = r2_score(y_test, pred_linear)

# ==================================================
# RANDOM FOREST
# ==================================================

forest = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

forest.fit(X_train, y_train)

pred_forest = forest.predict(X_test)

mae_rf = mean_absolute_error(y_test, pred_forest)
r2_rf = r2_score(y_test, pred_forest)

# ==================================================
# XGBOOST
# ==================================================

xgb = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)

xgb.fit(X_train, y_train)

pred_xgb = xgb.predict(X_test)

mae_xgb = mean_absolute_error(y_test, pred_xgb)
r2_xgb = r2_score(y_test, pred_xgb)

# ==================================================
# Comparação dos modelos
# ==================================================

comparacao = pd.DataFrame({
    "Modelo": [
        "Regressão Linear",
        "Random Forest",
        "XGBoost"
    ],
    "MAE": [
        mae_linear,
        mae_rf,
        mae_xgb
    ],
    "R²": [
        r2_linear,
        r2_rf,
        r2_xgb
    ]
})

print("\n========== COMPARAÇÃO ==========\n")
print(comparacao)

# ==================================================
# Coeficientes - Regressão Linear
# ==================================================

coef_df = pd.DataFrame({
    "Variável": X.columns,
    "Coeficiente": linear.coef_
})

coef_df = coef_df.sort_values(
    by="Coeficiente",
    ascending=False
)

print("\nCoeficientes da Regressão Linear\n")
print(coef_df)

# ==================================================
# Importância - Random Forest
# ==================================================

importance_rf = pd.DataFrame({
    "Variável": X.columns,
    "Importância": forest.feature_importances_
})

importance_rf = importance_rf.sort_values(
    by="Importância",
    ascending=False
)

print("\nImportância - Random Forest\n")
print(importance_rf)

# ==================================================
# Importância - XGBoost
# ==================================================

importance_xgb = pd.DataFrame({
    "Variável": X.columns,
    "Importância": xgb.feature_importances_
})

importance_xgb = importance_xgb.sort_values(
    by="Importância",
    ascending=False
)

print("\nImportância - XGBoost\n")
print(importance_xgb)

# ==================================================
# Gráfico - XGBoost
# ==================================================

plt.figure(figsize=(10,6))

plt.barh(
    importance_xgb["Variável"],
    importance_xgb["Importância"]
)

plt.gca().invert_yaxis()

plt.title("Importância das Variáveis - XGBoost")

plt.tight_layout()
plt.show()

comparacao = pd.DataFrame({
    "Real": y_test,
    "Previsto": pred_xgb
})

comparacao.to_csv(
    "predicoes.csv",
    index=False
)
# =================================================
# Previsão de vitórias para todas as equipes    
# =================================================
df["wins_previstas"] = xgb.predict(X)

print(
    df[
        ["Franchise", "season", "wins", "wins_previstas"]
    ].head()
)

df.to_csv(
    "nba_predicoes.csv",
    index=False,
    sep=";",
    decimal=","
)