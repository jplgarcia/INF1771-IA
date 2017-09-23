from random import shuffle

path = "/Users/juliaaleixo/PycharmProjects/ia-trab1/gr24.tsp"
file = open(path, "r")
count = 0
dimension = 0
i = 0
j = 0

beganReadingMatrix = False
for line in file:
    if(not beganReadingMatrix):
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


def create_neighbourhood(initial_solution):

    length = len(initial_solution) - 1
    neighbours = []

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

initial_solution = create_initial_solution( int(dimension) )
neighbourhood = create_neighbourhood( initial_solution )
(best_neighbour,distance)= evaluate_neighbours( matrix , neighbourhood )
print distance
print best_neighbour
