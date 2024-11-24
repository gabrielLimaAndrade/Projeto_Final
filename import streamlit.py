import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projeto Final")

with st.container():
    st.subheader("Projeto Final")
    st.title("Preços e Produtos")
    st.write("Informações sobre produtos e seus preços")
    


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("MagazineTratada.csv")
    return tabela

