import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Projeto Final", layout="wide")

# Exibição do título e introdução
with st.container():
    st.subheader("Projeto Final")
    st.title("Preços e Produtos")
    st.write("Informações sobre produtos e seus preços")

# Funções ou dados de gráficos importados de lit.py
try:
    from lit import generate_charts  # Certifique-se de que lit.py está no mesmo diretório ou acessível no PYTHONPATH
    
    # Exibir gráficos gerados pelo módulo lit.py
    st.markdown("### Gráficos")
    charts = generate_charts()
    
    # Supondo que `generate_charts` retorna uma lista de gráficos matplotlib ou dados prontos para visualização
    for idx, chart in enumerate(charts, start=1):
        st.pyplot(chart)  # Renderiza gráficos matplotlib
        st.markdown(f"Gráfico {idx}")
        
except ImportError as e:
    st.error("Erro ao importar o arquivo lit.py. Certifique-se de que ele está no diretório correto.")
    st.write(e)

# Suporte para carregar um arquivo CSV, se necessário
uploaded_file = st.file_uploader("Envie um arquivo CSV para análise:", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Prévia dos dados:")
    st.dataframe(df)
