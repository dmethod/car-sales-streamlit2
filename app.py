import streamlit as st
import pandas as pd
import plotly.express as px

# Lê o CSV
df = pd.read_csv("vehicles.csv")

# Cabeçalho
st.header("📊 Análise Exploratória de Anúncios de Carros")

# Botão para histograma de preços
if st.button("Mostrar histograma de preços"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribuição de Preços dos Carros")
    st.plotly_chart(fig, use_container_width=True)

# Botão para gráfico de dispersão Ano x Preço
if st.button("Mostrar gráfico de dispersão Ano x Preço"):
    fig = px.scatter(
        df,
        x="model_year",
        y="price",
        title="Dispersão: Ano do Modelo vs Preço",
        opacity=0.6,
        labels={"model_year": "Ano do Modelo", "price": "Preço"}
    )
    st.plotly_chart(fig, use_container_width=True)