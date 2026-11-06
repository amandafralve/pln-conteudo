import nltk
import string
import random

# nltk.download("stopwords")
# nltk.download("punkt")
# nltk.download("punkt_tab")

# 1. CRIAÇÃO DA BASE DE DADOS
# Base de dados com 20 avaliações, com id, texto e classe
textos = [
    {"id": 1, "classe": 1, "texto": """Gostei muito desta HQ porque a história consegue prender a atenção desde as primeiras páginas. Os personagens são bem construídos e suas personalidades ficam cada vez mais interessantes conforme a trama avança. As ilustrações também combinam perfeitamente com os acontecimentos e ajudam bastante na criação da atmosfera. Foi uma leitura divertida, emocionante e que certamente recomendo para outros leitores."""},

    {"id": 2, "classe": 0, "texto": """Achei a história bastante cansativa e tive dificuldade para continuar a leitura até o final. O começo apresenta algumas ideias interessantes, mas o desenvolvimento acaba sendo muito lento e repetitivo. Alguns personagens parecem não ter uma função realmente importante dentro da narrativa, enquanto determinadas situações são prolongadas sem necessidade. Apesar de a arte ser razoável, o roteiro não conseguiu me envolver como eu esperava."""},

    {"id": 3, "classe": 1, "texto": """Esta foi uma das HQs que mais gostei de ler recentemente. A narrativa apresenta uma combinação muito boa entre aventura, drama e momentos de humor, fazendo com que a leitura não fique monótona. Os personagens possuem características próprias e conseguem transmitir diferentes emoções ao longo da história. Além disso, os desenhos são detalhados e ajudam a tornar as cenas mais marcantes e interessantes."""},

    {"id": 4, "classe": 0, "texto": """Infelizmente, a obra não conseguiu alcançar minhas expectativas. A ideia apresentada inicialmente parecia promissora, mas o desenvolvimento do enredo foi bastante previsível e não apresentou grandes surpresas. Alguns diálogos também parecem artificiais e pouco naturais, o que dificultou minha identificação com os personagens. A parte visual é bonita em alguns momentos, porém não foi suficiente para compensar os problemas encontrados na narrativa."""},

    {"id": 5, "classe": 1, "texto": """A experiência de leitura foi excelente, principalmente pela forma como a história trabalha os sentimentos dos personagens. Existem momentos de tensão, tristeza e esperança que tornam a narrativa bastante envolvente. Gostei especialmente da evolução do protagonista, que passa por várias situações difíceis e aprende com seus erros. A qualidade dos desenhos também merece destaque, pois cada página possui detalhes que enriquecem muito a obra."""},

    {"id": 6, "classe": 0, "texto": """Não gostei muito desta HQ porque senti que a história não conseguiu desenvolver adequadamente suas principais ideias. Muitas situações acontecem rapidamente, enquanto outras cenas são excessivamente longas e poderiam ter sido resumidas. Os personagens secundários também receberam pouca atenção, fazendo com que suas atitudes parecessem sem explicação. No geral, terminei a leitura com a sensação de que a obra poderia ter sido muito melhor."""},

    {"id": 7, "classe": 1, "texto": """A HQ apresenta uma história criativa e bastante original, principalmente pela maneira como utiliza seus personagens para desenvolver os acontecimentos. Gostei da ambientação e da forma como os desenhos complementam cada momento importante da narrativa. Algumas cenas são realmente memoráveis e conseguem transmitir bastante emoção sem precisar de muitos diálogos. Foi uma leitura agradável e diferente, que conseguiu me surpreender positivamente."""},

    {"id": 8, "classe": 0, "texto": """Minha opinião sobre esta HQ acabou sendo negativa porque a narrativa não conseguiu manter o mesmo nível apresentado no início. As primeiras páginas despertaram minha curiosidade, mas depois a história começou a ficar previsível e repetitiva. Também achei alguns personagens pouco desenvolvidos, especialmente aqueles que deveriam ter maior importância para o conflito principal. A arte possui bons momentos, mas o roteiro prejudicou bastante minha experiência."""},

    {"id": 9, "classe": 1, "texto": """Gostei bastante da construção da história e principalmente da relação entre os personagens principais. A narrativa consegue apresentar conflitos interessantes sem deixar de lado momentos mais leves, tornando a leitura equilibrada. As ilustrações possuem bastante personalidade e ajudam o leitor a compreender melhor as emoções presentes nas cenas. É uma HQ que consegue divertir, mas também apresenta temas interessantes que permanecem na cabeça depois da leitura."""},

    {"id": 10, "classe": 0, "texto": """Esperava encontrar uma história mais profunda, porém acabei achando o resultado pouco interessante. O enredo possui algumas ideias boas, mas elas não são aproveitadas da maneira que poderiam. Em vários momentos tive a impressão de que os acontecimentos estavam sendo colocados apenas para fazer a história avançar. Os desenhos são competentes, mas não conseguiram compensar a falta de desenvolvimento dos personagens e do conflito principal."""},

    {"id": 11, "classe": 1, "texto": """Esta HQ me surpreendeu positivamente pela qualidade do roteiro e pela maneira como a história consegue construir suspense. A cada capítulo aparecem novas informações que fazem o leitor querer descobrir o que acontecerá depois. Os personagens também apresentam mudanças convincentes ao longo da trama, principalmente o protagonista. A arte é muito expressiva e cria cenas visualmente fortes, tornando toda a experiência de leitura ainda mais interessante."""},

    {"id": 12, "classe": 0, "texto": """Achei a leitura bastante decepcionante porque a história prometia muito mais do que realmente entregou. O conflito principal demora para começar e, quando finalmente acontece, parece ser resolvido de maneira rápida demais. Alguns acontecimentos importantes não recebem explicações suficientes, deixando várias dúvidas ao final. Além disso, não consegui criar nenhuma conexão com os personagens, o que tornou a leitura ainda menos envolvente para mim."""},

    {"id": 13, "classe": 1, "texto": """Uma das melhores características desta HQ é a capacidade de equilibrar uma narrativa séria com momentos divertidos. Os personagens possuem personalidades diferentes e suas interações são responsáveis por várias das melhores partes da obra. Também gostei muito da qualidade visual, principalmente das expressões faciais e das cenas de ação. No conjunto, é uma história emocionante, bem produzida e que conseguiu me manter interessado até a última página."""},

    {"id": 14, "classe": 0, "texto": """Não achei esta HQ tão interessante quanto esperava. A história começa de maneira razoável, mas perde força conforme os capítulos avançam. Muitas situações acabam parecendo repetidas e algumas decisões dos personagens não fazem muito sentido dentro do contexto apresentado. O ritmo também é irregular, alternando momentos extremamente lentos com acontecimentos muito rápidos. Apesar de possuir uma arte bonita, o conteúdo não conseguiu me conquistar."""},

    {"id": 15, "classe": 1, "texto": """A leitura foi muito agradável e conseguiu despertar várias emoções diferentes durante a história. O roteiro é bem estruturado e apresenta acontecimentos que fazem sentido dentro do universo criado pelo autor. Gostei principalmente da evolução dos personagens, que não permanecem iguais durante toda a narrativa. As ilustrações também são muito bonitas e possuem uma identidade própria. É uma obra que eu recomendaria facilmente para quem gosta de quadrinhos."""},

    {"id": 16, "classe": 0, "texto": """Infelizmente, não consegui aproveitar muito esta HQ. O principal problema, na minha opinião, está no roteiro, que apresenta muitos acontecimentos sem desenvolver adequadamente suas consequências. Alguns personagens aparecem e desaparecem sem que sua participação fique realmente clara. Também achei determinados diálogos exagerados e pouco naturais. A parte visual é interessante, mas uma boa arte não foi suficiente para tornar a história envolvente."""},

    {"id": 17, "classe": 1, "texto": """Gostei muito da maneira como a HQ apresenta seus personagens e desenvolve seus conflitos pessoais. A história consegue criar momentos emocionantes sem parecer exagerada, e várias cenas possuem bastante impacto. Outro ponto positivo é a qualidade das ilustrações, que apresentam muitos detalhes e ajudam a transmitir o clima de cada situação. Quando terminei a leitura, fiquei com vontade de conhecer outras histórias do mesmo universo."""},

    {"id": 18, "classe": 0, "texto": """A história não funcionou para mim porque achei o desenvolvimento muito irregular. Algumas partes são interessantes, mas outras parecem ter sido incluídas apenas para aumentar o número de páginas. O protagonista também não apresentou mudanças significativas durante a narrativa, tornando difícil acompanhar sua trajetória. O final foi especialmente decepcionante, pois esperava uma conclusão mais bem trabalhada e coerente com tudo que havia acontecido anteriormente."""},

    {"id": 19, "classe": 1, "texto": """Esta HQ conseguiu superar minhas expectativas e foi uma leitura que aproveitei bastante. O roteiro apresenta boas ideias, os personagens possuem características marcantes e a história consegue manter um ritmo agradável durante a maior parte do tempo. As ilustrações também são muito bem feitas e contribuem para o impacto das cenas mais importantes. No geral, considero uma obra criativa, emocionante e muito recomendável para quem gosta de quadrinhos."""},

    {"id": 20, "classe": 0, "texto": """Apesar de ter começado a leitura com bastante expectativa, terminei a HQ sem sentir que a história realmente me conquistou. O enredo apresenta algumas ideias interessantes, mas o desenvolvimento é previsível e não cria momentos de grande impacto. Também achei que os personagens poderiam ter sido melhor explorados, principalmente os secundários. A arte possui qualidade, porém, para mim, não foi suficiente para esconder os problemas presentes no roteiro."""},
]

