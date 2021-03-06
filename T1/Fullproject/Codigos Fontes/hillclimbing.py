from random import shuffle, seed
import os
import time


def selectTSP(cwd, filename):

    cwd = cwd + "/TSP/"
    fullpathfile = cwd + filename
    return fullpathfile


def readTSP(selectedTSP): #le o arquivo do TSP e salva em uma matriz de distancias

    file = open(selectedTSP, 'r')
    lines = []
    i = 0
    matrixLine = 0
    matrixColumn = 0

    for line in file:
        item = line.strip(' \t\r\n')
        lines.append(item)

    length = len(lines)

    while (lines[i] != "EDGE_WEIGHT_SECTION"):
        splitted = lines[i].split(' ')
        splittedLine = splitted[0]
        if (splittedLine == "DIMENSION:"):
            dimension = splitted[1]
            dimension = int(dimension)
        elif (splittedLine == "EDGE_WEIGHT_FORMAT:"):
            edge_format = splitted[1]
        i = i + 1

    if 'dimension' in locals():
        if (dimension > 0):
            i = i + 1
            matrix = [[0 for x in range(dimension)] for y in range(dimension)]
            contador_inicial_x = 0
            contador_inicial_y = 0
            x = 0
            y = -1
            while (i < length - 1):
                line = lines[i].split(' ')
                for word in line:
                    if (word == ''):
                        continue
                    if (edge_format == "UPPER_DIAG_ROW"): #trata da matriz upper diagonal
                        if (int(word) == 0):
                            y += 1
                        matrix[x][y] = int(word)
                        matrix[y][x] = int(word)
                        x += 1
                        if (x == dimension):
                            contador_inicial_x += 1
                            x = contador_inicial_x
                    else: # lower diagonal
                        matrix[matrixLine][matrixColumn] = int(word)
                        matrix[matrixColumn][matrixLine] = int(word)
                        matrixLine = matrixLine + 1
                    if (word == "0"):
                        matrixColumn = matrixColumn + 1
                        matrixLine = 0

                i = i + 1
    file.close()

    return matrix, dimension


def writeTSP(currentWorkingDirectory, selectedTSP, cost, route) : #escreve em um novo arquivo a melhor solucao e sua distancia
    splittedTSP = selectedTSP.split('/')
    dirResult = currentWorkingDirectory + "/resultados/"
    if not os.path.exists(dirResult):
        os.makedirs(dirResult)
    splittedTSP = splittedTSP[(len(splittedTSP) - 1)]
    splittedTSP = splittedTSP.split('.')
    splittedTSP = splittedTSP[0]
    splittedTSP = splittedTSP + ".sol"
    cost = str(cost) + '\n'
    filename = dirResult + "/result_hill_climbing_" + splittedTSP
    file = open(filename, 'w')
    file.write(cost)
    for city in route:
        city = str(city) + ' '
        file.write(city)
    file.close()


def route_distance ( distance_matrix , cities ): # calcula a distancia do percurso

    total = 0
    num_cities = len(cities)

    for i in range(num_cities):
        j = ( i + 1 ) % num_cities
        city_i = cities [ i ]
        city_j = cities [ j ]

        total = total + distance_matrix [ city_i ][ city_j ]

    return total

def evaluate_neighbours ( distance_matrix , neighbours ): # seleciona o melhor vizinho (com a menor distancia)

    shortest_distance = 0
    best_neighbour = []

    for neighbour in neighbours:
        distance = route_distance( distance_matrix , neighbour )
        if shortest_distance == 0:
            shortest_distance = distance
            best_neighbour = neighbour
        elif distance < shortest_distance:
            shortest_distance = distance
            best_neighbour = neighbour

    return ( best_neighbour, shortest_distance )


def swap ( solution, first_city_number , second_city_number ): #funcao que troca duas cidades

    aux = solution[first_city_number]
    solution[first_city_number] = solution[second_city_number]
    solution[second_city_number] = aux

    return solution


