import random
import time


#função que cria peças
def cria_pecas():
    pecas = []
    i=0
    while i<=6:
        ii=0
        while ii<=6:
            if [i, ii] not in pecas and [ii, i] not in pecas:
                pecas.append([i, ii])
            ii+=1
        i+=1
    random.shuffle(pecas) #embaralhando
    return pecas


#função que inicia o jogo
def inicia_jogo(n, pecas):
    inicio = {
        'jogadores' : {

        },
        'monte' : [],
        'mesa' : []
    }
    i=0
    while i<n:
        inicio['jogadores'][i]=[]
        i+=1
    indisponiveis = []
    for peca in pecas:
        ii=0
        while ii<n:
            if len(inicio['jogadores'][ii])<7:
                if peca not in indisponiveis:
                    inicio['jogadores'][ii].append(peca)
                    indisponiveis.append(peca)
            ii+=1
        if peca not in indisponiveis:
            inicio['monte'].append(peca)
    return inicio


#função que verifica o ganhador:
def verifica_ganhador(lista_pecas):
    for jogador, pecas in lista_pecas.items():
        if len(pecas)==0:
            return jogador
    return -1


#função que soma as peças do jogador:
def soma_pecas(pecas_do_jogador):
    soma = 0
    for pecas in pecas_do_jogador:
        for valor in pecas:
            soma+=valor
    return soma


#função que retorna as possíveis posições:
def posicoes_possiveis(mesa, pecas):
    posicoes = []
    if len(mesa)==0:
        i=0
        while i<len(pecas):
            posicoes.append(i)
            i+=1
        return posicoes
    ponta1 = mesa[0][0]
    ponta2 = mesa[-1][1]
    i=0
    while i<len(pecas):
        if pecas[i][0]==ponta1 or pecas[i][0]==ponta2 or pecas[i][1]==ponta1 or pecas[i][1]==ponta2:
            posicoes.append(i)
        i+=1
    return posicoes


#função que adiciona peças a mesa:
def adiciona_na_mesa(peca, mesa):
    if len(mesa)==0:
        mesa.append(peca)
        return mesa
    p1 = peca[0]
    p2 = peca[1]
    ponta1 = mesa[0][0]
    ponta2 = mesa[(len(mesa)-1)][1]
    if p1==ponta1:
        invertida = [p2, p1]
        mesa.insert(0, invertida)
        return mesa
    if p2==ponta1:
        mesa.insert(0, peca)
        return mesa
    if p1==ponta2:
        mesa.append(peca)
        return mesa
    if p2==ponta2:
        invertida = [p2, p1]
        mesa.append(invertida)
        return mesa


#função que retorna quem tem a maior peça para começar o jogo:
def quem_comeca(dic, n):
    i=6
    while i>=0:
        ii=0
        while ii<n:
            for peca in dic['jogadores'][ii]:
                if peca==[i, i]:
                    return ii
            ii+=1
        i-=1
