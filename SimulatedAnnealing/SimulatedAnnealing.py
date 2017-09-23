import random.random as random
import math.exp as exp
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

def p(delta,temp):
	return exp(-delta,temp)

"""
	-A chance de aceitar um vizinho pior diminui a cada solução que se aceita
	-exaustion_criteria é o número de vizinhos que o algoritmo tem que avaliar antes de parar
"""
def simulated_annealing(task,start_temp, alpha):
	current = task.getStartSolution()
	best = current
	"""
		cooling_schedule representa uma diminuição da temperatura inversamente proporcional ao tempo gasto
		
	"""
	cooling_schedule = kirkpatrick_cooling(start_temp,alpha)

	#a cada temperatura, visita-se vizinhos até trocar com um deles
	for temp in cooling_schedule:

		#swaped permite a iteração no conjunto dos vizinhos numa mesma temperatura
		swaped = False

		comparisions = 1
		neighborhood = current.getNeighborhood()

		#visita a cada vizinho
		while not swaped:
			#pede novo vizinho aleatório
			solution = neighborhood.getRandom()

			#avaliação do vizinho com a solução atual
			delta_eval = solution.eval - current.eval
			if delta_eval<=0:
				current = solution
				if current>best:
					best = current
					swaped = True
			else:
				if random() < p(abs(delta_eval),alpha):
					current = solution
					swaped = True

			comparisions+=1
			if comparisions >= task.exaustion_criteria:
				return best,best.eval,start_temp,temp,alpha