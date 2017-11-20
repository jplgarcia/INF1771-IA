from pyswip import Prolog
import monster
import agent
import random
import os

# Descricao: busca aleatoriamente uma posicao vaga no mundo
# Uma posicao vaga nao esta ocupada por nada
# Param: world - Matriz contendo as informacoes PC = poco, M1,M2,M3,M4=monstros e GD = ouro
# Return: Tupla com posicao vaga (x, y) como coordenadas cartesianas
def getFreeSpace(world):
    x = 0
    y = 0

    while world[x][y] != '  ':
        x = random.randint(0,11)
        y = random.randint(0,11)
    return (x,y)

prolog = Prolog()
prolog.consult("run.pl")

dimension = 12

startedRunning = False

#Criar mundo como uma matriz dimension x dimension (12x12)
world = [['  ' for x in range(dimension)] for y in range(dimension)]

#Criar agente inserindo ele na casa 1,1
world[0][0] = 'AG'

#criar monstros colocando-os em locais aleatorios
(x,y) = getFreeSpace(world)
world[x][y] = 'M1'

(x,y) = getFreeSpace(world)
world[x][y] = 'M2'

(x,y) = getFreeSpace(world)
world[x][y] = 'M3'

(x,y) = getFreeSpace(world)
world[x][y] = 'M4'

#criar pocos colocando-os em locais aleatorios
i = 0
while i < 8:
    (x,y) = getFreeSpace(world)
    world[x][y] = 'PC'
    i = i + 1

# criar ouros colocando-os em locais aleatorios
i = 0
while i < 3:
    (x, y) = getFreeSpace(world)
    world[x][y] = 'GD'
    i = i + 1