# 2. PRÉ-PROCESSAMENTO DOS TEXTOS
# Obter stopwords em português
stop_words = nltk.corpus.stopwords.words("portuguese")

# preservando palavras de negação para a análise
palavras_negacao = ["não", "nunca", "nem", "jamais"]
for palavra in palavras_negacao:
    if palavra in stop_words:
        stop_words.remove(palavra)

stop_words = set(stop_words)
pontuacao = string.punctuation + "“”‘’—–…"
textos_processados = []

# Pré-processar as 20 avaliações
for item in textos:
    # 1. Converter para letras minúsculas
    texto = item["texto"].lower()
    # 2. Remover pontuação
    texto = texto.translate(str.maketrans("", "", pontuacao))
    # 3. Separar o texto em palavras
    palavras = nltk.word_tokenize(texto, language="portuguese")
    # 4. Remover stopwords, preservando as negações
    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in stop_words
    ]

    # Armazenar o resultado
    textos_processados.append(palavras_filtradas)

# Exibir o resultado de cada avaliação
for item, palavras in zip(textos, textos_processados):
    print(f"\nAvaliação {item['id']} (classe {item['classe']}):")
    print(palavras)

print("\nTotal de avaliações processadas:", len(textos_processados))

# 3. TRANSFORMAÇÃO DOS TEXTOS EM NÚMEROS
# Contar em quantas avaliações cada palavra aparece
contagem = {}
for palavras in textos_processados:
    for palavra in set(palavras):  #conta no máximo 1x por avaliação
        contagem[palavra] = contagem.get(palavra, 0) + 1

