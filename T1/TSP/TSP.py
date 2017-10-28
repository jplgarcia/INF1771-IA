from random import shuffle
import sys
import random as rdm
from copy import deepcopy
from SimulatedAnnealing import SimulatedAnnealing as SA

class TSP_Task:
	def read_TSPmatrix(self,tspfile):
		path = tspfile
		try:
			file = open(path,"r")
		except IOError:
			print("Erro: file not opened --read_TSPmatrix ")
		count = 0
		dimension = 0
		i = 0
		j = 0

		beganReadingMatrix = False
		for line in file:
			if (not beganReadingMatrix):
				word = line.split(':')[0]
				if word == "DIMENSION":
					dimension = line.split(":")[1]
					print(dimension)
					matrix = [[0 for x in range(int(dimension))] for y in range(int(dimension))]
				elif word == "EDGE_WEIGHT_FORMAT":
					format = line.split(":")[1]
				elif word == "EDGE_WEIGHT_SECTION" or word == "EDGE_WEIGHT_SECTION\n":
					beganReadingMatrix = True
			else:
				lineArray = line.split(' ')
				for word in lineArray:
					if (word == '' or word == 'EOF' or word == 'EOF\n'):
						continue
					matrix[i][j] = int(word)
					matrix[j][i] = int(word)
					i += 1
					if int(word) == 0:
						i = 0
						j += 1
		file.close()
		return matrix, dimension

	def __init__(self,tspfile):
		self.problem_matrix,self.dimension = self.read_TSPmatrix(tspfile)
	#Classe Solution------------------------------------------------------
	class Solution:
		def swap(self, first_city_number, second_city_number):  # funcao que troca duas cidades

			aux = self.cities[first_city_number]
			self.cities[first_city_number] = self.cities[second_city_number]
			self.cities[second_city_number] = aux
		#Classe Neighbour-------------------------------------------------
		class Neighbourhood:
			def __init__(self, sol):
				solution = sol.cities
				length = len(solution) - 1
				self.curr = 0
				self.neighbours = []

				for number in range(0, length, 1):
					if (number == 0):  # a cidade inicial precisa continuar na mesma posicao
						continue
					if (number == length):
						break
					#temporary_solution = solution[:]
					new_neighbour = deepcopy(sol)
					new_neighbour.swap(number, number + 1)
					self.neighbours.append(new_neighbour)
			def getNeighborhood(self):
				return self.neighbours
			def getRandom(self):
				return self.neighbours[rdm.randint(0,len(self.neighbours)-1)]

		#FIM--Classe Neighbourhood-------------------------------------------------
		def __init__(self,cities):
			self.cities = cities

		def create_neighbourhood(self):
			return self.Neighbourhood(self)

		def random_solution(self):
			initial_solution = []

			for i in range(0, int(self.dimension), 1):
				initial_solution.append(i)

			shuffle(initial_solution)

			return self.Solution(initial_solution)

	#FIM--Classe Solution------------------------------------------------------
	def eval(self,solution):  # calcula a distancia do percurso

		total = 0
		num_cities = len(solution.cities)

		for i in range(num_cities):
			j = (i + 1) % num_cities
			city_i = solution.cities[i]
			city_j = solution.cities[j]

			total += self.problem_matrix[city_i][city_j]

		return total

	def create_initial_solution(self):
		return self.Solution.random_solution(self)




if __name__=="__main__":
	HasAnnFile = True
	path = sys.argv[1]
	print (str(sys.argv[1]))
	task = TSP_Task(path)

	#SIM_ANN começa aqui --------------------------------------
	try:
		print(str(sys.argv[2]))
	except IndexError:
		HasAnnFile = False
		print("No Ann_Params file passed")
	if HasAnnFile:
		ann_testname,ann_testparams = read_AnnealingParams(sys.argv[2])
		print("\n\t"+str(ann_testname))
		for testparams in ann_testparams:
			print("\t\t("+testparams[0]+","+testparams[1]+","+testparams[2]+")")
			(best, best_eval, start_temp, temp, alpha, elapsed_time) =\
				SA.simulated_annealing(task,int(testparams[0]),float(testparams[1]),int(testparams[2]))
			print("\t\tBest = "+str(best.cities)+" with eval = "+str(best_eval))
			print("\t\tStarting Temp = "+str(start_temp)+"; End Temp = "+str(temp))
			print("\t\tElapsed Time"+str(elapsed_time))
			break
	# SIM_ANN termina aqui --------------------------------------