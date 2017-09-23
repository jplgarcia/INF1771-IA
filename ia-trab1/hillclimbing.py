




def evaluate_neighbours ( task, neighbours ): #seleciona o melhor vizinho (com a menor distancia)

	shortest_distance = 0
	best_neighbour = []

	for neighbour in neighbours:
		distance = task.route_distance(neighbour)
		if shortest_distance == 0:
			shortest_distance = distance
		elif distance < shortest_distance:
			shortest_distance = distance
			best_neighbour = neighbour

	return (best_neighbour, shortest_distance)





def hill_climbing(task):
	initial_solution = task.create_initial_solution()
	neighbourhood =  initial_solution.create_neighbourhood()
	(best_neighbour,distance)= evaluate_neighbours( task , neighbourhood )
	print (distance)
	print (best_neighbour)
