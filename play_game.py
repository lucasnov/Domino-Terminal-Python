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


def formatador(lista):

    print('\n')

    for peca in lista:

        new = []
        
        for numero in peca:
            convert = '\033[1;3{}m{}\033[m'.format((numero+1),numero)
            new.append(convert)
        
        print ('{}|{}   '.format(new[0], new[1]), end="")

    print('\n')

    for i in range(0, len(lista)):

        print(' \033[;1m{}\033[m    '.format(i), end="")

    print('\n')


def formatador2(lista):

    print('\n')

    for peca in lista:

        new = []
        
        for numero in peca:
            convert = '\033[1;3{}m{}\033[m'.format((numero+1),numero)
            new.append(convert)
        
        print ('{}|{}  '.format(new[0], new[1]), end="")

    print('\n')


def formatador3(peca):

    new = []
        
    for numero in peca:
        convert = '\033[1;3{}m{}\033[m'.format((numero+1),numero)
        new.append(convert)
        
    print ('{}|{}'.format(new[0], new[1]), end="")



#código cores
#\033[1:31:40m vermelho fundo branco


#inicio do jogo
time.sleep(2)

print('\n')

time.sleep(2)

print('\033[1;31;47m------- O INCRÍVEL DOMINÓ -------\033[m')

print('\n')

time.sleep(2)

print('\033[1;31;47m-------- VAMOS COMEÇAR! --------\033[m')

time.sleep(2)

pecas_iniciais = cria_pecas()

numero_jogadores = int(input('\nInsira o número de adversários (1-3): '))

if numero_jogadores not in range(1, 4):

    while numero_jogadores not in range(1, 4):

        print('\nNúmero de jogadores inválido!')

        numero_jogadores = int(input('\nInsira o número de adversários (1-3): '))


print('\n')

time.sleep(2)

numero_jogadores+=1

inicio1 = inicia_jogo(numero_jogadores, pecas_iniciais)

jogador_inicial = quem_comeca(inicio1, numero_jogadores)

print('\033[1;31;47m-------- O JOGO COMEÇOU! --------\033[m')

time.sleep(2)

#Primeira jogada
if jogador_inicial==0:
    print('\nVocê começa!')

    time.sleep(2)

    print('\nSuas peças: ', end="")
    
    formatador(inicio1['jogadores'][jogador_inicial])

    time.sleep(2)

    peca_a_ser_jogada = int(input('\nEscolha a peça a ser jogada: '))-1

    time.sleep(2)
    
    possiveis = posicoes_possiveis(inicio1['mesa'], inicio1['jogadores'][jogador_inicial])

    if peca_a_ser_jogada not in possiveis:
        while peca_a_ser_jogada not in possiveis:
            peca_a_ser_jogada = int(input('\nEscolha entre as peças: '.format(possiveis)))-1

            time.sleep(2)
            
    print('\nVocê jogou a peça: ', end="")
    
    formatador3(inicio1['jogadores'][jogador_inicial][peca_a_ser_jogada])

    time.sleep(2)
    
    inicio1['mesa'] = adiciona_na_mesa(inicio1['jogadores'][jogador_inicial][peca_a_ser_jogada], inicio1['mesa'])

    inicio1['jogadores'][jogador_inicial].remove(inicio1['jogadores'][jogador_inicial][peca_a_ser_jogada])

    time.sleep(2)

    print('\n-----------------------------------------------')

    print('MESA ---> ', end="")
        
    formatador2(inicio1['mesa'])

    print('\nMONTE --> {} peças'.format(len(inicio1['monte'])))

    print('-----------------------------------------------')


