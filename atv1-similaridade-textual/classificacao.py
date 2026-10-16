import string
from pathlib import Path
import pandas as pd
import numpy as np
import nltk

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

# Avaliações de referência
ref_positiva = "O produto possui excelente qualidade, chegou rapidamente e atendeu completamente às minhas expectativas. Gostei muito da compra e recomendo este produto para outras pessoas."

ref_negativa = "O produto possui péssima qualidade, apresentou problemas logo após a compra e não atendeu às minhas expectativas. Fiquei muito decepcionado e não recomendo este produto."

# LEITURA DO ARQUIVO EXCEL
PASTA_ATUAL = Path(__file__).parent
CAMINHO_EXCEL = PASTA_ATUAL / "avaliacoes.xlsx"
df = pd.read_excel(CAMINHO_EXCEL)
df["avaliacao"] = df["avaliacao"].fillna("").astype(str)

# posição 0 = REF positiva, posição 1 = REF negativa, resto = avaliações do Excel
textos = [ref_positiva, ref_negativa] + list(df["avaliacao"])

# StopWords e preservando palavras de negação importantes para análise
stop_words = nltk.corpus.stopwords.words("portuguese")
palavras_negacao = ["não", "nunca", "jamais"]

for palavra in palavras_negacao:
    if palavra in stop_words:
        stop_words.remove(palavra)

pontuacao = string.punctuation + "“”‘’—–…"

# PRÉ-PROCESSAMENTO DOS TEXTOS
textos_processados = []

for texto in textos:
    # Conversão para letras minúsculas, remoção de pontuação e espaços desnecessários, e tokenização das palavras.
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", pontuacao))
    palavras = nltk.word_tokenize(texto, language="portuguese")
    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in stop_words
    ]
    # Armazenar o resultado
    textos_processados.append(palavras_filtradas)


# SIMILARIDADE DE JACCARD
def jaccard(palavras1, palavras2):
    # Conjuntos de palavras (sem repetição)
    p1 = set(palavras1)
    p2 = set(palavras2)

    # Intersecção: palavras presentes nos dois textos
    interseccao = 0
    for palavra1 in p1:
        for palavra2 in p2:
            if palavra1 == palavra2:
                interseccao = interseccao + 1

    # União: |A| + |B| - |A ∩ B|  (a intersecção é subtraída para não contar duas vezes)
    uniao = (len(p1) + len(p2)) - interseccao

    if uniao == 0:
        return 0.0
    return interseccao / uniao


# DISTÂNCIA DE LEVENSHTEIN
def levenshtein(seq1, seq2):
    # criar uma matriz
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))

    # atribuir valor aos números das colunas (0,n-1)
    for x in range(size_x):
        matrix[x, 0] = x

    # atribuir valor aos números das linhas (0,n-1)
    for y in range(size_y):
        matrix[0, y] = y

    # calcular a distância
    for x in range(1, size_x):
        for y in range(1, size_y):
            # se os caracteres são iguais, não aumenta a distância
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = matrix[x - 1, y - 1]
            # se são diferentes, aumenta a distância em 1
            else:
                matrix[x, y] = min(matrix[x - 1, y], matrix[x - 1, y - 1], matrix[x, y - 1])
                matrix[x, y] = matrix[x, y] + 1

    return int(matrix[size_x - 1, size_y - 1])


# Para Levenshtein, as palavras processadas voltam a ser uma string 
textos_str = [" ".join(palavras) for palavras in textos_processados]

pos_tokens, neg_tokens = textos_processados[0], textos_processados[1]
pos_str, neg_str = textos_str[0], textos_str[1]

# CÁLCULO E CLASSIFICAÇÃO (apenas as avaliações do Excel, a partir da posição 2)
resultados = []

for i in range(len(df)):
    tokens = textos_processados[i + 2]
    texto_str = textos_str[i + 2]

    jac_pos = jaccard(tokens, pos_tokens)
    jac_neg = jaccard(tokens, neg_tokens)
    lev_pos = levenshtein(texto_str, pos_str)
    lev_neg = levenshtein(texto_str, neg_str)

    # Jaccard: maior similaridade = mais próximo
    class_jac = "Positiva" if jac_pos > jac_neg else "Negativa"
    # Levenshtein: menor distância = mais próximo
    class_lev = "Positiva" if lev_pos < lev_neg else "Negativa"

    resultados.append({
        "ID": df.loc[i, "ID"],
        "Avaliação": df.loc[i, "avaliacao"],
        "Jaccard Pos.": round(jac_pos, 4),
        "Jaccard Neg.": round(jac_neg, 4),
        "Class. Jaccard": class_jac,
        "Lev. Pos.": lev_pos,
        "Lev. Neg.": lev_neg,
        "Class. Lev.": class_lev,
    })

df_resultado = pd.DataFrame(resultados)

# TABELA DE RESULTADOS
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 40)
print(df_resultado.to_string(index=False))

# Exportação para Excel
df_resultado.to_excel(PASTA_ATUAL / "resultados_classificacao.xlsx", index=False)

# ANÁLISE DOS RESULTADOS
mesma = (df_resultado["Class. Jaccard"] == df_resultado["Class. Lev."]).sum()

print("\n===== ANÁLISE DOS RESULTADOS =====")
print("1. Positivas (Jaccard):     ", (df_resultado["Class. Jaccard"] == "Positiva").sum())
print("2. Negativas (Jaccard):     ", (df_resultado["Class. Jaccard"] == "Negativa").sum())
print("3. Positivas (Levenshtein): ", (df_resultado["Class. Lev."] == "Positiva").sum())
print("4. Negativas (Levenshtein): ", (df_resultado["Class. Lev."] == "Negativa").sum())
print("5. Mesma classificação:     ", mesma)
print("6. Classificação diferente: ", len(df_resultado) - mesma)

dif_jac = (df_resultado["Jaccard Pos."] - df_resultado["Jaccard Neg."]).abs()
dif_lev = (df_resultado["Lev. Pos."] - df_resultado["Lev. Neg."]).abs()
print("\nDiferença média |Pos - Neg| Jaccard:     ", round(dif_jac.mean(), 4))
print("Diferença média |Pos - Neg| Levenshtein: ", round(dif_lev.mean(), 2))
print("Empates em Jaccard:     ", (df_resultado["Jaccard Pos."] == df_resultado["Jaccard Neg."]).sum())
print("Empates em Levenshtein: ", (df_resultado["Lev. Pos."] == df_resultado["Lev. Neg."]).sum())