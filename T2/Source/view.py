from Tkinter import *
from PIL import ImageTk, Image
import time

master = Tk()

#carrega todas as imagens usadas no tabuleiro
imageWWFace = ImageTk.PhotoImage(Image.open("WWface.jpg"))
imageWW = ImageTk.PhotoImage(Image.open("wwleste.gif"))
imageHole = ImageTk.PhotoImage(Image.open("buraco.png"))
imageFloor = ImageTk.PhotoImage(Image.open("chao.png"))
imageGold = ImageTk.PhotoImage(Image.open("ouro.gif"))
imageMonster20 = ImageTk.PhotoImage(Image.open("monstro20.gif"))
imageMonster50 = ImageTk.PhotoImage(Image.open("monstro50.gif"))

#insere rosto da agente para inserir ao lado da sua pontuacao
faceCanvas = Canvas ( master, width = 80, height = 80  )
WWfacesprite =  faceCanvas.create_image ( 45, 45, image = imageWWFace )
faceCanvas.grid ( row = 0, column = 0, rowspan = 6 )

#cria secao para pontuacoes, energia e flechas
labelPoints = Label ( master, text = "Pontos : " )
labelNumPoints = Label ( master, text = "0" )

labelPoints.grid ( row = 2 , column = 1, sticky = "W" )
labelNumPoints.grid ( row = 2, column = 2, sticky = "W" )

labelEnergy = Label ( master, text = "Energia : " )
labelNumEnergy = Label ( master, text = "100" )
labelEnergy.grid ( row = 3 , column = 1, sticky ="W" )
labelNumEnergy.grid ( row = 3, column = 2, sticky ="W" )

labelAmmo = Label ( master, text = "Flechas : " )
labelNumAmmo = Label ( master, text = "5" )
labelAmmo.grid ( row = 4 , column = 1, sticky = "W" )
labelNumAmmo.grid ( row = 4, column = 2, sticky = "W" )

#Energia do Monstro 1 (dano 20)
labelM1 = Label ( master, text = "Monstro 1 : ", pady = 5 )
labelM1Energy = Label ( master, text = "Energia : " )
labelM1NumEnergy = Label ( master, text = "100" )
labelM1Damage = Label ( master, text = "Dano : " )
labelM1NumDamage = Label ( master, text = "20" )
labelM1.grid ( row = 0, column = 3, columnspan = 2, sticky = "W" )
labelM1Energy.grid ( row = 1, column = 3, sticky = "W" )
labelM1NumEnergy.grid ( row = 1, column = 4, sticky = "W" )
labelM1Damage.grid ( row = 2, column = 3, sticky = "W" )
labelM1NumDamage.grid ( row = 2, column = 4, sticky = "W" )

#Energia do Monstro 2 (dano 20)
labelM2 = Label ( master, text = "Monstro 2 : ", pady = 5 )
labelM2Energy = Label ( master, text = "Energia : " )
labelM2NumEnergy = Label ( master, text = "100" )
labelM2Damage = Label ( master, text = "Dano : " )
labelM2NumDamage = Label ( master, text = "20" )
labelM2.grid ( row = 0, column = 5, columnspan = 2, sticky = "W" )
labelM2Energy.grid ( row = 1, column = 5, sticky = "W" )
labelM2NumEnergy.grid ( row = 1, column = 6, sticky = "W" )
labelM2Damage.grid ( row = 2, column = 5, sticky = "W" )
labelM2NumDamage.grid ( row = 2, column = 6, sticky = "W" )

#Energia do Monstro 3 (dano 50)
labelM3 = Label ( master, text = "Monstro 3 : ", pady = 5 )
labelM3Energy = Label ( master, text = "Energia : " )
labelM3NumEnergy = Label ( master, text = "100" )
labelM3Damage = Label ( master, text = "Dano : " )
labelM3NumDamage = Label ( master, text = "50" )
labelM3.grid( row = 3, column = 3, columnspan = 2 , rowspan=3, sticky = "W" )
labelM3Energy.grid ( row = 5, column = 3, sticky = "W" )
labelM3NumEnergy.grid ( row = 5, column = 4, sticky = "W" )
labelM3Damage.grid ( row = 6, column = 3, sticky = "W" )
labelM3NumDamage.grid ( row = 6, column = 4, sticky = "W" )

#Energia do Monstro 4 (dano 50)
labelM4 = Label ( master, text = "Monstro 4 : ", pady = 5)
labelM4Energy = Label ( master, text = "Energia : " )
labelM4NumEnergy = Label ( master, text = "100" )
labelM4Damage = Label ( master, text = "Dano : " )
labelM4NumDamage = Label ( master, text = "50" )
labelM4.grid( row = 3, column = 5, columnspan = 2 , rowspan=3, sticky = "W" )
labelM4Energy.grid ( row = 5, column = 5 , sticky = "W" )
labelM4NumEnergy.grid ( row = 5, column = 6 , sticky = "W" )
labelM4Damage.grid ( row = 6, column = 5 , sticky = "W" )
labelM4NumDamage.grid ( row = 6, column = 6 , sticky = "W" )

boardCanvas = Canvas ( master, width = 500, height = 550 ) #tamanho do tabuleiro
rectSize = 40 #cada casa do tabuleiro tem 40 x 40 px

imagespriteMonster01 = None
imagespriteMonster02 = None
imagespriteMonster03 = None
imagespriteMonster04 = None