# vocabulário: palavras que aparecem em pelo menos 2 avaliações
vocabulario = sorted(
    palavra for palavra, freq in contagem.items() if freq >= 2
)

print("Tamanho do vocabulário:", len(vocabulario))
print("Vocabulário:", vocabulario)

# Transformar cada avaliação em um vetor binário
# 1 = a palavra do vocabulário aparece na avaliação
# 0 = a palavra não aparece
X = []
for palavras in textos_processados:
    presentes = set(palavras)
    vetor = [1 if palavra in presentes else 0 for palavra in vocabulario]
    X.append(vetor)

# Classes (rótulos) na mesma ordem dos vetores
y = [item["classe"] for item in textos]

# Conferência
print("\nDimensão de X:", len(X), "avaliações x", len(X[0]), "palavras")
print("Dimensão de y:", len(y))

# 4. IMPLEMENTAÇÃO DO PERCEPTRON
random.seed(42)

def ativacao(soma):
    return 1 if soma > 0.5 else 0

taxa_aprendizagem = 0.1
max_epocas = 100

n_caracteristicas = len(X[0])
pesos = [random.uniform(-0.5, 0.5) for _ in range(n_caracteristicas)]
bias = random.uniform(-0.5, 0.5)

def calcular_soma(vetor):
    # Soma
    return sum(x * w for x, w in zip(vetor, pesos)) + bias

def prever(vetor):
    return ativacao(calcular_soma(vetor))


