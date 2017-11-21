from Tkinter import *
from PIL import ImageTk, Image
import time
import wumpus

master = Tk()

# Carrega todas as imagens usadas no tabuleiro
# Imagens de encontram na pasta Imagens
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

# Variavel utilizada para alinhamento do grid
# a interface grafica utiliza o modo grid do tkinter
# necessario uma fileira(row) base para alinhamento dos elementos graficos
baseRow = 0

# infocanvas
# O quadro onde fica desenhado o rosto da agente, fotos dos monstros e informacoes sobre eles
# Necessario criar um canvas para podermos desenhar os contornos dos campos de informacoes e imagens
infoCanvas = Canvas ( master, width = 500, height = 600 )
infoCanvas.place ( anchor = NW )

infoCanvas.create_rectangle(3,40,220,125)  # Contorno das informacoes da agente
infoCanvas.create_rectangle(3,135,220,212) # Contorno das informacoes do monstro 1
infoCanvas.create_rectangle(3,212,220,289) # Contorno das informacoes do monstro 2
infoCanvas.create_rectangle(3,289,220,366) # Contorno das informacoes do monstro 3
infoCanvas.create_rectangle(3,366,220,443) # Contorno das informacoes do monstro 4

infoCanvas.create_image(45, 82, image = imageWWFace)

# Cria secao para pontuacoes, energia e flechas da agente
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

# Informacao do Monstro 1 (dano 20)
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

# Informacao do Monstro 2 (dano 20)
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

# Informacao do Monstro 3 (dano 50)
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

# Informacao do Monstro 4 (dano 50)
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
baseGoldList = []
baseHoleList = []

# Descricao: insere as imagens dos monstros no boardCanvas a partir de uma lista com tuplas
# tupla x,y,id definem coordenada cartesianas x,y e identificador do monstro
# Param: monsterList - lista com tuplas (x,y,id)
# Return: none
def insertMonsters ( monsterList ) :

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

# Descricao: insere as imagens dos buracos no boardCanvas a partir de uma lista com tuplas
# tupla x,y definem coordenada cartesianas x,y
# Param: holeList - lista com tuplas (x,y)
# Return: none
def insertHoles ( holeList ) : #funcao que insere buracos no tabuleiro baseado nas casas sorteadas
    global baseHoleList
    for hole in holeList:
        ( x , y ) = hole
        baseHoleList.append((x,y))
        # posicoes no tabuleiro sao de 0 a 11, e as recebidas de 1 a 12
        imagesprite = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageHole )


# Descricao: insere as imagens dos ouros no boardCanvas a partir de uma lista com tuplas
# tupla x,y definem coordenada cartesianas x,y
# Param: goldList - lista com tuplas (x,y)
# Return: none
def insertGold ( goldList ) : #insere ouros no tabuleiro

    for gold in goldList :
        (x,y) = gold #lista contem posicao x,y de cada ouro
        baseGoldList.append((x,y))
        imagesprite = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageGold )


# Descricao: insere as linhas no boardCanvas para definir limites dos quadrados
# Param: none
# Return: none
def drawLines () : # desenha as linhas do tabuleiro

    i = 0
    while i < 12: # i e j sao as linhas e colunas do tabuleiro, que tem dimensao de 12 x 12
        j = 0
        while j < 12:
            boardCanvas.create_rectangle (10 + rectSize * j,  rectSize * (12 - i), 10 + rectSize * j + rectSize,
                                           rectSize * (12 - i) + rectSize, fill = "", outline = 'black')
            j = j + 1
        i = i + 1

# Descricao: desenha quadrados referentes ao chao nas celulas de 1 a 12
# Param: none
# Return: none
def drawFloor () : #desenha o chao do labirinto/tabuleiro

    i = 0
    while i < 12:
        j = 0
        while j < 12:
            # insere imagem do chao no tabuleiro em cada casa
            imagesprite = boardCanvas.create_image ( 30 + rectSize * j, 20 + rectSize * (12 - i), image = imageFloor )
            j = j + 1
        i = i + 1

# Descricao: muda a direcao e a posicao da agente e redesenhas no tabuleiro no local e com posicao certa
# Param: direction: direcao North, South, East, West para onde o agente esta olhando
# Param: position: tupla (x,y) com coordenadas cartesianas referentes a posicao da agente
# Return: none
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

# Descricao: Cria uma mensgame pop up com mensagem costumizavel
# Param: msg: mensagem que sera exibida na pop up
# Return: none
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

# Descricao: retira ouro de uma posicao X Y
# Param: x: coordenada cartesiana X
# Param: y: coordenada cartesiana Y
# Return: none
def retrieveGold ( x, y ) : #tira ouro da posicao onde o agente recolheu

    imagesprite = boardCanvas.create_image ( 30 + rectSize * (x - 1), 20 + rectSize * (12 - (y - 1)), image = imageFloor )
    drawLines()
    master.update()

