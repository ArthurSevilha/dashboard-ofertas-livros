"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader (arquivo)
            for linha in leitor:
                livros.append(linha)
                print(linha ["titulo"])
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)
    
    return livros

def calcular_preco_medio(livros):
    
    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: float = preco_original.replace("£", "")
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

if __name__ == "__main__":
    livros = ler_livros()
    print(f"A quantidade de livros da coleção é de {len(livros)} livros.")

    preco_medio: float = calcular_preco_medio(livros)
    print(f"O preço médio dos livros é de £{preco_medio:.2f}")

    cinco_estrelas = contar_cinco_estrelas(livros)
    print("Quantidade de Estrelas")
