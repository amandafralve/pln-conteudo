import nltk
import string


# Base de dados com 20 avaliações
textos = [
    """Gostei muito desta HQ porque a história consegue prender a atenção desde as primeiras páginas. Os personagens são bem construídos e suas personalidades ficam cada vez mais interessantes conforme a trama avança. As ilustrações também combinam perfeitamente com os acontecimentos e ajudam bastante na criação da atmosfera. Foi uma leitura divertida, emocionante e que certamente recomendo para outros leitores.""",

    """Achei a história bastante cansativa e tive dificuldade para continuar a leitura até o final. O começo apresenta algumas ideias interessantes, mas o desenvolvimento acaba sendo muito lento e repetitivo. Alguns personagens parecem não ter uma função realmente importante dentro da narrativa, enquanto determinadas situações são prolongadas sem necessidade. Apesar de a arte ser razoável, o roteiro não conseguiu me envolver como eu esperava.""",

    """Esta foi uma das HQs que mais gostei de ler recentemente. A narrativa apresenta uma combinação muito boa entre aventura, drama e momentos de humor, fazendo com que a leitura não fique monótona. Os personagens possuem características próprias e conseguem transmitir diferentes emoções ao longo da história. Além disso, os desenhos são detalhados e ajudam a tornar as cenas mais marcantes e interessantes.""",

    """Infelizmente, a obra não conseguiu alcançar minhas expectativas. A ideia apresentada inicialmente parecia promissora, mas o desenvolvimento do enredo foi bastante previsível e não apresentou grandes surpresas. Alguns diálogos também parecem artificiais e pouco naturais, o que dificultou minha identificação com os personagens. A parte visual é bonita em alguns momentos, porém não foi suficiente para compensar os problemas encontrados na narrativa.""",

    """A experiência de leitura foi excelente, principalmente pela forma como a história trabalha os sentimentos dos personagens. Existem momentos de tensão, tristeza e esperança que tornam a narrativa bastante envolvente. Gostei especialmente da evolução do protagonista, que passa por várias situações difíceis e aprende com seus erros. A qualidade dos desenhos também merece destaque, pois cada página possui detalhes que enriquecem muito a obra.""",

    """Não gostei muito desta HQ porque senti que a história não conseguiu desenvolver adequadamente suas principais ideias. Muitas situações acontecem rapidamente, enquanto outras cenas são excessivamente longas e poderiam ter sido resumidas. Os personagens secundários também receberam pouca atenção, fazendo com que suas atitudes parecessem sem explicação. No geral, terminei a leitura com a sensação de que a obra poderia ter sido muito melhor.""",

    """A HQ apresenta uma história criativa e bastante original, principalmente pela maneira como utiliza seus personagens para desenvolver os acontecimentos. Gostei da ambientação e da forma como os desenhos complementam cada momento importante da narrativa. Algumas cenas são realmente memoráveis e conseguem transmitir bastante emoção sem precisar de muitos diálogos. Foi uma leitura agradável e diferente, que conseguiu me surpreender positivamente.""",

    """Minha opinião sobre esta HQ acabou sendo negativa porque a narrativa não conseguiu manter o mesmo nível apresentado no início. As primeiras páginas despertaram minha curiosidade, mas depois a história começou a ficar previsível e repetitiva. Também achei alguns personagens pouco desenvolvidos, especialmente aqueles que deveriam ter maior importância para o conflito principal. A arte possui bons momentos, mas o roteiro prejudicou bastante minha experiência.""",

    """Gostei bastante da construção da história e principalmente da relação entre os personagens principais. A narrativa consegue apresentar conflitos interessantes sem deixar de lado momentos mais leves, tornando a leitura equilibrada. As ilustrações possuem bastante personalidade e ajudam o leitor a compreender melhor as emoções presentes nas cenas. É uma HQ que consegue divertir, mas também apresenta temas interessantes que permanecem na cabeça depois da leitura.""",

    """Esperava encontrar uma história mais profunda, porém acabei achando o resultado pouco interessante. O enredo possui algumas ideias boas, mas elas não são aproveitadas da maneira que poderiam. Em vários momentos tive a impressão de que os acontecimentos estavam sendo colocados apenas para fazer a história avançar. Os desenhos são competentes, mas não conseguiram compensar a falta de desenvolvimento dos personagens e do conflito principal.""",

    """Esta HQ me surpreendeu positivamente pela qualidade do roteiro e pela maneira como a história consegue construir suspense. A cada capítulo aparecem novas informações que fazem o leitor querer descobrir o que acontecerá depois. Os personagens também apresentam mudanças convincentes ao longo da trama, principalmente o protagonista. A arte é muito expressiva e cria cenas visualmente fortes, tornando toda a experiência de leitura ainda mais interessante.""",

    """Achei a leitura bastante decepcionante porque a história prometia muito mais do que realmente entregou. O conflito principal demora para começar e, quando finalmente acontece, parece ser resolvido de maneira rápida demais. Alguns acontecimentos importantes não recebem explicações suficientes, deixando várias dúvidas ao final. Além disso, não consegui criar nenhuma conexão com os personagens, o que tornou a leitura ainda menos envolvente para mim.""",

    """Uma das melhores características desta HQ é a capacidade de equilibrar uma narrativa séria com momentos divertidos. Os personagens possuem personalidades diferentes e suas interações são responsáveis por várias das melhores partes da obra. Também gostei muito da qualidade visual, principalmente das expressões faciais e das cenas de ação. No conjunto, é uma história emocionante, bem produzida e que conseguiu me manter interessado até a última página.""",

    """Não achei esta HQ tão interessante quanto esperava. A história começa de maneira razoável, mas perde força conforme os capítulos avançam. Muitas situações acabam parecendo repetidas e algumas decisões dos personagens não fazem muito sentido dentro do contexto apresentado. O ritmo também é irregular, alternando momentos extremamente lentos com acontecimentos muito rápidos. Apesar de possuir uma arte bonita, o conteúdo não conseguiu me conquistar.""",

    """A leitura foi muito agradável e conseguiu despertar várias emoções diferentes durante a história. O roteiro é bem estruturado e apresenta acontecimentos que fazem sentido dentro do universo criado pelo autor. Gostei principalmente da evolução dos personagens, que não permanecem iguais durante toda a narrativa. As ilustrações também são muito bonitas e possuem uma identidade própria. É uma obra que eu recomendaria facilmente para quem gosta de quadrinhos.""",

    """Infelizmente, não consegui aproveitar muito esta HQ. O principal problema, na minha opinião, está no roteiro, que apresenta muitos acontecimentos sem desenvolver adequadamente suas consequências. Alguns personagens aparecem e desaparecem sem que sua participação fique realmente clara. Também achei determinados diálogos exagerados e pouco naturais. A parte visual é interessante, mas uma boa arte não foi suficiente para tornar a história envolvente.""",

    """Gostei muito da maneira como a HQ apresenta seus personagens e desenvolve seus conflitos pessoais. A história consegue criar momentos emocionantes sem parecer exagerada, e várias cenas possuem bastante impacto. Outro ponto positivo é a qualidade das ilustrações, que apresentam muitos detalhes e ajudam a transmitir o clima de cada situação. Quando terminei a leitura, fiquei com vontade de conhecer outras histórias do mesmo universo.""",

    """A história não funcionou para mim porque achei o desenvolvimento muito irregular. Algumas partes são interessantes, mas outras parecem ter sido incluídas apenas para aumentar o número de páginas. O protagonista também não apresentou mudanças significativas durante a narrativa, tornando difícil acompanhar sua trajetória. O final foi especialmente decepcionante, pois esperava uma conclusão mais bem trabalhada e coerente com tudo que havia acontecido anteriormente.""",

    """Esta HQ conseguiu superar minhas expectativas e foi uma leitura que aproveitei bastante. O roteiro apresenta boas ideias, os personagens possuem características marcantes e a história consegue manter um ritmo agradável durante a maior parte do tempo. As ilustrações também são muito bem feitas e contribuem para o impacto das cenas mais importantes. No geral, considero uma obra criativa, emocionante e muito recomendável para quem gosta de quadrinhos.""",

    """Apesar de ter começado a leitura com bastante expectativa, terminei a HQ sem sentir que a história realmente me conquistou. O enredo apresenta algumas ideias interessantes, mas o desenvolvimento é previsível e não cria momentos de grande impacto. Também achei que os personagens poderiam ter sido melhor explorados, principalmente os secundários. A arte possui qualidade, porém, para mim, não foi suficiente para esconder os problemas presentes no roteiro."""
]

# Obter stopwords em português
stop_words = nltk.corpus.stopwords.words("portuguese")

# Preservar palavras de negação importantes para análise de sentimentos
palavras_negacao = ["não", "nunca", "nem", "jamais"]

for palavra in palavras_negacao:
    if palavra in stop_words:
        stop_words.remove(palavra)

# Pontuação comum e alguns sinais adicionais
pontuacao = string.punctuation + "“”‘’—–…"

# Lista para armazenar todas as avaliações processadas
textos_processados = []

# Pré-processar as 20 avaliações
for texto in textos:

    # 1. Converter para letras minúsculas
    texto = texto.lower()

    # 2. Remover pontuação
    texto = texto.translate(
        str.maketrans("", "", pontuacao)
    )

    # 3. Separar o texto em palavras
    palavras = nltk.word_tokenize(texto, language="portuguese")

    # 4. Remover stopwords, preservando as negações
    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in stop_words
    ]

    # Armazenar o resultado
    textos_processados.append(palavras_filtradas)


# Exibir todas as avaliações processadas
for i, palavras in enumerate(textos_processados, start=1):
    print(f"\nAvaliação {i}:")
    print(palavras)

print("\nTotal de avaliações processadas:", len(textos_processados))