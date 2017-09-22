from random import shuffle

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
    fullpathfile = cwd + filesname[selectedoption]
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
        i = i + 1

    if 'dimension' in locals():
        if ( dimension > 0 ):
            i = i + 1
            matrix = [[0 for x in range(dimension)] for y in range(dimension)]
            while (i < length - 1):
                line = lines[i].split(' ')
                for word in line:
                    matrix[matrixLine][matrixColumn] = int ( word )
                    matrixColumn = matrixColumn + 1
                    if (word == "0"):
                        matrixLine = matrixLine + 1
                        matrixColumn = 0
                i = i + 1
    file.close()
    return matrix, dimension


def writeTSP(currentWorkingDirectory, selectedTSP, cost, route):
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

        total += distance_matrix [ city_i ][ city_j ]

    return total

def evaluate_neighbours ( distance_matrix , neighbours ): #seleciona o melhor vizinho (com a menor distancia)

    shortest_distance = 0
    best_neighbour = []

    for neighbour in neighbours:
        distance = route_distance( distance_matrix , neighbour )
        if shortest_distance == 0:
            shortest_distance = distance
        elif distance < shortest_distance:
            shortest_distance = distance
            best_neighbour = neighbour

    return ( best_neighbour, shortest_distance )


def swap ( solution, first_city_number , second_city_number ): #funcao que troca duas cidades

    aux = solution[first_city_number]
    solution[first_city_number] = solution[second_city_number]
    solution[second_city_number] = aux

    return solution


def create_neighbourhood ( initial_solution ):

    length = len(initial_solution) - 1
    neighbours = [initial_solution]

    for number in range ( 0 , length , 1 ):
        if ( number == 0 ): # a cidade inicial precisa continuar na mesma posicao
            continue
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

cwd = os.getcwd()
selectedTSP = selectTSP(cwd)
( matrix , dimension ) = readTSP(selectedTSP)

initial_solution = create_initial_solution( int ( dimension ) )
print initial_solution
neighbourhood = create_neighbourhood ( initial_solution )
( best_neighbour , distance ) = evaluate_neighbours( matrix , neighbourhood )

while best_neighbour != initial_solution:
    print best_neighbour
    initial_solution = best_neighbour
    neighbourhood = create_neighbourhood ( initial_solution )
    ( best_neighbour, distance ) = evaluate_neighbours ( matrix , neighbourhood )
    print distance
print best_neighbour


route = []
route.append("1")
route.append("2")
route.append("3")
writeTSP(cwd, selectedTSP, "10", route)