"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")

col1, col2, col3, col4 = st.columns(4)

livros = dados.ler_livros()

qtd_livros = len(livros)
col1.metric("Total de livros", qtd_livros)

preco_medio = dados.calcular_preco_medio(livros)
col2.metric("Preço Médio", f"£{preco_medio:.2f}")

cinco_estrelas = dados.contar_cinco_estrelas(livros)
col3.metric("Qtd de Cinco Estrelas", cinco_estrelas)

livro_mais_caro = dados.obter_livro_mais_caro(livros)

if livro_mais_caro:
    preco_str = livro_mais_caro["preco"]
    titulo_mais_caro = livro_mais_caro["titulo"]
    
    col4.metric("Livro Mais Caro", preco_str)
    col4.caption(f"📖 {titulo_mais_caro}")
else:
    col4.metric("Livro Mais Caro", "N/A")

st.divider()
st.dataframe(livros, use_container_width=True)
