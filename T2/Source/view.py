from Tkinter import *
from PIL import ImageTk, Image
import time

master = Tk()

#carrega todas as imagens usadas no tabuleiro
imageWWFace = ImageTk.PhotoImage(Image.open("Imagens/WWface.jpg"))
imageWW = ImageTk.PhotoImage(Image.open("Imagens/wwleste.gif"))
imageHole = ImageTk.PhotoImage(Image.open("Imagens/buraco.png"))
imageFloor = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
imageGold = ImageTk.PhotoImage(Image.open("Imagens/ouro.gif"))
imageMonster1 = ImageTk.PhotoImage(Image.open("Imagens/monstro20.gif"))
imageMonster2 = ImageTk.PhotoImage(Image.open("Imagens/monstro20.gif"))
imageMonster3 = ImageTk.PhotoImage(Image.open("Imagens/monstro50.gif"))
imageMonster4 = ImageTk.PhotoImage(Image.open("Imagens/monstro50.gif"))
imageMonster1Face = ImageTk.PhotoImage(Image.open("Imagens/monstro20.gif"))
imageMonster2Face = ImageTk.PhotoImage(Image.open("Imagens/monstro20.gif"))
imageMonster3Face = ImageTk.PhotoImage(Image.open("Imagens/monstro50.gif"))
imageMonster4Face = ImageTk.PhotoImage(Image.open("Imagens/monstro50.gif"))

baseRow = 0

#infocanvas
infoCanvas = Canvas ( master, width = 500, height = 600 )
infoCanvas.place ( anchor = NW )

infoCanvas.create_rectangle(3,40,220,125)
infoCanvas.create_rectangle(3,135,220,212)
infoCanvas.create_rectangle(3,212,220,289)
infoCanvas.create_rectangle(3,289,220,366)
infoCanvas.create_rectangle(3,366,220,443)

infoCanvas.create_image(45, 82, image = imageWWFace)

#cria secao para pontuacoes, energia e flechas
labelPoints = Label ( master, text = "Pontos : " )
labelNumPoints = Label ( master, text = "0" )
labelPoints.grid ( row = 0 + baseRow , column = 1, sticky = "W" , pady = (40,0), padx=(100,0))
labelNumPoints.grid ( row = 0 + baseRow, column = 2, sticky = "W" , pady = (40,0), padx=(0,0))

labelEnergy = Label ( master, text = "Energia : " )
labelNumEnergy = Label ( master, text = "100" )
labelEnergy.grid ( row = 1 + baseRow , column = 1, sticky ="W" , padx=(100,0))
labelNumEnergy.grid ( row = 1 + baseRow, column = 2, sticky ="W" , padx=(0,0))

labelAmmo = Label ( master, text = "Flechas : " )
labelNumAmmo = Label ( master, text = "5" )
labelAmmo.grid ( row = 2  + baseRow, column = 1, sticky = "W" , padx=(100,0))
labelNumAmmo.grid ( row = 2 + baseRow, column = 2, sticky = "W" , padx=(0,0))

#Informacao do Monstro 1 (dano 20)
infoCanvas.create_image ( 45, 170, image = imageMonster1Face )
labelM1 = Label ( master, text = "Monstro 1 : ", )
labelM1Energy = Label ( master, text = "Energia : " )
labelM1NumEnergy = Label ( master, text = "100" )
labelM1Damage = Label ( master, text = "Dano : " )
labelM1NumDamage = Label ( master, text = "20" )
labelM1.grid ( row = 8 + baseRow, column = 1, columnspan = 2, sticky = "W", padx=(100,0) )
labelM1Energy.grid ( row = 9 + baseRow, column = 1, sticky = "W", padx=(100,0) )
labelM1NumEnergy.grid ( row = 9 + baseRow, column = 2, sticky = "W", padx=(0,0) )
labelM1Damage.grid ( row = 10 + baseRow, column = 1, sticky = "W", padx=(100,0) )
labelM1NumDamage.grid ( row = 10 + baseRow, column = 2, sticky = "W", padx=(0,0) )

#Informacao do Monstro 2 (dano 20)
infoCanvas.create_image ( 45, 255, image = imageMonster2Face )
labelM2 = Label ( master, text = "Monstro 2 : ")
labelM2Energy = Label ( master, text = "Energia : " )
labelM2NumEnergy = Label ( master, text = "100" )
labelM2Damage = Label ( master, text = "Dano : " )
labelM2NumDamage = Label ( master, text = "20" )
labelM2.grid ( row = 11 + baseRow, column = 1, columnspan = 2, sticky = "W", padx=(100,0) )
labelM2Energy.grid ( row = 12 + baseRow, column = 1, sticky = "W", padx=(100,0) )
labelM2NumEnergy.grid ( row = 12 + baseRow, column = 2, sticky = "W", padx=(0,0) )
labelM2Damage.grid ( row = 13 + baseRow, column = 1, sticky = "W", padx=(100,0) )
labelM2NumDamage.grid ( row = 13 + baseRow, column = 2, sticky = "W", padx=(0,0) )

