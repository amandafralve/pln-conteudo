import nltk
from nltk.corpus import stopwords
import string

texto = "Não gostei, meu Samsung era melhor. Não gostei da qualidade do som, não gostei da volta na orelha, não casou bem com minha orelha. Ou seja, meio decepcionante"

# 1. Tokenização
palavras = nltk.word_tokenize(texto)
frases = nltk.sent_tokenize(texto)

# OUTPUT
print("-"*70)
print("TOKENIZAÇÃO DE PALAVRAS")
print(palavras)

print('-'*70)
print("TOKENIZAÇÃO DE FRASES")
print(frases)

# 2. Avaliação sem palavras repetidas (mantendo apenas palavras, ignorando maiúsculas/minúsculas para deduplicar)
vocabulario = []
vocabulario_sem_repetidos = []

for text in texto:
    palavras = nltk.word_tokenize(texto.lower())
    print(palavras)
    print()

    for palavra in palavras:
        vocabulario.append(palavra)

vocabulario_sem_repetidos = set(vocabulario)

reducao = (len(vocabulario_sem_repetidos)/len(vocabulario)*100)

print("-"*70)
print("AVALIAÇÃO SEM PALAVRAS REPETIDAS")
print(vocabulario_sem_repetidos)
# Porcentagem de redução 1: (Total Tokenizado Original -> Sem Repetidas Limpas)
print(f"Porcentagem de redução: {reducao:.2f}%")

# 3. Avaliação sem palavras repetidas E sem stopwords

print("-"*70)
print("AVALIAÇÃO SEM PALAVRAS REPETIDAS E SEM STOPWORDS")
# print(sem_stopwords)
# Porcentagem de redução 2: (Total Tokenizado Original -> Sem Repetidas e Sem Stopwords)
# print(f"Porcentagem de redução: {reducao_stopords:.2f}%")


# 4. Lematização / Stemming (RSLP Stemmer para PT-BR)


print("-"*70)
print("AVALIAÇÃO COM LEMATIZAÇÃO S/ PALAVRAS REPETIDAS E S/ STOPWORDS")
print()
