#!/usr/bin/python3


from json.encoder import INFINITY
from pathlib import Path

import Graph_Constructor

def traversal(start_vertex, graph):
#     # This unified algorithm takes a graph, a start_vertex part of this graph
#     # and performs graph traversal using a queuing structure.
#     # The algorighm returns the List of explored_vertices, and a 
#     # routing table to navigate the graph.


        queuing_structure = []
        queuing_structure.append([start_vertex, None]) # null cause the root haven't got parents
        explored_vertices = []
        routing_table = {}
        while queuing_structure: 
            current_vertex, parent = queuing_structure.pop() # we .pop() a vertex and it's parent
            if  current_vertex not in explored_vertices: # if the vertex is not explored
                explored_vertices.append(current_vertex) # we mark it as explored
                routing_table[current_vertex] = parent # we update the routing table by associating the vertex with his parent
               # for neighbor in neighbors(graph, current_vertex): # Finally, we add all unexplored neighbors of the 
                for neighbor in graph[current_vertex]:
                    if neighbor not in explored_vertices:         # vertex to the queuing structure with the current vertex as parent.
                        queuing_structure.append([neighbor, current_vertex]) # If the vertex we popped from the queuing structure was 
        return explored_vertices, routing_table                          # already explored, we simply ignore it.



#So, we initialize two data structures: first, the set of explored vertices, which are initially
#empty, and second, the array of distances from v_1
#to the other vertices in the graph, initialized to infinity everywhere but v_1, where we insert a 0

# Explored = {}
# Distances = {}


# def dijkstra(graph, start_vertex):
#     #initialize
#     min_heap = new_min_heap
#     add_or_replace(min_heap, start_vertex, value)

#     #algorithm loop
#     while min_heap is not None:
#         v, distance = remove(min_heap)
#         for each i neighbor of v:
#             distance_through_v = distance + graph[v][i]
#             add_or_replace(min_heap, i, distance_through_v)
#             return distance_through_v


# best_lenght = INFINITY
# best_path = []
# def bruteforce(remaining, vertex, path, weight, graph):
#     #The arguments of the call are as follows: The list of vertices - the starting point
#     #the initial vertex, an empty list which will contain the optimal path in the end
#     #the initial weight of this empty list, which is 0, and the graph.
#     global best_lenght, best_path
#     if remaining is None:
#         if weight < best_lenght:
#             best_lenght = weight
#             best_path = Path
#         else:
#             for each vertex i in remaining:
#                 bruteforce(remaining -1, i, path +i, weight + graph[vertex][i],graph)



# my_graph = Graph_Constructor.Graph()


# my_graph.add_vertex('v1')
# my_graph.add_vertex('v2')
# my_graph.add_vertex('v3')
# my_graph.add_vertex('v4')
# my_graph.add_vertex('v5')
# my_graph.add_vertex('v6')
# my_graph.add_vertex('v7')


# my_graph.add_edge('v1','v2')
# my_graph.add_edge('v1','v4')
# my_graph.add_edge('v2','v4')
# my_graph.add_edge('v2','v3')
# my_graph.add_edge('v3','v4')
# my_graph.add_edge('v4','v6')
# my_graph.add_edge('v2','v6')
# my_graph.add_edge('v6','v7')
# my_graph.add_edge('v6','v5')


# my_graph.print_graph()

# print(traversal('v1', my_graph.adj_list))

test = []
for i in range(1,200001):
    test.append(i)

def max_pairwise_product(a):
    index1 = 0
    for i in range(len(a)):
        if a[i] > a[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
        for i in range(len(a)):
            if a[i] != a[index1] and a[i] > a[index2]:
                index2 = i
    else:
        index2 = 0
        for i in range(len(a)):
        
            if a[i] != a[index1] and a[i] > a[index2]:
                index2 = i
    return a[index1] * a[index2]

print(max_pairwise_product(test))