import numpy as np

# criação de array x1, x2
X = np.array([[0,0],[0,1],[1,0],[1,1]])
pesos = [0.5,0.5]
Y = np.array([0,0,0,1])

qtdEntradas = 0
taxaAprendizagem=0.5

for entrada in X:
    i=0
    soma = 0
    classeReal = Y[qtdEntradas]
    
    for xi in entrada:        
        soma += xi*pesos[i]
        
    #função de ativação
    if soma >=1:
        yp = 1
    else:
        yp=0
    
    if yp == classeReal:
        print("Acertou")
    else:
        print("Errrou")
        for p in pesos:
            p = p + taxaAprendizagem * (yp-classeReal)*xi

    soma = 0