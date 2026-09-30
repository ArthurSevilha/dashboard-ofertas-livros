"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print(f"O arquivo {CAMINHO_CSV.name} não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo:", error)
    
    return livros

def calcular_preco_medio(livros):
    if not livros:
        return 0.0

    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        soma += preco_num

    preco_medio: float = soma / len(livros)
    return preco_medio

def contar_cinco_estrelas(livros):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            contador += 1

    return contador

def obter_livro_mais_caro(livros):
    if not livros:
        return None
    
    livro_mais_caro = max(
        livros,
        key=lambda livro: float(livro["preco"].replace("£", ""))
    )
    return livro_mais_caro