#Informacao do Monstro 3 (dano 50)
infoCanvas.create_image ( 45, 330, image = imageMonster3Face )
labelM3 = Label ( master, text = "Monstro 3 : " )
labelM3Energy = Label ( master, text = "Energia : " )
labelM3NumEnergy = Label ( master, text = "100" )
labelM3Damage = Label ( master, text = "Dano : " )
labelM3NumDamage = Label ( master, text = "50" )
labelM3.grid( row = 14 + baseRow, column = 1, columnspan = 2 , sticky = "W", padx=(100,0) )
labelM3Energy.grid ( row = 15 + baseRow, column = 1, sticky = "W", padx=(100,0) )
labelM3NumEnergy.grid ( row = 15 + baseRow, column = 2, sticky = "W", padx=(0,0) )
labelM3Damage.grid ( row = 16 + baseRow, column = 1, sticky = "W", padx=(100,0) )
labelM3NumDamage.grid ( row = 16 + baseRow, column = 2, sticky = "W", padx=(0,0) )

#Informacao do Monstro 4 (dano 50)
infoCanvas.create_image ( 45, 400, image = imageMonster4Face )
labelM4 = Label ( master, text = "Monstro 4 : ")
labelM4Energy = Label ( master, text = "Energia : " )
labelM4NumEnergy = Label ( master, text = "100" )
labelM4Damage = Label ( master, text = "Dano : " )
labelM4NumDamage = Label ( master, text = "50" )
labelM4.grid( row = 17 + baseRow, column = 1, columnspan = 2 , sticky = "W", padx=(100,0) )
labelM4Energy.grid ( row = 18 + baseRow, column = 1 , sticky = "W", padx=(100,0) )
labelM4NumEnergy.grid ( row = 18 + baseRow, column = 2 , sticky = "W", padx=(0,0) )
labelM4Damage.grid ( row = 19 + baseRow, column = 1 , sticky = "W", padx=(100,0) )
labelM4NumDamage.grid ( row = 19 + baseRow, column = 2 , sticky = "W", padx=(0,0) )



boardCanvas = Canvas ( master, width = 500, height = 550) #tamanho do tabuleiro
rectSize = 40 #cada casa do tabuleiro tem 40 x 40 px

def insertMonsters ( monsterList ) : #insere os monstros em suas respectivas posicoes no tabuleiro

    global imagespriteMonster01, imagespriteMonster02, imagespriteMonster03, imagespriteMonster04

    for monster in monsterList:
        ( x , y , id ) = monster #(x,y): coordenadas de cada monstro, id 1 e 2 tem dano 20 e 3 e 4 dano 50
        if id == 1:
            boardCanvas.imagespriteMonster01 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster1 )
        elif id == 2:
            boardCanvas.imagespriteMonster02 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster2 )
        elif id == 3:
            boardCanvas.imagespriteMonster03 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster3 )
        elif id == 4:
            boardCanvas.imagespriteMonster04 = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageMonster4 )

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
                                           rectSize * (12 - i) + rectSize, fill = "", outline = 'black')
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
    # para cada direcao da agente, a foto atualiza para faze-la virar nessa direcao.
    if direction == "South":
        imageWW = ImageTk.PhotoImage(Image.open("Imagens/wwsul.gif"))
    if direction == "North":
        imageWW = ImageTk.PhotoImage(Image.open("Imagens/wwnorte.gif"))
    if direction == "East":
        imageWW = ImageTk.PhotoImage(Image.open("Imagens/wwleste.gif"))
    if direction == "West":
        imageWW = ImageTk.PhotoImage(Image.open("Imagens/wwoeste.gif"))

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

def retrieveGold ( x, y ) : #tira ouro da posicao em que o agente recolheu

    imagesprite = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageFloor )
    drawLines()
    master.update()

def movement () : #executa os movimentos da agente
    #acessar o arquivo wumpus.py que acessa o prolog para determinar movimentos
    """
    true_condition = TRUE
    do
        #Aqui deve Ficar o loop de avisa o q ta sentindo e perguta o q fazer, certo?
    while(true_condition)

    """
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
    retrieveGold(2,7)
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

    global labelM1NumEnergy, labelM2NumEnergy, labelM3NumEnergy, labelM4Energy, imageMonster1, imageMonster2, imageMonster3, imageMonster4

    if monster == 01 :
        total = int ( labelM1NumEnergy ["text"] ) - value
        labelM1NumEnergy.config ( text = str ( total ) )
        # se a energia do monstro ficar igual ou menor que 0, ele morre e sai do tabuleiro
        if total <= 0 :
            imageMonster1 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
            master.update()

    if monster == 02:
        total = int ( labelM2NumEnergy ["text"] ) - value
        labelM2NumEnergy.config ( text = str ( total ) )
        if total <= 0 :
            imageMonster2 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))

            master.update()

    if monster == 03:
        total = int ( labelM3NumEnergy ["text"] ) - value
        labelM3NumEnergy.config ( text = str ( total ) )
        if total <= 0 :
            imageMonster3 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
            master.update()

    if monster == 04:
        total = int ( labelM4NumEnergy ["text"] ) - value
        labelM4NumEnergy.config ( text = str ( total ) )
        if total <= 0 :
            imageMonster4 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
            master.update()

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
boardCanvas.grid (row=0, column = 7, rowspan = 50, columnspan = 8, padx=(30,0) )

#botao para iniciar a simulacao
button = Button ( master, text = "Start", command = lambda: movement() )
button.grid ( columnspan = 20, pady = ( 0 , 10 ) )

master.mainloop()

