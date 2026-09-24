"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")

col1, col2, col3 = st.columns(3)

livros = dados.ler_livros()

qtd_livros = len(livros)
col1.metric("Total de livros", qtd_livros)

preco_medio = dados.calcular_preco_medio(livros)
col2.metric("total média", f"£{preco_medio:.2f}")

cinco_estrelas = dados.contar_cinco_estrelas(livros)
col3.metric("Qtd de Cinco Estrelas", cinco_estrelas)

st.dataframe(livros)
