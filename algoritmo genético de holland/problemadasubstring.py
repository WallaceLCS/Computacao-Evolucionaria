import random

ind = [[1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8]]

adaptacao = []  #guardar a adaptação de cada individuo nesse vetor
c = 1 #contador de gerações

def gera_populacao(ind):
    for i in range(10):
        for j in range(8):
            ind[i][j] = random.randint(0, 1)

def calcula_adaptacao(ind, i):
    c = 0
    for j in range(7):
        if ind[i][j] == 0 and ind[i][j+1] == 1:
            c += 1
    return c

def seleciona(ind, adaptacao):
    # Combinar as duas listas usando zip() e Ordena a lista combinada com base nos valores da adaptação
    combinado = list(zip(ind, adaptacao))
    combinado.sort(key=lambda x: x[1], reverse=True)

    # Separar novamente a lista combinada em duas listas separadas
    ind_ordenado, adaptacao_ordenado = (zip(*combinado))
    
    ind_ordenado, adaptacao_ordenado = list(ind_ordenado), list(adaptacao_ordenado)

    while len(ind_ordenado) > 5:
        ind_ordenado.pop()
        adaptacao_ordenado.pop()
    
    return ind_ordenado, adaptacao_ordenado

def cruza(ind):
    f1 = [0, 0, 0, 0, 0, 0, 0, 0]
    f2 = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(5):
        for j in range(i, 5):
            r = random.randint(0, 100)
            if r >= 60:
                r = random.randint(0, 8)
                for k in range(5):
                    f1[k]= ind[i][k]
                    f2[k] = ind[j][k]
                for k in range(r+1, 8):
                    f1[k] = ind[j][k]
                    f2[k] = ind[i][k]
                ind.append(f1)
                ind.append(f2)

def muta(ind):
    m = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(5):
        r = random.randint(0, 100)
        if r >= 90:
            for j in range(8):
                r = random.randint(0, 1)
                if r == 1:
                    if ind[i][j] == 1:
                        m[j] = 0
                    else: 
                        m[j] = 1
                else:
                    m[j] = ind[i][j]
            #Substitui o cromossomo por sua versão mutada
            ind[i] = m
            adaptacao[i] = calcula_adaptacao(ind, i)
    

#Gera a população inicial aleatoriamente
gera_populacao(ind)

#Calcula a adaptação de cada individuo da população inicial
for i in range(len(ind)):
    adaptacao.append(calcula_adaptacao(ind, i))

#Loop para continuar gerando novos descendentes e os mutando até que haja um cromossomo com 
# adaptação 4 (maior substring)
while [0, 1, 0, 1, 0, 1, 0, 1] not in ind:
    
    #Seleciona os 5 indivíduos mais adaptados
    ind, adaptacao = seleciona(ind, adaptacao)
    
    #Cruza esses indivíduos e gera descendentes
    cruza(ind)
    
    #Possibilidade de um ou mais da população selecionada mutarem
    muta(ind)

    #Depois de gerar novos descendentes, define os graus de adaptação deles
    for i in range(5, len(ind)):
        adaptacao.append(calcula_adaptacao(ind, i))
    
    print('\n', ind)
    c = c+1

#Printa o cromossomo com a maior substring '01'
indice = ind.index([0, 1, 0, 1, 0, 1, 0, 1])
print('\n O indivíduo com maior substring foi encontrado na ' + str(c) + 'ª geração:\n', ind[indice])