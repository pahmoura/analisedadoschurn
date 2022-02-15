# A base de dados utilizada é pública

import pandas as pd

# Passo 1: Importar base de dados
tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# Passo 3: Tratamento de dados
# - Valores com formato errado
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: Análise
# Como estão os cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Comparar cada coluna da tabela com a coluna de cancelamento
import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()

# Conclusões:





