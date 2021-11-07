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
