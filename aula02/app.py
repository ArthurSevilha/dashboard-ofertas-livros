"""Dashboard de Livros: app Streamlit."""

import streamlit as st
import dados


def montar_tabela(livros):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": livro["nota"] * "⭐",
            "Preço": f"£ {livro['preco']:.2f}",
            "Faixa": classificar_preco(livro["preco"]),
        }
        tabela.append(linha)
    return tabela


def classificar_preco(preco):
    """Classifica um preço em libras em uma faixa de texto."""
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"


def contar_por_faixa(livros):
    """Conta quantos livros existem em cada faixa de preço: {"Caro": 403, ...}"""
    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        if faixa in contagem:
            contagem[faixa] = contagem[faixa] + 1
        else:
            contagem[faixa] = 1

    return contagem


def listar_categorias(livros):
    """Extrai todas as categorias únicas da lista de livros."""
    categorias = []
    for livro in livros:
        if livro["categoria"] not in categorias:
            categorias.append(livro["categoria"])

    categorias.sort()
    return categorias


def filtrar_por_categoria(livros, categoria):
    """Filtra a lista de livros pela categoria selecionada."""
    if categoria == "Todas":
        return livros

    resultado = []
    for livro in livros:
        if livro["categoria"] == categoria:
            resultado.append(livro)

    return resultado


def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    livros = dados.carregar_livros()

    # Métricas Globais
    col1, col2, col3, col4 = st.columns(4)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    if mais_caro:
        col4.metric("Livro mais caro", f"£{mais_caro['preco']:.2f}")
        col4.caption(mais_caro["titulo"])

    st.markdown("---")

    # Colunas de busca e filtro
    col_busca, col_categoria = st.columns(2)

    busca = col_busca.text_input("Buscar por título:", placeholder="Digite o nome do livro...")
    categoria = col_categoria.selectbox("Filtrar por Categoria", ["Todas"] + listar_categorias(livros))

    # Aplicação dos Filtros
    livros_filtrados = filtrar_por_categoria(livros, categoria)
    livros_filtrados = dados.buscar_por_titulo(livros_filtrados, busca)

    # Exibição do Resultado
    if len(livros_filtrados) > 0:
        st.write(f"**Livros encontrados:** {len(livros_filtrados)}")
        tabela = montar_tabela(livros_filtrados)
        st.dataframe(tabela, use_container_width=True)
    else:
        st.warning("Nenhum livro encontrado.")


if __name__ == "__main__":
    main()