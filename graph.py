#Markov Chain representation
import random

class Vertex:
    def __init__(self, value):
        self.value = value  #value = the word
        #adjacent = примыкающий 
        self.adjacent = {}  #nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        #adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight  

    def increment_edge(self, vertex):
        #if this vertex is the key that is currently in this dictionaty, 
        #then we get the value of this vertex or we make it equal to 0 at default 
        #and then we add a 1
        #keeps the track of amount of neighbors
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        #choose the next word (randomly) based on weights 
        #returns the list, so we want to get the first item from it
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

#Represent the vertices as a graph 
class Graph:
    def __init__(self):
        #whenever we encounter a new word, we look it up in this dictionary and then get the vertex
        #object from this dictionary (string to vertex mapping)
        self.vertices = {}

    def get_vertex_values(self):
        #return all possible words (what are the values of all vertices?)
        return set(self.vertices.keys()) 
    
    def add_vertex(self, value):
        #create a new Vertex object and put it into string to vertex mapping 
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        #firstly, check that the value is graph, otherwise adds it
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]  #secondly, get the vertex object 
    
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        #gets probability mappings of every vertex
        for vertex in self.vertices.values():
            vertex.get_probability_map()