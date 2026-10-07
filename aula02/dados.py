"""Leitura dos arquivos CSV do projeto."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está.
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros():
    """Lê o CSV de livros e devolve uma lista de dicionários."""
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros


def calcular_preco_medio(livros):
    """Soma os preços de todos os livros e divide pelo total."""
    if not livros:
        return 0.0
    soma: float = 0
    for livro in livros:
        soma += livro["preco"]

    preco_medio: float = soma / len(livros)
    return preco_medio


def contar_cinco_estrelas(livros):
    """Conta quantos livros têm a nota máxima."""
    contador: int = 0
    for livro in livros:
        if livro["nota"] == 5:
            contador += 1

    return contador


def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço."""
    if not livros:
        return None
    mais_caro = livros[0]
    for livro in livros:
        if livro["preco"] > mais_caro["preco"]:
            mais_caro = livro
    return mais_caro


def converter_preco(preco):
    """Converte um preço do site em número: "£51.77" -> 51.77"""
    return float(preco.replace("£", ""))


def converter_nota(nota):
    """Converte a nota escrita em inglês em número: "Three" -> 3"""
    if nota == "Five":
        return 5
    elif nota == "Four":
        return 4
    elif nota == "Three":
        return 3
    elif nota == "Two":
        return 2
    else:
        return 1


def preparar_livros(linhas):
    """Recebe as linhas lidas do CSV e devolve os livros com preço e nota em número."""
    livros = []
    for linha in linhas:
        livro = {
            "titulo": linha["titulo"],
            "preco": converter_preco(linha["preco"]),
            "categoria": linha["categoria"],
            "nota": converter_nota(linha["nota"]),
            "url": linha["url"],
        }
        livros.append(livro)

    return livros


def carregar_livros():
    """Lê o CSV e já devolve os livros prontos para usar."""
    return preparar_livros(ler_livros())


def buscar_por_titulo(livros, buscar):
    """Devolve uma lista nova só com os livros cujo título contém o texto buscado."""
    if not buscar:
        return livros

    resultado = []
    texto_busca = buscar.strip().lower()

    for livro in livros:
        if texto_busca in livro["titulo"].lower():
            resultado.append(livro)

    return resultado


if __name__ == "__main__":
    livros = carregar_livros()
    print(f"{len(livros)} livros carregados")
    if livros:
        print("Primeiro livro:", livros[0])