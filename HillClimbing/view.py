from Tkinter import *
from hillclimbing import runForCommomHillClimb, runForMultipleSeedsHillClimb
import networkx as nx
import pylab as plt

#Outer scope Variables!
distance = 0
neighbor = []
time = 0
matrix = []

#Window definition
root = Tk()
root.resizable(width=False, height=False)
root.title("hillclimbing")
root.geometry("500x500")

#Description label:
descriptionLabel = Label(root, text = "Choose the TSP you want to solve:")
descriptionLabel.pack()

#Dropdownbox to choose tsp:
dropValue = StringVar(root)
dropValue.set("gr17.tsp") # initial value
option = OptionMenu(root, dropValue, "gr17.tsp", "gr21.tsp", "gr24.tsp", "hk48.tsp", "si175.tsp")
option.pack()

#Action
def runButtonAction():
    global distance, neighbor, time, matrix #To change out of scope variables
    (distance, neighbor, time, matrix) = runForMultipleSeedsHillClimb(dropValue.get())
    textField.delete(1.0,END)
    textField.insert(END, "Results for " + dropValue.get())
    textField.insert(END, ":\nTime: ")
    textField.insert(END, time)
    textField.insert(END, "\nDistance: ")
    textField.insert(END, distance)
    textField.insert(END, "\nTour: ")
    textField.insert(END, neighbor)
    return (distance, neighbor, time, matrix)

#run tsp button:
runButton = Button(root, text ="Run Hillclimbing", command = lambda: runButtonAction())
runButton.pack()

#Text Field
textField = Text(root, height=18, width=490)
textField.pack()

#action
def showGraphAction():
    global distance, neighbor, time, matrix #To change out of scope variables
    # Create a graph
    Graph = nx.Graph()
    # distances
    Distances = matrix
    labels = {}
    lenght = len(neighbor)
    #Create all the dashed edges for a complete graph, so the graph wont simply be a circle
    for n in range(len(Distances)):
        for m in range(len(Distances) - (n + 1)):
            Graph.add_edge(n, n + m + 1, weight=0.1)
    #Create the solid edges for the tour(must come after the other)
    for i in range(0, lenght, 1):
        Graph.add_edge(neighbor[i], neighbor[(i + 1) % lenght], weight=0.6)
        labels[(neighbor[i], neighbor[(i + 1) % lenght])] = str(Distances[neighbor[i]][neighbor[(i + 1) % lenght]])
    #Setup the collection for both types of edges
    elarge = [(u, v) for (u, v, d) in Graph.edges(data=True) if d['weight'] > 0.5]
    esmall = [(u, v) for (u, v, d) in Graph.edges(data=True) if d['weight'] <= 0.5]
    #A dictionary with nodes as keys and positions as values.
    pos = nx.spring_layout(Graph)
    # Draw nodes, dashed edges, solid edges, node labels and edge labels
    nx.draw_networkx_nodes(Graph, pos, node_size=210)
    nx.draw_networkx_edges(Graph, pos, edgelist=elarge, width=4, alpha=1, edge_color='k', style='solid')
    nx.draw_networkx_edges(Graph, pos, edgelist=esmall, width=0.1, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_labels(Graph, pos, font_size=12, font_family='sans-serif')
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels, font_size=8)
    #plot
    plt.axis('off')
    plt.show()

#show graph button
showGraphButton = Button(root, text ="Show Graph", command = lambda: showGraphAction())
showGraphButton.pack()


root.mainloop()

