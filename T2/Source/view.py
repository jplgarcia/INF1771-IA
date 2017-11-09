from Tkinter import *
from PIL import ImageTk, Image
import time

master = Tk()

w = Canvas ( master , width=500 , height=600 )
rectSize = 40

#carrega todas as imagens usadas no tabuleiro
imageWW = ImageTk.PhotoImage(Image.open("wwleste.gif"))
imageHole = ImageTk.PhotoImage(Image.open("buraco.png"))
imageFloor = ImageTk.PhotoImage(Image.open("chao.png"))
imageGold = ImageTk.PhotoImage(Image.open("ouro.gif"))
imageMonster20 = ImageTk.PhotoImage(Image.open("monstro20.gif"))
imageMonster50 = ImageTk.PhotoImage(Image.open("monstro50.gif"))

def insertMonsters ( monsterList ) : #insere os monstros em suas respectivas posicoes no tabuleiro

    for monster in monsterList:
        ( x , y , damage ) = monster #(x,y): coordenadas de cada monstro, damage indica se o monstro tem dano de 20 ou 50
        if damage == 20:
            imagesprite = w.create_image ( 30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageMonster20 )
        else:
            imagesprite = w.create_image ( 30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageMonster50 )

def insertHoles ( holeList ) : #funcao que insere buracos no tabuleiro baseado nas casas sorteadas

    for hole in holeList:
        ( x , y ) = hole
        imagesprite = w.create_image ( 30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageHole ) # posicoes no tabuleiro sao de 0 a 11, e as recebidas de 1 a 12

def insertGold ( goldList ) : #insere ouros no tabuleiro

    for gold in goldList :
        (x,y) = gold #lista contem posicao x,y de cada ouro
        imagesprite = w.create_image ( 30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageGold )

def drawLines () : # desenha as linhas do tabuleiro

    i = 0
    while i < 12: # i e j sao as linhas e colunas do tabuleiro, que tem dimensao de 12 x 12
        j = 0
        while j < 12:
            w.create_rectangle ( 10 + rectSize * j, 50 + rectSize * (12 - i), 10 + rectSize * j + rectSize,
                               50 + rectSize * (12 - i) + rectSize, fill="", outline='black' )
            j = j + 1
        i = i + 1

def drawFloor () : #desenha o chao do labirinto/tabuleiro

    i = 0
    while i < 12:
        j = 0
        while j < 12:
            imagesprite = w.create_image(30 + rectSize * j, 70 + rectSize * (12 - i), image=imageFloor) #insere imagem do chao no tabuleiro em cada casa
            j = j + 1
        i = i + 1

def changeDirection ( direction, position ) : #muda direcao da agente em sua respectiva posicao no tabuleiro

    global imageWW
    global agentSprite

    ( x , y ) = position
    #para cada direcao da agente, a foto atualiza para faze-la virar nessa direcao.
    if direction == "South":
        imageWW = ImageTk.PhotoImage(Image.open("wwsul.gif"))
    if direction == "North":
        imageWW = ImageTk.PhotoImage(Image.open("wwnorte.gif"))
    if direction == "East":
        imageWW = ImageTk.PhotoImage(Image.open("wwleste.gif"))
    if direction == "West":
        imageWW = ImageTk.PhotoImage(Image.open("wwoeste.gif"))

    # posiciona imagem com a direcao correta na casa onde a agente se encontra.
    agentSprite = w.create_image( 30 + rectSize * ( x - 1 ), 70 + rectSize * ( 12 - ( y - 1 ) ), image = imageWW )

def movement () :
    #acessar o arquivo wumpus.py que acessa o prolog para determinar movimentos
    time.sleep(0.5)
    changeDirection("East",(2,1))
    master.update()
    time.sleep(0.5)
    changeDirection("East", (3, 1))
    master.update()
    time.sleep(0.5)
    changeDirection("North", (3, 1))
    master.update()
    time.sleep(0.5)
    changeDirection("North", (3, 2))
    master.update()
    time.sleep(0.5)
    changeDirection("East", (3, 2))
    master.update()
    time.sleep(0.5)
    changeDirection("East", (4, 2))
    master.update()
    time.sleep(0.5)
    changeDirection("North", (5, 2))
    master.update()
    time.sleep(0.5)
    changeDirection("South", (5, 2))
    master.update()



drawFloor()
insertHoles([(1,3),(3,3)])
insertGold([(2,7),(5,6),(10,9)])
insertMonsters([(2,2,20),(10,10,50)])
agentSprite = w.create_image(30 , 70 + rectSize * 12, image = imageWW)
drawLines()
w.pack()


button = Button ( master, text = "Start", command = lambda: movement() )
button.pack()


master.mainloop()

