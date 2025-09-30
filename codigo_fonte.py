"""codigo_fonte.ipynb

import pandas as pd
import plotly.express as px
import streamlit as st

#streamlit run Igrafics_Covid19.py

#ler o dataset
df = pd.read_csv("https://raw.githubusercontent.com/wcota/covid19br/refs/heads/master/cases-brazil-states.csv")

#melhorando as colunas
df = df.rename(columns={"newDeaths": "novos óbitos", "newCases": "novos casos", "deaths_per_100k_inhabitants":
                "óbitos por 100 mil habitantes", "totalCases_per_100k_inhabitants": "casos por 100 mil habitantes",})

#Seleção de estado
estados = list(df["state"].unique())
state = st.sidebar.selectbox("Qual estado?", estados)

#Seleção da coluna
colunas = ["novos óbitos", "novos casos", "óbitos por 100 mil habitantes", "casos por 100 mil habitantes"]
column = st.sidebar.selectbox("Qual tipo de informação?", colunas)

#Seleção das linhas que pertencem ao estado
df= df[df["state"] == state]

#Gráfico
fig = px.line(df, x="date", y=column, title=column + " - " + state)
fig.update_layout( xaxis_title="Data", yaxis_title=column.upper(), title={"x":0.5})

st.title("DADOS COVID - BRASIL")
st.write("Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico."
      "Utilize o menu lateral para a navegação")

#mostrar gráfico no streamlit
st.plotly_chart(fig, use_container_width=True)

#Fontes

st.caption("Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br/blob/master/cases-brazil-states.csv")


