from graph_implement_list import *

g = Graph()
a = Vertex('A')
g.add_vertex(a)
l = ['A','B','C','D','E','F','G','H','I','J']
g.add_vertex(Vertex('B'))
for i in l:
  g.add_vertex(Vertex(i))
g.add_vertices_from_list(l)
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[0], edge[1])

g.print_graph()
g = Graph()
data = g.ret()
print(len(data))
