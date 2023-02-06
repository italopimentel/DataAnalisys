import pandas as pd
import plotly.express as px

data = pd.read_csv("contratos-2022_03-02-2023_11-37-18.csv")

data.head()

data.shape
data.info()

data['VALOR'].count()

# Soma de todos os valores
data['VALOR'].sum()

# Valor máximo
data['VALOR'].max()

# Valor mínimo
data['VALOR'].min()

# Média dos valores
data['VALOR'].mean()


# Mediana dos valores
data['VALOR'].median()

# Quartil 1
data['VALOR'].quantile(.25)

# Quartil 2
data['VALOR'].quantile(.5)

# Quartil 3
data['VALOR'].quantile(.75)


# ## Análises gráficas
# Boxplot
fig = px.box(data, y="VALOR", title="Boxplot referente aos valores dos contratos")
fig.show()

fig = px.bar(data, x="TIPOCONTRATO", barmode='group', title="Quantidade de Tipos de contrato")
fig.show()

# Criando Dataframe apenas com as razões sociais de GOL NETO EIRELI e CONSTRUTORA INHUMAS LTDA - ME para fins de apresentação de gráficos
df_unico = data[(data['RAZAOSOCIAL'] == 'GOL NETO EIRELI') | (df['RAZAOSOCIAL'] == 'CONSTRUTORA INHUMAS LTDA - ME')]


fig = px.histogram(df_unico, x="VALOR", title='Histograma dos Valores dos contratos')
fig.show()


fig = px.bar(df_unico, x="TIPOCONTRATO", y="VALOR", color="RAZAOSOCIAL", barmode='group', title="Soma de valores dos tipos de contrato")
fig.show()


fig = px.box(df_unico, x="RAZAOSOCIAL", y="VALOR", title="Boxplot referente aos valores dos contratos")
fig.show()





