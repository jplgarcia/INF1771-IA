from Tkinter import *
from PIL import ImageTk, Image
import time

master = Tk()

faceCanvas = Canvas ( master, width = 80, height = 80  )
imageWWFace = ImageTk.PhotoImage(Image.open("WWface.jpg"))
WWfacesprite =  faceCanvas.create_image ( 45, 45, image = imageWWFace)
faceCanvas.grid ( row = 0, column = 0, rowspan = 3 )

#cria secao para pontuacoes, energia e flecha
labelPoints = Label ( master, text = "Pontos : " )
labelNumPoints = Label ( master, text = "0" )

labelPoints.grid ( row = 0 , column = 1 )
labelNumPoints.grid ( row = 0, column = 2 )

labelEnergy = Label ( master, text = "Energia : " )
labelNumEnergy = Label ( master, text = "100" )
labelEnergy.grid ( row = 1 , column = 1 )
labelNumEnergy.grid ( row = 1, column = 2 )

labelAmmo = Label ( master, text = "Flechas : " )
labelNumAmmo = Label ( master, text = "5" )
labelAmmo.grid ( row = 2 , column = 1 )
labelNumAmmo.grid ( row = 2, column = 2 )


boardCanvas = Canvas ( master, width = 500, height = 600 ) #tamanho do tabuleiro
rectSize = 40 #cada casa do tabuleiro tem 40 x 40 px

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
            imagesprite = boardCanvas.create_image (30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageMonster20)
        else:
            imagesprite = boardCanvas.create_image (30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageMonster50)

def insertHoles ( holeList ) : #funcao que insere buracos no tabuleiro baseado nas casas sorteadas

    for hole in holeList:
        ( x , y ) = hole
        # posicoes no tabuleiro sao de 0 a 11, e as recebidas de 1 a 12
        imagesprite = boardCanvas.create_image (30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageHole)

def insertGold ( goldList ) : #insere ouros no tabuleiro

    for gold in goldList :
        (x,y) = gold #lista contem posicao x,y de cada ouro
        imagesprite = boardCanvas.create_image (30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageGold)

def drawLines () : # desenha as linhas do tabuleiro

    i = 0
    while i < 12: # i e j sao as linhas e colunas do tabuleiro, que tem dimensao de 12 x 12
        j = 0
        while j < 12:
            boardCanvas.create_rectangle (10 + rectSize * j, 50 + rectSize * (12 - i), 10 + rectSize * j + rectSize,
                                          50 + rectSize * (12 - i) + rectSize, fill="", outline='black')
            j = j + 1
        i = i + 1

def drawFloor () : #desenha o chao do labirinto/tabuleiro

    i = 0
    while i < 12:
        j = 0
        while j < 12:
            # insere imagem do chao no tabuleiro em cada casa
            imagesprite = boardCanvas.create_image ( 30 + rectSize * j, 70 + rectSize * (12 - i), image = imageFloor )
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
    agentSprite = boardCanvas.create_image(30 + rectSize * (x - 1), 70 + rectSize * (12 - (y - 1)), image = imageWW)

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
agentSprite = boardCanvas.create_image(30, 70 + rectSize * 12, image = imageWW)
drawLines()
boardCanvas.grid ( columnspan = 5 )


button = Button ( master, text = "Start", command = lambda: movement() )
button.grid ( columnspan = 5, pady = (0,40) )


master.mainloop()

