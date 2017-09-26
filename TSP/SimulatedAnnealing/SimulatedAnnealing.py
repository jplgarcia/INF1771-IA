from random import random
import time
from math import exp
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
def simulated_annealing(task,start_temp,alpha,exaustion_criteria):
	start_time = time.time()
	current = task.create_initial_solution()
	current_eval = task.eval(current)
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
		neighborhood = current.create_neighbourhood()

		#visita a cada vizinho
		while not swaped:
			#pede novo vizinho aleatório
			solution = neighborhood.getRandom()
			solution_eval = task.eval(solution)
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
				elapsed_time = start_time-time.time()
				print("Comparisions = " + str(comparisions))
				return best,task.eval(best),start_temp,temp,alpha,elapsed_time
		print("Comparisions = "+str(comparisions)+"\tEval"+str(current_eval)+"\tTemp:"+str(temp))