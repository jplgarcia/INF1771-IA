import sys
from random import random, shuffle, randint
import time
from math import exp
import os
#import hillclimbing as hc

""""""
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
    cost = str(cost) + '\n'
    filename = currentWorkingDirectory + "/result_" + splittedTSP[(len(splittedTSP) - 1)]
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

    for number in range ( 1 , length , 1 ) : # range comeca no 1 pq a cidade inicial precisa continuar na mesma posicao
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

def getRandomNeighbour(neighborhood):
	return neighborhood[randint(0,len(neighborhood)-1)]

def read_AnnealingParams(paramsfile):
	path = paramsfile
	try:
		file = open(path,"r")
	except IOError:
		print("Erro: file not opened --read_AnnealingParams ")

	began_reading_params = False
	testlist = []
	for line in file:
		if not began_reading_params:
			word = line.split(' ')[0]
			if word == "NAME":
				testname =  line.split(" ")[1]
			elif word == "PARAMS":
				began_reading_params=True
		else:
			linewords = []
			for word in line.split():
				if word == '' or word == ' ':
					continue
				linewords.append(word)
			word = line.split(' ')[0]
			if word == "EOF":
				file.close()
				return (testname,testlist)
			else:
				start_temp = linewords[0]
				alpha = linewords[1]
				exaust = linewords[2]
				#print (start_temp,alpha,exaust)
				testlist.append((start_temp,alpha,exaust.strip('\n')))
	file.close()

"""
	kirkpatrick_cooling(start_temp, alpha)
	0 < alpha < 1
"""
def kirkpatrick_cooling(start_temp, alpha):
	t = start_temp
	while True:
		yield t
		t = alpha * t
"""
	funcao p() retorna uma probabilidade P 0<P<=1
"""
def p(delta,temp):
	return exp(-delta/temp)

"""
	-A chance de aceitar um vizinho pior diminui a cada solucao que se aceita
	-exaustion_criteria eh o numero de vizinhos que o algoritmo tem que avaliar antes de parar
"""
def simulated_annealing(start_temp,alpha,exaustion_criteria, matrix , dimension):
	start_time = time.time()
	current = create_initial_solution(dimension)
	current_eval = route_distance(matrix,current)
	best = current
	best_eval = current_eval
	"""
		cooling_schedule representa uma diminuicao da temperatura inversamente proporcional ao tempo gasto
		
	"""
	cooling_schedule = kirkpatrick_cooling(start_temp,alpha)

	#a cada temperatura, visita-se vizinhos ate trocar com um deles
	for temp in cooling_schedule:

		#swaped permite a iteracao no conjunto dos vizinhos numa mesma temperatura
		swaped = False

		comparisions = 1
		#Ao otimizar SimAnn, eh essa referencia que deve ser afetada
		neighborhood = create_neighbourhood(current)

		#visita a cada vizinho
		while not swaped:
			#pede novo vizinho aleatorio
			solution = getRandomNeighbour(neighborhood)
			solution_eval = route_distance(matrix,solution)
			#avaliacao do vizinho com a solucao atual
			delta_eval = solution_eval - current_eval
			if delta_eval<0:
				current = solution
				current_eval = solution_eval
				if current_eval<best_eval:
					best = current
					best_eval = current_eval
				swaped = True
				continue
			elif delta_eval>0:
				if random() < p(abs(delta_eval),temp):
					current = solution
					current_eval = solution_eval
					swaped = True
					#print("Accepted!!!")
					continue

			comparisions+=1
			if comparisions >= exaustion_criteria:
				elapsed_time = time.time()-start_time
				#print("Comparisions = " + str(comparisions))
				return best,best_eval,start_temp,temp,alpha,elapsed_time
		#print("Comparisions = "+str(comparisions)+"\tEval"+str(current_eval)+"\tTemp:"+str(temp))

if __name__ =="__main__":
	cwd = os.getcwd()
	selectedTSP = hc.selectTSP(cwd)
	matrix, dimension = hc.readTSP(selectedTSP)
	for line in matrix:
		print (line)
	testname,alltestparams = read_AnnealingParams(cwd+"/AnnealingParams/"+sys.argv[1])
	"""Falta ler o arquivo de params do annealing"""
	for testparams in alltestparams:
		print(testparams)
		(best, best_eval, start_temp, temp, alpha, elapsed_time) =\
					simulated_annealing(int(testparams[0]),float(testparams[1]),int(testparams[2]),matrix, dimension)
		hc.writeTSP(cwd, selectedTSP, best_eval, best)

def runSimulatedAnneling(chosen_tsp, chosen_params):
	cwd = os.getcwd()
	selectedTSP = selectTSP(cwd, chosen_tsp)
	matrix, dimension = readTSP(selectedTSP)

	testname, alltestparams = read_AnnealingParams(cwd + "/AnnealingParams/" + chosen_params)
	"""Falta ler o arquivo de params do annealing"""
	for testparams in alltestparams:
		print(testparams)
		(best, best_eval, start_temp, temp, alpha, elapsed_time) = \
			simulated_annealing(int(testparams[0]), float(testparams[1]), int(testparams[2]), matrix, dimension)
		writeTSP(cwd, selectedTSP, best_eval, best)

	return (best_eval, best, elapsed_time, matrix, start_temp, temp, alpha)