# 5. TREINAMENTO
print("\nTREINAMENTO")
epocas_treinadas = 0
for epoca in range(1, max_epocas + 1):
    erros = 0
    for vetor, classe_real in zip(X, y):
        classe_prevista = prever(vetor)
        erro = classe_real - classe_prevista

        if erro != 0:
            for i in range(n_caracteristicas):
                pesos[i] += taxa_aprendizagem * erro * vetor[i]
            bias += taxa_aprendizagem * erro
            erros += 1

    epocas_treinadas = epoca
    print(f"Época {epoca}: {erros} erros")


# 6. TESTE DO MODELO
print("\nTESTE DO MODELO")
nome_classe = {1: "Positiva", 0: "Negativa"}
corretas = 0
incorretas_ids = []

for item, vetor in zip(textos, X):
    classe_prevista = prever(vetor)
    acertou = classe_prevista == item["classe"]

    if acertou:
        corretas += 1
    else:
        incorretas_ids.append(item["id"])

    print(f"\nAvaliação {item['id']}")
    print(f"Texto: {item['texto'][:90]}...")
    print(f"Classe real: {item['classe']} ({nome_classe[item['classe']]})")
    print(f"Classe prevista: {classe_prevista} ({nome_classe[classe_prevista]})")
    print(f"Resultado: {'Correto' if acertou else 'Incorreto'}")


# 7. CÁLCULO DA PORCENTAGEM DE ACERTO
total = len(textos)
incorretas = total - corretas
acuracia = (corretas / total) * 100

print("\nACURÁCIA")
print(f"Total de avaliações: {total}")
print(f"Classificações corretas: {corretas}")
print(f"Classificações incorretas: {incorretas}")
print(f"Acurácia: {acuracia:.0f}%")
print(f"IDs classificados incorretamente: {incorretas_ids}")


# 8. TESTE COM NOVAS AVALIAÇÕES
def preprocessar(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", pontuacao))
    palavras = nltk.word_tokenize(texto, language="portuguese")
    return [p for p in palavras if p not in stop_words]

def vetorizar(texto):
    presentes = set(preprocessar(texto))
    return [1 if p in presentes else 0 for p in vocabulario]

novas_avaliacoes = [
    {"texto": "A história é emocionante e os desenhos são lindos, recomendo a leitura.", "classe": 1},
    {"texto": "Não gostei, a narrativa é previsível e os personagens são pouco desenvolvidos.", "classe": 0},
    {"texto": "Uma HQ criativa, com personagens marcantes e uma leitura muito agradável.", "classe": 1},
    {"texto": "Achei cansativa e repetitiva, o roteiro não me conquistou.", "classe": 0},
    {"texto": "Leitura divertida, com boas ideias e ilustrações detalhadas.", "classe": 1},
    {"texto": "A obra foi decepcionante, com diálogos artificiais e final fraco.", "classe": 0},
    # casos difíceis para o Bag of Words (negação e ironia)
    {"texto": "A história não é ruim, achei bem divertida e envolvente.", "classe": 1},
    {"texto": "Que maravilha, mais uma história previsível e cansativa. Parabéns!", "classe": 0},
]

print("\nTESTE COM NOVAS AVALIAÇÕES")
acertos_novas = 0
incorretas_novas = []

for i, nova in enumerate(novas_avaliacoes, start=1):
    classe_prevista = prever(vetorizar(nova["texto"]))
    acertou = classe_prevista == nova["classe"]
    acertos_novas += acertou

    if not acertou:
        incorretas_novas.append(i)

    print(f"\nNova avaliação {i}")
    print(f"Texto: {nova['texto']}")
    print(f"Classe real: {nova['classe']} ({nome_classe[nova['classe']]})")
    print(f"Classe prevista: {classe_prevista} ({nome_classe[classe_prevista]})")
    print(f"Resultado: {'Correto' if acertou else 'Incorreto'}")

acuracia_novas = (acertos_novas / len(novas_avaliacoes)) * 100

print("\nACURÁCIA NAS NOVAS AVALIAÇÕES")
print(f"Total de avaliações: {len(novas_avaliacoes)}")
print(f"Classificações corretas: {acertos_novas}")
print(f"Classificações incorretas: {len(novas_avaliacoes) - acertos_novas}")
print(f"Acurácia: {acuracia_novas:.0f}%")
print(f"Números classificados incorretamente: {incorretas_novas}")