def insertMonsters ( monsterList ) : #insere os monstros em suas respectivas posicoes no tabuleiro

    global imagespriteMonster01, imagespriteMonster02, imagespriteMonster03, imagespriteMonster04

    for monster in monsterList:
        ( x , y , id ) = monster #(x,y): coordenadas de cada monstro, id 1 e 2 tem dano 20 e 3 e 4 dano 50
        if id == 1:
            boardCanvas.imagespriteMonster01 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster20 )
        elif id == 2:
            boardCanvas.imagespriteMonster02 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster20 )
        elif id == 3:
            boardCanvas.imagespriteMonster03 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster50 )
        elif id == 4:
            boardCanvas.imagespriteMonster04 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster50 )

def insertHoles ( holeList ) : #funcao que insere buracos no tabuleiro baseado nas casas sorteadas

    for hole in holeList:
        ( x , y ) = hole
        # posicoes no tabuleiro sao de 0 a 11, e as recebidas de 1 a 12
        imagesprite = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageHole )

def insertGold ( goldList ) : #insere ouros no tabuleiro

    for gold in goldList :
        (x,y) = gold #lista contem posicao x,y de cada ouro
        imagesprite = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageGold )

def drawLines () : # desenha as linhas do tabuleiro

    i = 0
    while i < 12: # i e j sao as linhas e colunas do tabuleiro, que tem dimensao de 12 x 12
        j = 0
        while j < 12:
            boardCanvas.create_rectangle (10 + rectSize * j,  rectSize * (12 - i), 10 + rectSize * j + rectSize,
                                           rectSize * (12 - i) + rectSize, fill="", outline='black')
            j = j + 1
        i = i + 1

def drawFloor () : #desenha o chao do labirinto/tabuleiro

    i = 0
    while i < 12:
        j = 0
        while j < 12:
            # insere imagem do chao no tabuleiro em cada casa
            imagesprite = boardCanvas.create_image ( 30 + rectSize * j, 20 + rectSize * (12 - i), image = imageFloor )
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
    agentSprite = boardCanvas.create_image(30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageWW)

def popUpMsg ( msg ) : #abre um pop up com Game Over

    popup = Tk()

    popup.wm_title ( "Game Over!" )
    label = Label ( popup, text = msg ) #a mensagem indica se o agente ganhou ou perdeu
    label.pack ( side = "top", fill = "x", padx = 50, pady = (10,0) )
    label = Label ( popup, text = "Score : " + labelNumPoints [ "text" ] ) #imprime pontuacao final do agente
    label.pack ( side  = "top", fill = "x", padx = 50 )

    B1 = Button ( popup, text = "Okay", command = lambda: [ master.destroy(), popup.destroy() ] )
    B1.pack()
    popup.geometry ( '%dx%d+%d+%d' % ( 200, 90, 150 ,300 ) )

    popup.mainloop()

def movement () : #executa os movimentos da agente
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
    updateAgentPoints(10)
    updateAgentEnergy(10)
    updateAmmo()
    updateMonsterEnergy(100,01)
    popUpMsg("Game Over!")

def updateAgentPoints ( value ) : #muda pontuacao do agente

    global labelNumPoints

    #caso o valor recebido seja para diminuir do numero de pontos, ele vem com sinal negativo. Por isso, sempre somamos o valor.
    total = int ( labelNumPoints [ "text" ] ) + value
    labelNumPoints.config ( text = str ( total ) )

def updateAgentEnergy ( value ) : #muda energia do agente

    global labelNumEnergy

    #o valor da energia sempre vem em modulo e e diminuita do numero total
    total = int ( labelNumEnergy [ "text" ] ) - value
    labelNumEnergy.config ( text = str ( total ) )

def updateMonsterEnergy ( value, monster ) : #muda energia do monstro

    global labelM1NumEnergy, labelM2NumEnergy, labelM3NumEnergy, labelM4Energy

    if monster == 01 :
        total = int ( labelM1NumEnergy ["text"] ) - value
        labelM1NumEnergy.config ( text = str ( total ) )
        #if total <= 0 :
            #boardCanvas.imagespriteMonster01.config(image='')
    if monster == 02:
        total = int ( labelM2NumEnergy ["text"] ) - value
        labelM2NumEnergy.config ( text = str ( total ) )
    if monster == 03:
        total = int ( labelM3NumEnergy ["text"] ) - value
        labelM3NumEnergy.config ( text = str ( total ) )
    if monster == 04:
        total = int ( labelM4NumEnergy ["text"] ) - value
        labelM4NumEnergy.config ( text = str ( total ) )



def updateAmmo (): #diminui municao, uma flecha por vez

    global labelNumAmmo

    total = int ( labelNumAmmo [ "text" ] ) - 1
    labelNumAmmo.config ( text = str ( total ) )


drawFloor()
insertHoles([(1,3),(3,3),(1,12),(2,5),(7,11),(7,8),(4,4),(7,7)])
insertGold([(2,7),(5,6),(10,9)])
insertMonsters([(2,2,1), (3,10,2),(10,10,3),(5,5,4)])
agentSprite = boardCanvas.create_image ( 30, 20 + rectSize * 12, image = imageWW )
drawLines()
boardCanvas.grid ( columnspan = 8 )

#botao para iniciar a simulacao
button = Button ( master, text = "Start", command = lambda: movement() )
button.grid ( columnspan = 8, pady = ( 0, 20 ) )

master.mainloop()