else:
    print('\nJogador {} começa!'.format(jogador_inicial))

    time.sleep(2)

    peca_a_ser_jogada = random.choice(posicoes_possiveis(inicio1['mesa'], inicio1['jogadores'][jogador_inicial]))

    inicio1['mesa'] = adiciona_na_mesa(inicio1['jogadores'][jogador_inicial][peca_a_ser_jogada], inicio1['mesa'])

    print('\nJogador {} jogou a peça: '.format(jogador_inicial), end="")
    
    formatador3(inicio1['jogadores'][jogador_inicial][peca_a_ser_jogada])

    time.sleep(2)

    inicio1['jogadores'][jogador_inicial].remove(inicio1['jogadores'][jogador_inicial][peca_a_ser_jogada])

    print('\n-----------------------------------------------')

    print('MESA ---> ', end="")
        
    formatador2(inicio1['mesa'])

    print('\nMONTE --> {} peças'.format(len(inicio1['monte'])))

    print('------------------------------------------------')

    time.sleep(2)

    #Contador de jogadas passadas
passadas = [0]*numero_jogadores
empatou = False


#Repetidor de jogadores
if jogador_inicial==(numero_jogadores-1):
    i=0
else:
    i=jogador_inicial+1
while i<numero_jogadores:

    time.sleep(2)

    if i==0: #HUMANO JOGADOR
        
        print('\nSua vez!')

        time.sleep(2)

        print('\nSuas peças: ', end="")
        
        formatador(inicio1['jogadores'][i])

        time.sleep(2)

        possiveis = posicoes_possiveis(inicio1['mesa'], inicio1['jogadores'][i])

        
        if len(possiveis)==0:

            print('\nVocê não possui peças para jogar!')

            time.sleep(2)

            if len(inicio1['monte'])!=0:

                mensagem = input('\nPressione ENTER para pegar uma peça do monte! ')

                time.sleep(2)
                
                pegou_do_monte = random.choice(inicio1['monte'])

                print('\nVocê pegou a peça: ')
                
                formatador3(pegou_do_monte)

                time.sleep(2)

                inicio1['jogadores'][i].append(pegou_do_monte)

                inicio1['monte'].remove(pegou_do_monte)

                possiveis = posicoes_possiveis(inicio1['mesa'], inicio1['jogadores'][i])

                possiveis = possiveis+1

                if len(possiveis)==0:

                    if len(inicio1['monte'])==0:
                        
                        passadas[i]+=1
                    
                    print('\nJogador {} passou!'.format(i))
                    
                    time.sleep(2)

                else:

                    print('\nVocê jogará esta peça!')

                    time.sleep(2)

                    inicio1['mesa'] = adiciona_na_mesa(inicio1['jogadores'][i][-1], inicio1['mesa'])

                    print('\nVocê jogou a peça: ', end="")
                    
                    formatador3(inicio1['jogadores'][i][-1])

                    time.sleep(2)
                    
                    inicio1['jogadores'][i].remove(inicio1['jogadores'][i][-1])

                    passadas[i] = 0



            else:

                if len(inicio1['monte'])==0:
                    
                    passadas[i]+=1

                print('\nVocê passou!')
                    
                time.sleep(2)
                


        else:
            peca_a_ser_jogada = int(input('\nEscolha a peça a ser jogada: '))-1

            if peca_a_ser_jogada not in possiveis:
                while peca_a_ser_jogada not in possiveis:
                    print('\nPeça inválida!')    

                    time.sleep(2)

                    peca_a_ser_jogada = int(input('\nEscolha entre as peças {}: '.format(possiveis)))-1

                    time.sleep(2)
                
            inicio1['mesa'] = adiciona_na_mesa(inicio1['jogadores'][i][peca_a_ser_jogada], inicio1['mesa'])

            print('\nVocê jogou a peça: ', end="")
            
            formatador3(inicio1['jogadores'][i][peca_a_ser_jogada])

            time.sleep(2)
            
            inicio1['jogadores'][i].remove(inicio1['jogadores'][i][peca_a_ser_jogada])

            passadas[i] = 0

        time.sleep(2)

        print('\n-----------------------------------------------')

        print('MESA ---> ', end="")
        
        formatador2(inicio1['mesa'])

        print('\nMONTE --> {} peças'.format(len(inicio1['monte'])))

        print('-----------------------------------------------')

        time.sleep(2)


    else: #jogador bot
        print('\nVez do jogador {} -- {} peças'.format(i, len(inicio1['jogadores'][i])))

        time.sleep(2)

        possiveis = posicoes_possiveis(inicio1['mesa'], inicio1['jogadores'][i])

        if len(possiveis)==0:

            print('\nJogador {} não possui peças para jogar!'.format(i))

            time.sleep(2)

            if len(inicio1['monte'])!=0:

                print('\nJogador {} pegou uma peça do monte!'.format(i))

                time.sleep(2)
                
                pegou_do_monte = random.choice(inicio1['monte'])

                inicio1['jogadores'][i].append(pegou_do_monte)

                inicio1['monte'].remove(pegou_do_monte)

                possiveis = posicoes_possiveis(inicio1['mesa'], inicio1['jogadores'][i])

                if len(possiveis)==0:

                    if len(inicio1['monte'])==0:
                        
                        passadas[i]+=1
                    
                    print('\nJogador {} passou!'.format(i))
                    
                    time.sleep(2)

                else:

                    print('\nJogador {} jogará a peça que pegou do monte!'.format(i))

                    time.sleep(2)

                    inicio1['mesa'] = adiciona_na_mesa(inicio1['jogadores'][i][-1], inicio1['mesa'])

                    print('\nJogador {} jogou a peça:  '.format(i), end="")

                    formatador3(pegou_do_monte)

                    time.sleep(2)

                    inicio1['jogadores'][i].remove(inicio1['jogadores'][i][-1])

                    passadas[i] = 0

            else:

                if len(inicio1['monte'])==0:
                    
                    passadas[i]+=1

                print('\nNão há peças no monte!')

                time.sleep(2)

                print('\nJogador {} passou!'.format(i))
                    
                time.sleep(2)


        else: 

            peca_a_ser_jogada = random.choice(possiveis)

            inicio1['mesa'] = adiciona_na_mesa(inicio1['jogadores'][i][peca_a_ser_jogada], inicio1['mesa'])

            print('\nJogador {} jogou a peça: '.format(i), end="")
            
            formatador3(inicio1['jogadores'][i][peca_a_ser_jogada])

            time.sleep(2)

            inicio1['jogadores'][i].remove(inicio1['jogadores'][i][peca_a_ser_jogada])

            passadas[i] = 0

        
        time.sleep(2)

        print('\n-----------------------------------------------')

        print('MESA ---> ')
        
        formatador2(inicio1['mesa'])

        print('\nMONTE --> {} peças'.format(len(inicio1['monte'])))

        print('-----------------------------------------------')

        time.sleep(2)

    jogo_continua = verifica_ganhador(inicio1['jogadores'])

    if jogo_continua != -1:
        ganhador = i
        break

    if len(inicio1['monte'])==0:
        ii=0
        while ii<numero_jogadores:
            if passadas[ii]==1:
                empatou = True
            else:
                empatou = False
                break
            ii+=1

    if empatou==True:
        break

    if i==numero_jogadores-1:
        i=0
    else:
        i+=1

print('\n\033[1;31;47mFim de Jogo!\033[m')

time.sleep(2)

if empatou==True:

    print('\nO jogo trancou! Temos um Empate!')

    time.sleep(2)

    iii=0
    menor = 100000
    while iii<numero_jogadores:
        soma = soma_pecas(inicio1['jogadores'][iii])
        if soma<menor:
            menor = soma
            vencedor = iii
        iii+=1
    
    if vencedor==0:
        
        print('\nParabéns! Você venceu por ter a menor soma de pontos nas peças!')

        time.sleep(2)

    else:

        print('\nNão foi dessa vez! Jogador {} venceu por ter a menor soma de pontos nas peças!'.format(vencedor))

        time.sleep(2)

else:
    if ganhador==0:

        print('\nParabéns! Você venceu!')

    else:
        print('\nNão foi dessa vez! O jogador {} é o vencedor!'.format(ganhador))
