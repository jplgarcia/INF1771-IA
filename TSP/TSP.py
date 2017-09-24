from random import shuffle
import sys


class TSP_Task:
	def read_TSPmatrix(self,tspfile):
		path = tspfile
		file = open(path, "r")
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
		def swap(solution, first_city_number, second_city_number):  # funcao que troca duas cidades

			aux = solution[first_city_number]
			solution[first_city_number] = solution[second_city_number]
			solution[second_city_number] = aux

			return solution
		#Classe Neighbour-------------------------------------------------
		class Neighbourhood:
			def __init__(self, solution):
				length = len(solution) - 1
				neighbours = []

				for number in range(0, length, 1):
					if (number == 0):  # a cidade inicial precisa continuar na mesma posicao
						continue
					if (number == length):
						break
					temporary_solution = solution[:]
					new_neighbour = solution.swap(temporary_solution, number, number + 1)
					neighbours.append(new_neighbour)

				return neighbours
		#FIM--Classe Neighbour-------------------------------------------------

		def __init__(self):
			pass

		def create_neighbourhood(self):
			return self.Neighbourhood(self)

		def random_solution(self,task):
			initial_solution = []

			for i in range(0, task.dimension, 1):
				initial_solution.append(i)

			shuffle(initial_solution)

			return initial_solution
	#FIM--Classe Solution------------------------------------------------------
	def create_initial_solution(self):
		self.Solution.random_solution(self)

	def route_distance(self, cities):  # calcula a distancia do percurso

		total = 0
		num_cities = len(cities)

		for i in range(num_cities):
			j = (i + 1) % num_cities
			city_i = cities[i]
			city_j = cities[j]

			total += self.problem_matrix[city_i][city_j]

		return total


if __name__=="__main__":
	path = sys.argv[1]
	task = TSP_Task(path)
