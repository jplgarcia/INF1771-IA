from Tkinter import *
from PIL import ImageTk, Image
import time

master = Tk()

w = Canvas(master, width=500, height=600)
rectSize = 40

imageWW = ImageTk.PhotoImage(Image.open("wwleste.gif"))
imageHole = ImageTk.PhotoImage(Image.open("buraco.png"))
imageFloor = ImageTk.PhotoImage(Image.open("chao.png"))
imageMonster20 = ImageTk.PhotoImage(Image.open("monstro20.gif"))
imageMonster50 = ImageTk.PhotoImage(Image.open("monstro50.gif"))

def insertMonsters(monsterList): #insere os monstros em suas respectivas posicoes no tabuleiro

    for monster in monsterList:
        ( x , y , damage ) = monster #(x,y): coordenadas de cada monstro, damage indica se o monstro tem dano de 20 ou 50
        if damage == 20:
            imagesprite = w.create_image(30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image=imageMonster20)
        else:
            imagesprite = w.create_image(30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image=imageMonster50)

def insertHoles(holeList): #funcao que insere buracos no tabuleiro baseado nas casas sorteadas

    for hole in holeList:
        ( x , y ) = hole
        imagesprite = w.create_image(30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageHole) # posicoes no tabuleiro sao de 0 a 11, e as recebidas de 1 a 12

def drawLines(): # desenha as linhas do tabuleiro
    i = 0
    while i < 12:
        j = 0
        while j < 12:
            w.create_rectangle(10 + rectSize * j, 50 + rectSize * (12 - i), 10 + rectSize * j + rectSize,
                               50 + rectSize * (12 - i) + rectSize, fill="", outline='black')
            j = j + 1
        i = i + 1

def drawFloor(): #desenha o chao do labirinto/tabuleiro

    i = 0
    while i < 12:
        j = 0
        while j < 12:
            imagesprite = w.create_image(30 + rectSize * j, 70 + rectSize * (12 - i), image=imageFloor) #insere imagem do chao no tabuleiro
            j = j + 1
        i = i + 1

def changeDirection(direction): #muda direcao da agente

    global imageWW

    if direction == "South":
        imageWW = ImageTk.PhotoImage(Image.open("wwsul.gif"))
    if direction == "North":
        imageWW = ImageTk.PhotoImage(Image.open("wwnorte.gif"))
    if direction == "East":
        imageWW = ImageTk.PhotoImage(Image.open("wwleste.gif"))
    if direction == "West":
        imageWW = ImageTk.PhotoImage(Image.open("wwoeste.gif"))


drawFloor()
insertHoles([(1,3),(3,3)])
insertMonsters([(2,2,20),(10,10,50)])
agentSprite = w.create_image(30 , 70 + rectSize * 12, image=imageWW)
drawLines()
w.pack()
master.mainloop()

time.sleep(2)
changeDirection("North")
imageWW = ImageTk.PhotoImage(Image.open("wwsul.gif"))
agentSprite = w.create_image(30 , 70 + rectSize * 12, image=imageWW)
master.mainloop()
#w.pack()
time.sleep(2)
changeDirection("East")
agentSprite = w.create_image(30 , 70 + rectSize * 12, image=imageWW)
#w.pack()
time.sleep(2)
changeDirection("South")
agentSprite = w.create_image(30 , 70 + rectSize * 12, image=imageWW)
#w.pack()
time.sleep(2)
changeDirection("West")
agentSprite = w.create_image(30 , 70 + rectSize * 12, image=imageWW)
#w.pack()
time.sleep(2)
changeDirection("South")
agentSprite = w.create_image(30 , 70 + rectSize * 12, image=imageWW)
#w.pack()
