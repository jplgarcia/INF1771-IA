import time




def evaluate_neighbours ( task, neighbours ): #seleciona o melhor vizinho (com a menor distancia)

	shortest_distance = 0

	for neighbour in neighbours.getNeighborhood():
		distance = task.eval(neighbour)
		if shortest_distance == 0:
			shortest_distance = distance
		elif distance < shortest_distance:
			shortest_distance = distance
			best_neighbour = neighbour

	return (best_neighbour, shortest_distance)





def hill_climbing(task):
	start_time = time.time()
	initial_solution = task.create_initial_solution()
	neighbourhood =  initial_solution.create_neighbourhood()
	(best_neighbour,distance)= evaluate_neighbours( task , neighbourhood )
	time_elapsed = start_time-time.time()
	print (distance)
	print (best_neighbour)
	print(time_elapsed)