# Descricao: Acao ao apertar botao start
# Pergunta ao modulo wumpus.py a melhor acao a se tomar
# Recebe informcoes do prolog para chamar as funcoes auxiliares de atualizacao da interface
# Param: none
# Return: none
def movement () : #executa os movimentos da agente
    #acessar o arquivo wumpus.py que acessa o prolog para determinar movimentos
    while(True):
        gameData = wumpus.takeAction()

        dead = gameData['dead']
        score = gameData['score']
        energy = gameData['energy']
        position = gameData['position']
        facing = gameData['facing']
        ammo = gameData['ammo']
        goldList = gameData['goldList']

        monster1Energy = gameData['monster1']
        monster2Energy = gameData['monster2']
        monster3Energy = gameData['monster3']
        monster4Energy = gameData['monster4']

        print "score: " + str(score)
        print "energy: " + str(energy)
        print "ammo: " + str(ammo)
        print "position: " + str(position)
        print "facing: " + str(facing)
        print "goldList: " + str(goldList)

        print "monster 1: " + str(monster1Energy)
        print "monster 2: " + str(monster2Energy)
        print "monster 3: " + str(monster3Energy)
        print "monster 4: " + str(monster4Energy)

        facingDirection = "North"
        if facing == (1,0):
            facingDirection = "East"
        elif facing == (-1,0):
            facingDirection = "West"
        elif facing == (0,1):
            facingDirection = "North"
        elif facing == (0,-1):
            facingDirection = "South"

        updateAgentPoints(score)
        updateAgentEnergy(energy)
        updateAmmo(ammo)
        updateMonsterEnergy(monster1Energy, 1)
        updateMonsterEnergy(monster2Energy, 2)
        updateMonsterEnergy(monster3Energy, 3)
        updateMonsterEnergy(monster4Energy, 4)

        if position in baseGoldList:
            (x,y) = position
            retrieveGold(x,y)

        if position in baseHoleList:
            popUpMsg("You Lost!")
            break

        changeDirection(facingDirection, position)
        #boardCanvas.update()
        #infoCanvas.update()
        master.update()

        time.sleep(0.25)

        if energy <= 0 or dead:
            popUpMsg("You Lost!")
            break

        if score > 0 and position == (1,1):
            popUpMsg("You Won!")
            break


# Descricao: Atualiza a label pontos da agente
# Param: value: novo valor de pontos a ser estabelecido
# Return: none
def updateAgentPoints ( value ) : #muda pontuacao do agente

    global labelNumPoints

    #caso o valor recebido seja para diminuir do numero de pontos, ele vem com sinal negativo. Por isso, sempre somamos o valor.
    total = value
    labelNumPoints.config ( text = str ( total ) )


# Descricao: Atualiza a label energia da agente
# Param: value: novo valor de energia a ser estabelecido
# Return: none
def updateAgentEnergy ( value ) : #muda energia do agente

    global labelNumEnergy

    #o valor da energia sempre vem em modulo e e diminuita do numero total
    total =  value
    labelNumEnergy.config ( text = str ( total ) )


# Descricao: Atualiza a label energia do monstro especifico
# Param: value: novo valor de energia a ser estabelecido
# Param: monster: identificador do montro cuja label sera alterada
# Return: none
def updateMonsterEnergy ( value, monster ) : #muda energia do monstro

    global labelM1NumEnergy, labelM2NumEnergy, labelM3NumEnergy, labelM4Energy, imageMonster1, imageMonster2, imageMonster3, imageMonster4

    if monster == 01 :
        total =  value
        labelM1NumEnergy.config ( text = str ( total ) )
        # se a energia do monstro ficar igual ou menor que 0, ele morre e sai do tabuleiro
        if total <= 0 :
            imageMonster1 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
            master.update()

    if monster == 02:
        total = value
        labelM2NumEnergy.config ( text = str ( total ) )
        if total <= 0 :
            imageMonster2 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))

            master.update()

    if monster == 03:
        total = value
        labelM3NumEnergy.config ( text = str ( total ) )
        if total <= 0 :
            imageMonster3 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
            master.update()

    if monster == 04:
        total =  value
        labelM4NumEnergy.config ( text = str ( total ) )
        if total <= 0 :
            imageMonster4 = ImageTk.PhotoImage(Image.open("Imagens/chao.png"))
            master.update()


# Descricao: Atualiza a label municao da agente
# Param: value: novo valor de municao a ser estabelecido
# Return: none
def updateAmmo (value): #diminui municao, uma flecha por vez

    global labelNumAmmo

    total = value
    labelNumAmmo.config ( text = str ( total ) )

# Descricao: inicializa o tabuleiro chamando todas as funcoes necessaria para sua construcao
# Param: none
# Return: none
def initializeBoard() :
    drawFloor()
    insertHoles(wumpus.getHolePositions())
    insertGold(wumpus.getGoldPositions())
    insertMonsters(wumpus.getMonsterPositions())
    agentSprite = boardCanvas.create_image ( 30, 20 + rectSize * 12, image = imageWW )
    drawLines()
    boardCanvas.grid (row=0, column = 7, rowspan = 50, columnspan = 8, padx=(30,0) )
    #botao para iniciar a simulacao
    button = Button ( master, text = "Start", command = lambda: movement() )
    button.grid ( row = 100, columnspan = 20, pady = ( 0 , 10 ) )

initializeBoard()
master.mainloop()

