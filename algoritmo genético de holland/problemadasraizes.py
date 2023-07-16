import random

ind = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

adaptacao = []  #guardar a adaptação de cada individuo nesse vetor
c = 1 #contador de gerações

def gera_populacao(ind):
    for i in range(10):
        for j in range(10):
            ind[i][j] = random.randint(0, 1)

def g(x):
    return x ** 2 - 9

def decodifica(binario):
    
    bit_sinal = binario[0]
    bits_valor = binario[1:]
    
    valor_decimal = int(''.join(str(bit) for bit in bits_valor), 2)

    if bit_sinal == 1:
        valor_decimal = -valor_decimal
    
    return valor_decimal

def penalidade(ind, i):
    
    x1 = decodifica(ind[i][0:5])
    x2 = decodifica(ind[i][5:])

    if -10 < x1 < 10 and -10 < x2 < 10 and x1 != x2:
            return 0
    else: 
        return 999

def calcula_adaptacao(ind, i):
    
    return -abs(0 + g(decodifica(ind[i][0:5])) + g(decodifica(ind[i][5:])) + penalidade(ind, i))

def seleciona(ind, adaptacao):
    
    # Combina as duas listas usando zip() e Ordena a lista combinada com base nos valores da adaptação
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
    f1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    f2 = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
    
    for i in range(5):
        for j in range(i, 5):
            r = random.randint(0, 100)
            if r >= 60:
                r = random.randint(0, 10)
                for k in range(7):
                    f1[k]= ind[i][k]
                    f2[k] = ind[j][k]
                for k in range(r+1, 10):
                    f1[k] = ind[j][k]
                    f2[k] = ind[i][k]
                ind.append(f1)
                ind.append(f2)

def muta(ind):
    m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(5):
        r = random.randint(0, 100)
        if r >= 90:
            for j in range(10):
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


#Gera a população inicial aleatoriamente
gera_populacao(ind)

#Calcula a adaptação de cada individuo da população inicial
for i in range(len(ind)):
    adaptacao.append(calcula_adaptacao(ind, i))

#Loop para continuar gerando novos descendentes e os mutando até que haja um cromossomo com 
# adaptação 0 (raízes da função quadrática)
while 0 not in adaptacao:
    
    #Seleciona os 5 indivíduos mais adaptados
    ind, adaptacao = seleciona(ind, adaptacao)
    
    #Cruza esses indivíduos e gera descendentes
    cruza(ind)
    
    #Possibilidade de um ou mais da população selecionada mutarem
    muta(ind)

    #Depois de gerar novos descendentes, define os graus de adaptação deles
    for i in range(5, len(ind)):
        adaptacao.append(calcula_adaptacao(ind, i))
    
    #Depois de mutar. define os graus de adaptação dos mutados
    for i in range(5):
        adaptacao[i] = calcula_adaptacao(ind, i)

    c = c+1
    print('\n', adaptacao)

#Printa o cromossomo com a maior substring '01'
indice = adaptacao.index(0)
print('\n As raízes foram encontradas na ' + str(c) + 'ª geração:\nx1 = ' + str(decodifica(ind[indice][0:5])) + ' e x2 = ' + str(decodifica(ind[indice][5:])))
