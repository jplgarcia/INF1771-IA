from pyswip import Prolog, registerForeign
import monster
import agent
import random

def hello(t):
    print "Hello,", t
hello.arity = 1

def getFreeSpace(world):
    x = 0
    y = 0

    while world[x][y] != '  ':
        x = random.randint(0,11)
        y = random.randint(0,11)
    return (x,y)


registerForeign(hello)

prolog = Prolog()
prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")
list(prolog.query("father(michael,X), hello(X)"))

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

for list in world:
    print list