# Descricao: preenche o prolog atraves de asserts.
# As informacoes a serem passadas dos prolog vem de uma matriz NxN
# Apos a insercao de cada buraco insere as brizas, apos cada monstro insere os fedores
# prolog.assertz() faz uma assertiva no prolog
# at(obj, pos(X,Y)) - obj(hole, gold, monster, breeze, stench) na posicao (X,Y) cartesiana
# Param: world - Matriz contendo as informacoes PC = poco, M1,M2,M3,M4=monstros e GD = ouro
# Return: none
def fillMap(world) :
    pos_x = -1
    pos_y = -1
    for line in world:
        pos_y = pos_y + 1
        pos_x = -1
        for item in line:
            pos_x = pos_x+1
            if item == 'PC':
                prolog.assertz("at(hole, pos("+str(pos_x+1)+","+str(pos_y+1)+"))")
                if (pos_x < 11):
                    prolog.assertz("at(breeze, pos(" + str(pos_x + 2) + "," + str(pos_y + 1) + "))")
                if (pos_x > 0):
                    prolog.assertz("at(breeze, pos(" + str(pos_x) + "," + str(pos_y + 1) + "))")
                if (pos_y < 11):
                    prolog.assertz("at(breeze, pos(" + str(pos_x + 1) + "," + str(pos_y + 2) + "))")
                if (pos_y > 0):
                    prolog.assertz("at(breeze, pos(" + str(pos_x + 1) + "," + str(pos_y) + "))")
            elif item == 'M1' or item == 'M2' or item == 'M3' or item == 'M4':
                if item == 'M1':
                    prolog.assertz("at(monster(1), pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
                elif item == 'M2':
                    prolog.assertz("at(monster(2), pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
                elif item == 'M3':
                    prolog.assertz("at(monster(3), pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
                elif item == 'M4':
                    prolog.assertz("at(monster(4), pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
                if (pos_x < 11):
                    prolog.assertz("at(stench, pos(" + str(pos_x + 2) + "," + str(pos_y + 1) + "))")
                if (pos_x > 0):
                    prolog.assertz("at(stench, pos(" + str(pos_x) + "," + str(pos_y + 1) + "))")
                if (pos_y < 11):
                    prolog.assertz("at(stench, pos(" + str(pos_x + 1) + "," + str(pos_y + 2) + "))")
                if (pos_y > 0):
                    prolog.assertz("at(stench, pos(" + str(pos_x + 1) + "," + str(pos_y) + "))")
            elif item == 'GD':
                prolog.assertz("at(gold, pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")

#Chamada da funcao fillMap para preencher o prolog com as informacoes antes colocadas na matriz
fillMap(world)

for line in world:
    print line

# Descricao: busca no prolog onde estao os monstros e faz um parse da lista
# prolog.query() faz uma busca no prolog
# at(monster(N), pos(X,Y)) - monstro de identificador N na posicao (X,Y) cartesiana
# Param: nenhum
# Return: lista com tuplas(X,Y,N) onde x,y sao posicoes cartesianas e n o identificador do monstro
def getMonsterPositions():
    prologMonsterList = list(prolog.query("at(monster(N),pos(X,Y))"))
    monsterList = []
    for monster in prologMonsterList:
        monsterList.append((monster['X'],monster['Y'],monster['N']))
    return monsterList

# Descricao: busca no prolog onde estao os buracos e faz um parse da lista
# prolog.query() faz uma busca no prolog
# at(hole, pos(X,Y)) - hole na posicao (X,Y) cartesiana
# Param: nenhum
# Return: lista com tuplas(X,Y) onde x,y sao posicoes cartesianas
def getHolePositions():
    prologHoleList = list(prolog.query("at(hole,pos(X,Y))"))
    holeList = []
    for hole in prologHoleList:
        holeList.append((hole['X'], hole['Y']))
    return holeList

# Descricao: busca no prolog onde estao os ouros e faz um parse da lista
# prolog.query() faz uma busca no prolog
# at(gold, pos(X,Y)) - gold na posicao (X,Y) cartesiana
# Param: nenhum
# Return: lista com tuplas(X,Y) onde x,y sao posicoes cartesianas
def getGoldPositions():
    prologGoldList = list(prolog.query("at(gold,pos(X,Y))"))
    goldList = []
    for gold in prologGoldList:
        goldList.append((gold['X'], gold['Y']))
    return goldList

# Descricao: Chama a funcao take_action() do prolog para executar a melhor acao possivel
# Em seguida busca um conjunto de informacoes do prolog, faz o parse delas para um dicionario
# Devolte esse dicionario como resultado da funcao
# {
#   'score': pontuacao do personagem/agente/mulhermaravilha,
#   'energy': ponto de energia do personegem/agente/mulhermaravilha,
#   'ammo': municao restante usada para atacar monstros,
#   'position': posicao em coordenada cartesianas (x,y) onde o agente se encontra,
#   'facing': tupla de coordenadas cartesianas (x,y) para onde o agente esta olhando,
#   'goldList': tupla de coordenadas cartesianas (x,y) onde existem ouros,
#   'monster1': pontos de energia do monstro 1,
#   'monster2': pontos de energia do monstro 2,
#   'monster3': pontos de energia do monstro 3,
#   'monster4': pontos de energia do monstro 4,
# }
# Param: nenhum
# Return: dicionario contendo informacoes acima
def takeAction():
    global startedRunning
    if not startedRunning:
        print list(prolog.query("check_surrounding_and_current_position."))
        startedRunning = True

    queryString = "take_action."
    print queryString
    print list(prolog.query(queryString))

    #pega informacao do prolog sobre o agente
    pScore = list(prolog.query("score(agent, X)"))
    pEnergy = list(prolog.query("energy(agent, X)"))
    pAmmo = list(prolog.query("ammo(X)"))
    pPosition = list(prolog.query("at(agent,pos(X,Y))"))
    pFacing = list(prolog.query("agentfacing(X, Y)"))
    pGoldList = list(prolog.query("at(gold, pos(X,Y))"))

    #pega informacao do prolog sobre os monstros
    pMonster1Energy = list(prolog.query("energy(monster(01), X)"))
    pMonster2Energy = list(prolog.query("energy(monster(02), X)"))
    pMonster3Energy = list(prolog.query("energy(monster(03), X)"))
    pMonster4Energy = list(prolog.query("energy(monster(04), X)"))

    score = pScore[0]['X']
    energy = pEnergy[0]['X']
    position = (pPosition[0]['X'], pPosition[0]['Y'])
    facing = (pFacing[0]['X'], pFacing[0]['Y'])
    ammo = pAmmo[0]['X']

    goldlist = []
    for item in pGoldList:
        (x,y) = (item['X'],item['Y'])
        goldlist.append((x,y))

    monster1Energy = pMonster1Energy[0]['X']
    monster2Energy = pMonster2Energy[0]['X']
    monster3Energy = pMonster3Energy[0]['X']
    monster4Energy = pMonster4Energy[0]['X']

    #junta os dados para enviar para view.py
    gameData = {'score': score, 'energy': energy, 'ammo': ammo, 'position': position, 'facing': facing,'goldList': goldlist  , 'monster1':monster1Energy, 'monster2': monster2Energy, 'monster3': monster3Energy, 'monster4':monster4Energy}

    return gameData


print list(prolog.query("at(Name,pos(X,Y))"))