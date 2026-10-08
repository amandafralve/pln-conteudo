import  nltk

texto= "Vou-me embora pra Pasárgada Lá sou amigo do rei Lá tenho a mulher que eu quero Na cama que escolherei Vou-me embora pra Pasárgada Vou-me embora pra Pasárgada Aqui eu não sou feliz Lá a existência é uma aventur De tal modo inconseqüente Que Joana a Louca de Espanha Rainha e falsa demente Vem a ser contraparente Da nora que nunca tive E como farei ginástica Andarei de bicicleta Montarei em burro brabo Subirei no pau-de-sebo Tomarei banhos de mar! E quando estiver cansado Deito na beira do rio Mando chamar a mãe - d’água. Pra me contar as histórias Que no tempo de eu menino Rosa vinha me contar Vou-me embora pra Pasárgada Em Pasárgada tem tudo É outra civilização Tem um processo seguro De impedir a concepção Tem telefone automático Tem alcalóide à vontade Tem prostitutas bonitas Para a gente namorar E quando eu estiver mais triste Mas triste de não ter jeito Quando de noite me der Vontade de me matar - Lá sou amigo do rei - Terei a mulher que eu quero Na cama que escolherei Vou-me embora pra Pasárgada."

vocabulario = []

palavras = nltk.word_tokenize(texto.lower())

tamanho_original = len(palavras)

stop_words = nltk.corpus.stopwords.words("portuguese")

for palavra in palavras:
    if not(palavra in stop_words):
        vocabulario.append(palavra)

print(stop_words)
print()
print(vocabulario)

#print(stop_words)
tamanho_sem_stopwords = len(vocabulario)
print(vocabulario)

tamanho_sem_repetidos = len(set(vocabulario))

print()
print("TAMANHO ORIGINAL:")
print(tamanho_original)

print()
print("TAMANHO SEM STOPWORDS:")
print(tamanho_sem_stopwords)

print()
print("TAMANHO SEM REPETIDOS:")
print(tamanho_sem_repetidos)

reducao = 1 - (tamanho_sem_repetidos/tamanho_original)
print()
print("REDUCAO:")
print(reducao)
