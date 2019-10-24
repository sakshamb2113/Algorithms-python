#weighted,undirected graph

class Vertex:
    def __init__(self,n):
        self.name = n
       
            
class Graph:
    vertices = {}   #contains all the vertices 
    edges = []
    edges_indices = {}
    def add_vertex(self,vertex):                                                    #for inpredictable vertices ('A','B') or (1,5,8)
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:          #checks if vertex matches format of Vertex(defined by us)
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0]*(len(self.edges)+1))
            self.edges_indices[vertex.name] = len(self.edges_indices)
            return True
        else:
            return False
    def make_matrix_of_nxn(self,n):                                             #creates nxn matrix of zeroes
        self.edges = [[0 for i in range(n)] for j in range(n)]
    
    def add_edge_number(self,u,v,weight):                                            #replaces 0 with weights in matrix 
        self.edges[u-1][v-1] = weight
        self.edges[v-1][u-1] = weight
        return True
    
    def add_edge(self,u,v,weight = 1):                                               #adds edges for unpredictable vertices
        if u in self.vertices and v in self.vertices:
            self.edges[self.edges_indices[u]][self.edges_indices[v]] = weight 
            self.edges[self.edges_indices[v]][self.edges_indices[u]] = weight 
            
            return True 
        else:
            return False
    def print_graph(self):
        for v,i in sorted(list(self.edges_indices.items())):
            print(v + ' ',end = '')
            for j in range(len(self.edges)):
                print(self.edges[i][j],end = '')
            print(' ')
    def ret(self):
        return self.edges
            
g = Graph()
# print(str(len(g.vertices)))
n = 5
g.make_matrix_of_nxn(n)
weight = 7
g.add_edge_number(1,2,weight)
matrix = g.ret()
print(matrix) 
'''a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.print_graph()
'''