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

dimension = 12

#Criar mundo
world = [['  ' for x in range(dimension)] for y in range(dimension)]

#Criar agente
agent = agent.Agent((0,0),(0,1))
world[0][0] = 'AG'

#criar montros
(x,y) = getFreeSpace(world)
monster01 = monster.Monster(1,20,x,y)
world[x][y] = 'M1'

(x,y) = getFreeSpace(world)
monster02 = monster.Monster(1,20,x,y)
world[x][y] = 'M2'

(x,y) = getFreeSpace(world)
monster03 = monster.Monster(1,50,x,y)
world[x][y] = 'M3'

(x,y) = getFreeSpace(world)
monster04 = monster.Monster(1,50,x,y)
world[x][y] = 'M4'

#criar pocos
i = 0
while i < 8:
    (x,y) = getFreeSpace(world)
    world[x][y] = 'PC'
    i = i + 1

def writeFile(currentWorkingDirectory, world) : #escreve em um novo arquivo a melhor solucao e sua distancia
    filename = currentWorkingDirectory + "/rules.pl"
    file = open(filename, 'w')
    file.write("agent(1,1).\n")
    pos_x = -1
    pos_y = -1
    #inserir pocos no prolog
    for list in world:
        pos_y = pos_y + 1
        pos_x = -1
        for item in list:
            pos_x = pos_x+1
            if item == 'PC':
                file.write("pit("+str(pos_x+1)+","+str(pos_y+1)+").\n")
    #inserir monstros no prolog
    for list in world:
        pos_y = pos_y + 1
        pos_x = -1
        for item in list:
            pos_x = pos_x+1
            if item == 'M1' or item == 'M2' or item == 'M3' or item == 'M4':
                file.write("monster(" + str(pos_x + 1) + "," + str(pos_y + 1) + ").\n")

    file.close()

cwd = os.getcwd()
writeFile(cwd, world)

prolog = Prolog()
prolog.consult("rules.pl")
print list(prolog.query("pit(X,Y)"))
print list(prolog.query("monster(X,Y)"))
print bool(list(prolog.query("agent(1,1)")))
for list in world:
    print list