def create_neighbourhood ( initial_solution ) : # gera a vizinhanca de solucoes a partir de uma solucao inicial

    length = len ( initial_solution ) - 1
    neighbours = [ initial_solution ]

    for number in range ( 0 , length , 1 ) : # range comeca no 1 pq a cidade inicial precisa continuar na mesma posicao
        if ( number == length ):
            break
        temporary_solution = initial_solution[:]
        new_neighbour = swap ( temporary_solution, number , number + 1 )
        neighbours.append ( new_neighbour )

    return neighbours

def create_initial_solution ( dimension ): #cria uma solucao inicial aleatoria

    initial_solution = []

    for i in range ( 0, dimension, 1 ):
        initial_solution.append( i )

    shuffle(initial_solution)

    return initial_solution


def hill_climbing ( matrix , dimension ) :

    initial_solution = create_initial_solution ( dimension )
    neighbourhood = create_neighbourhood ( initial_solution )
    ( best_neighbour , distance ) = evaluate_neighbours( matrix , neighbourhood )
    #seed(1) #Para o hillclimb comum basta escolher uma seed arbitraria para termos sempre o mesmo shuffle
    while best_neighbour != initial_solution : 
        initial_solution = best_neighbour
        neighbourhood = create_neighbourhood ( initial_solution )
        ( best_neighbour, distance ) = evaluate_neighbours ( matrix , neighbourhood )

    return best_neighbour, distance

def single_hill_climbing ( matrix , dimension ):
    seed(432790) #escolha de uma seed arbitraria para o shuffle(criacao da solucao inicial)
    return hill_climbing( matrix, dimension)

def random_starts_hill_climbing ( matrix , dimension ): #hill climbing que exige um numero fixo de iteracoes para aceitar a melhor solucao

    iterations = 0
    best_solution = []
    shortest_distance = 0
    limit = 1000/dimension # numero de iteracoes reduz de acordo com o numero de cidades
    if limit < 1: # caso teste com um TSP com mais de 1000 cidades ira rodar apenas uma vez
        limit = 1
    while iterations < (limit) :
        #para cada start usamos uma seed diferentes que vai de 0 ate dimension
        seed(iterations+ 432790) #escolha de uma seed arbitraria para o shuffle(criacao da solucao inicial)
        if shortest_distance == 0 :
            ( best_solution , shortest_distance ) = hill_climbing ( matrix , dimension )
        else :
            ( new_solution , new_distance ) = hill_climbing ( matrix , dimension )
            if new_distance < shortest_distance:
                shortest_distance = new_distance
                best_solution = new_solution
                print (seed)
        iterations = iterations + 1

    return best_solution, shortest_distance


def runForCommomHillClimb(chosen_tsp):

    cwd = os.getcwd()
    selectedTSP = selectTSP(cwd, chosen_tsp)
    matrix, dimension = readTSP(selectedTSP)

    one_go_start_time = time.time()
    ( best_neighbor, distance ) = single_hill_climbing ( matrix , dimension )
    print (best_neighbor, distance)
    time_complete = time.time() - one_go_start_time
    print("time completed:")
    print(time_complete)
    writeTSP(cwd, selectedTSP, distance, best_neighbor)
    return (distance, best_neighbor, time_complete, matrix)

def runForMultipleSeedsHillClimb(chosen_tsp):

    cwd = os.getcwd()
    selectedTSP = selectTSP(cwd, chosen_tsp)
    matrix, dimension = readTSP(selectedTSP)

    random_tries_start_time = time.time()
    ( best_neighbor, distance ) = random_starts_hill_climbing ( matrix , dimension )
    print(best_neighbor, distance)
    time_complete = time.time() - random_tries_start_time
    print("time completed:")
    print(time_complete)
    writeTSP(cwd, selectedTSP, distance, best_neighbor)
    return (distance, best_neighbor, time_complete, matrix)
