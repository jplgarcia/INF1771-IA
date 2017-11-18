from pyswip import Prolog
import monster
import agent
import random
import os

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

#Criar mundo
world = [['  ' for x in range(dimension)] for y in range(dimension)]

#Criar agente
agent = agent.Agent((0,0),(0,1))
world[0][0] = 'AG'

#criar monstros
(x,y) = getFreeSpace(world)
monster01 = monster.Monster(01,20,x,y)
world[x][y] = 'M1'

(x,y) = getFreeSpace(world)
monster02 = monster.Monster(02,20,x,y)
world[x][y] = 'M2'

(x,y) = getFreeSpace(world)
monster03 = monster.Monster(03,50,x,y)
world[x][y] = 'M3'

(x,y) = getFreeSpace(world)
monster04 = monster.Monster(04,50,x,y)
world[x][y] = 'M4'

#criar pocos
i = 0
while i < 8:
    (x,y) = getFreeSpace(world)
    world[x][y] = 'PC'
    i = i + 1

# criar ouros
i = 0
while i < 3:
    (x, y) = getFreeSpace(world)
    world[x][y] = 'GD'
    i = i + 1


def fillMap(world) : #escreve em um novo arquivo a melhor solucao e sua distancia
    pos_x = -1
    pos_y = -1
    #inserir pocos no prolog
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

fillMap(world)

for line in world:
    print line

def getMonsterPositions():
    prologMonsterList = list(prolog.query("at(monster(N),pos(X,Y))"))
    monsterList = []
    for monster in prologMonsterList:
        monsterList.append((monster['X'],monster['Y'],monster['N']))
    return monsterList

def getHolePositions():
    prologHoleList = list(prolog.query("at(hole,pos(X,Y))"))
    holeList = []
    for hole in prologHoleList:
        holeList.append((hole['X'], hole['Y']))
    return holeList

def getGoldPositions():
    prologGoldList = list(prolog.query("at(gold,pos(X,Y))"))
    goldList = []
    for gold in prologGoldList:
        goldList.append((gold['X'], gold['Y']))
    return goldList

def takeAction():


    queryString = "take_action()."
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
    pMonster1Energy =  list(prolog.query("energy(monster(01), X)"))
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



