from random import shuffle
from random import randint
import os


def selectTSP(cwd):

	cwd = cwd + "/TSP/"
	filesname = os.listdir(cwd)

	i = 1

	print("Select an option: ")
	for file in filesname:
		if file.endswith(".tsp"):
			option = "\t" + str(i) + " - " + file
			print(option)
			i = i + 1
	selectedoption = eval(raw_input())
	fullpathfile = cwd + filesname[selectedoption - 1]

	return fullpathfile


def readTSP(selectedTSP):

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
				print(line)
				for word in line:
					if (word == ''):
						continue
					if (edge_format == "UPPER_DIAG_ROW"):
						if (int(word) == 0):
							y += 1
						matrix[x][y] = int(word)
						matrix[y][x] = int(word)
						x += 1
						if (x == dimension):
							contador_inicial_x += 1
							x = contador_inicial_x
					else:
						matrix[matrixLine][matrixColumn] = int(word)
						matrix[matrixColumn][matrixLine] = int(word)
						matrixLine = matrixLine + 1
					if (word == "0"):
						matrixColumn = matrixColumn + 1
						matrixLine = 0

				i = i + 1
	file.close()

	return matrix, dimension


def writeTSP(currentWorkingDirectory, selectedTSP, cost, route) :

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
def getRandomNeighbour(neighborhood):
	return neighborhood[randint(0,len(neighborhood)-1)]

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
		neighbours.append(new_neighbour)

	return neighbours

def create_initial_solution ( dimension ):

	initial_solution = []

	for i in range ( 0, dimension, 1 ):
		initial_solution.append( i )

	shuffle(initial_solution)

	return initial_solution


def hill_climbing ( matrix , dimension ) :

	initial_solution = create_initial_solution ( dimension )
	neighbourhood = create_neighbourhood ( initial_solution )
	( best_neighbour , distance ) = evaluate_neighbours( matrix , neighbourhood )

	while best_neighbour != initial_solution :
		initial_solution = best_neighbour
		neighbourhood = create_neighbourhood ( initial_solution )
		( best_neighbour, distance ) = evaluate_neighbours ( matrix , neighbourhood )

	return best_neighbour, distance


def altered_hill_climbing ( matrix , dimension ): #hill climbing que exige um numero fixo de iteracoes para aceitar a melhor solucao

	iterations = 0
	best_solution = []
	shortest_distance = 0

	while iterations < 10 :
		if shortest_distance == 0 :
			( best_solution , shortest_distance ) = hill_climbing ( matrix , dimension )
		else :
			( new_solution , new_distance ) = hill_climbing ( matrix , dimension )
			if new_distance < shortest_distance:
				shortest_distance = new_distance
				best_solution = new_solution
		iterations = iterations + 1

	return best_solution, shortest_distance

cwd = os.getcwd()
selectedTSP = selectTSP(cwd)
matrix, dimension = readTSP(selectedTSP)
for line in matrix:
	print (line)

( best_neighbor, distance ) = hill_climbing ( matrix , dimension )
print (best_neighbor, distance)

( best_neighbor, distance ) = altered_hill_climbing ( matrix , dimension )
print (best_neighbor, distance)

writeTSP(cwd, selectedTSP, distance, best_neighbor)
