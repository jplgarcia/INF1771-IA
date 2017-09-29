import sys
from random import random,seed,randint,shuffle
import time
from math import exp
from copy import deepcopy
import os
""""""
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

def selectTSP(cwd):

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
			word = line.split(' ')[0]
			if word == "EOF":
				file.close()
				return (testname,testlist)
			else:
				start_temp = word
				alpha = line.split(' ')[1]
				exaust = line.split(' ')[2]
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
def create_initial_solution ( dimension ):

	initial_solution = []

	for i in range ( 0, dimension, 1 ):
		initial_solution.append( i )

	shuffle(initial_solution)

	return initial_solution

def route_distance ( distance_matrix , cities ): # calcula a distancia do percurso

	total = 0
	num_cities = len(cities)

	for i in range(num_cities):
		j = ( i + 1 ) % num_cities
		city_i = cities [ i ]
		city_j = cities [ j ]

		total = total + distance_matrix [ city_i ][ city_j ]

	return total

def swap(cities):
	l = len(cities)-1
	n1 = randint(0,l)
	n2 = randint(0,l)
	while n1==n2:
		n2 = randint(0,l)
	new = deepcopy(cities)
	new[n1] = cities[n2]
	new[n2] = cities[n1]
	return new
"""def flip(cities):
	l = len(cities) - 1
	n1 = randint(0, l-1)
	n2 = randint(n1, l)
	new = deepcopy(cities)
	i =n1
	for n in range(n2,n1):
		new[i] = cities[n]
		i+=1
	return new"""
def getRandomNeighbour(solution):
	return swap(solution)
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

		#visita a cada vizinho
		while not swaped:
			#pede novo vizinho aleatório
			solution = getRandomNeighbour(current)
			solution_eval = route_distance(matrix,solution)
			#avaliação do vizinho com a solução atual
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
	seed(1)
	cwd = os.getcwd()
	selectedTSP = selectTSP(cwd)
	matrix, dimension = readTSP(selectedTSP)
	for line in matrix:
		print (line)
	testname,alltestparams = read_AnnealingParams(cwd+"/AnnealingParams/"+sys.argv[1])
	"""Falta ler o arquivo de params do annealing"""
	print (testname)
	for testparams in alltestparams:
		print(testparams)
		(best, best_eval, start_temp, temp, alpha, elapsed_time) =\
					simulated_annealing(int(testparams[0]),float(testparams[1]),int(testparams[2]),matrix, dimension)
		writeTSP(cwd, selectedTSP, best_eval, best)
		print(testparams)
		print(best_eval,"\n", best)
