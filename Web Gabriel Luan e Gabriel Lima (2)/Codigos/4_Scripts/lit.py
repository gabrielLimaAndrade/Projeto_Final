import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title('Trabalho Web: Celulares Magazine')

requisicao1 = requests.get("http://localhost:5000/dados")
requisicao2 = requests.get("http://127.0.0.1:5000/dados_brutos")
requisicao3 = requests.get("http://127.0.0.1:5000/precos")
requisicao4 = requests.get("http://127.0.0.1:5000/marcas")
requisicao5 = requests.get("http://127.0.0.1:5000/dinheiro")
st.button('Tela inicial',type='primary')
if st.button("Media, Mediana e Desvio Padrão"):
   resposta = requisicao3.json()
   resposta = pd.DataFrame(resposta)
   st.write(resposta.columns)
   media = resposta['Preco'].mean()
   mediana = resposta['Preco'].median()
   dp = resposta['Preco'].std()
   st.write(resposta)
   estatisticas = pd.DataFrame({'estatistica':['Media','Mediana','Desvio Padrão'],'valor':[media,mediana,dp]})
   fig = px.bar(estatisticas, x='estatistica',y = 'valor', title = 'Media, Mediana, Desvio Padrão',labels = {
    'valor':'Valores','estatistica':'Metricas'},text='valor')

   fig.update_traces(texttemplate='%{text:.2f}',textposition ='outside')
   
   st.plotly_chart(fig)

elif st.button("Quantidades de aparelhos por marca"):
   r = requisicao4.json()
   df = pd.DataFrame(list(r.items()), columns =['Marca','Quantidade'])
   st.write(df.columns)
   st.write(df)
   fig2 = px.pie(df,names='Marca', values='Quantidade', title='Quantidade de aparelhos por marca')
   st.plotly_chart(fig2)

elif st.button('Valores'):
   v = requisicao5.json()
   v2 = pd.DataFrame(list(v.items()), columns=['Custo','Quantidade'])
   st.write(v2.columns)
   st.write(v2)
   fig3 = px.bar(v2, x='Custo',y = 'Quantidade', title = 'quantidade de celulares por preco')

 
   st.plotly_chart(fig3)
