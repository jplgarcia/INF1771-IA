from random import random
import time
from math import exp
import os
from HillClimbing import hillclimbing as hc
def selectPARAMS(cwd):

	cwd = cwd+"/AnnealingParams/"
	filesname = os.listdir(cwd)

	i = 1

	print("Select an option: ")
	for file in filesname:
		if file.endswith(".txt"):
			option = "\t" + str(i) + " - " + file
			print(option)
			i = i + 1
	selectedoption = eval(raw_input())
	fullpathfile = cwd + filesname[selectedoption - 1]

	return fullpathfile

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
				testlist.append((start_temp,alpha,exaust.strip('\n')))
	file.close()

"""
	kirkpatrick_cooling(start_temp, alpha)
	0 < alpha < 1
	Essa implementação foi encontrada em 
	http://www.psychicorigami.com/2007/06/28/tackling-the-travelling-salesman-problem-simmulated-annealing/
"""
def kirkpatrick_cooling(start_temp, alpha):
	t = start_temp
	while True:
		yield t
		t = alpha * t
"""
	função p() retorna uma probabilidade P 0<P<=1
"""
def p(delta,temp):
	return exp(-delta/temp)

"""
	-A chance de aceitar um vizinho pior diminui a cada solução que se aceita
	-exaustion_criteria é o número de vizinhos que o algoritmo tem que avaliar antes de parar
"""
def simulated_annealing(start_temp,alpha,exaustion_criteria, matrix , dimension):
	start_time = time.time()
	current = hc.create_initial_solution(dimension)
	current_eval = hc.route_distance(matrix,current)
	best = current
	best_eval = current_eval
	"""
		cooling_schedule representa uma diminuição da temperatura inversamente proporcional ao tempo gasto
		
	"""
	cooling_schedule = kirkpatrick_cooling(start_temp,alpha)

	#a cada temperatura, visita-se vizinhos até trocar com um deles
	for temp in cooling_schedule:

		#swaped permite a iteração no conjunto dos vizinhos numa mesma temperatura
		swaped = False

		comparisions = 1
		#Ao otimizar SimAnn, é essa referência que deve ser afetada
		neighborhood = hc.create_neighbourhood(current)

		#visita a cada vizinho
		while not swaped:
			#pede novo vizinho aleatório
			solution = hc.getRandomNeighbour(neighborhood)
			solution_eval = hc.route_distance(matrix,solution)
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
					print("Accepted!!!")
					continue

			comparisions+=1
			if comparisions >= exaustion_criteria:
				elapsed_time = time.time()-start_time
				print("Comparisions = " + str(comparisions))
				return best,best_eval,start_temp,temp,alpha,elapsed_time
		print("Comparisions = "+str(comparisions)+"\tEval"+str(current_eval)+"\tTemp:"+str(temp))

if __name__ =="__main__":
	tcwd = os.getcwd()
	selectedTSP = hc.selectTSP(tcwd)
	matrix, dimension = hc.readTSP(selectedTSP)
	for line in matrix:
		print (line)
	testparams = read_AnnealingParams(selectPARAMS(tcwd))
	(best, best_eval, start_temp, temp, alpha, elapsed_time) =\
				simulated_annealing(int(testparams[0]),float(testparams[1]),int(testparams[2]))

