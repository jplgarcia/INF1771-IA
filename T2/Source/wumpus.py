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
prolog.consult("main.pl")

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

def fillFile(currentWorkingDirectory, world) : #escreve em um novo arquivo a melhor solucao e sua distancia
    pos_x = -1
    pos_y = -1
    #inserir pocos no prolog
    for list in world:
        pos_y = pos_y + 1
        pos_x = -1
        for item in list:
            pos_x = pos_x+1
            if item == 'PC':
                prolog.assertz("at(hole, pos("+str(pos_x+1)+","+str(pos_y+1)+"))")
                #file.write("pit("+str(pos_x+1)+","+str(pos_y+1)+").\n")
            if item == 'M1':
                prolog.assertz("at(monster01, pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
            if item == 'M2':
                prolog.assertz("at(monster02, pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
            if item == 'M3':
                prolog.assertz("at(monster03, pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")
            if item == 'M4':
                prolog.assertz("at(monster04, pos(" + str(pos_x + 1) + "," + str(pos_y + 1) + "))")

cwd = os.getcwd()
fillFile(cwd, world)

print list(prolog.query("at(monster01,X)"))
print list(prolog.query("at(hole,Y)"))
print list(prolog.query("at(breeze,X)"))

for list in world:
    print list