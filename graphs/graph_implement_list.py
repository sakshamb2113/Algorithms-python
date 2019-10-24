#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:24:50 2019

@author: saransh
"""

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()
    def add_neighbors(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
            
class Graph:
    vertices = {}   #contains all the vertices 
    
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices: #checks if vertex matches format of Vertex(defined by us)
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_vertices_from_list(self,l):      
        for item in l:
            if Vertex(item).name not in self.vertices:
                self.vertices[Vertex(item).name] = Vertex(item)
        return True                                                       #return value should be outside the loop
    def add_edge(self,u,v):                                               #add edge pairs  
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbors(v)                             #add v to list of u
            self.vertices[v].add_neighbors(u)                             #add  u to list of v
            return True 
        else:
            self.add_vertex(Vertex(u))
            self.add_vertex(Vertex(v))
            self.vertices[u].add_neighbors(v)                             #add v to list of u
            self.vertices[v].add_neighbors(u)
            return True
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbors))
    def ret(self):
        return self.vertices
            
'''g = Graph()
#print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
l = ['A','B','C','D','E','F','G','H','I','J']
g.add_vertex(Vertex('B'))
#for i in l:
#	g.add_vertex(Vertex(i))

g.add_vertices_from_list(l)
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[0], edge[1])
'''
#g.print_graph()
#g = Graph()
#data = g.ret()
#print(len(data))

