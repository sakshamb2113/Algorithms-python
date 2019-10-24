#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:52:54 2019

@author: saransh
"""
#from graph_implement_list import Vertex
from graph_implement_list import Graph
n = 5
g = Graph()
for i in range(n):
    u,v = list(map(int,input().split()))
    g.add_edge(u,v)
    
g = Graph()
data = g.ret()
def BFS(node,data):    #node is your starting node of the search 
    ans = []
    visited = [0]*(len(data)+1)
    queue = []
    queue.append(node)
    visited[node] = 1
    
    while queue:
        node = queue.pop(0)
        visited[node] = 1
        ans.append(node)
        
        for i in data[node].neighbors:
            if visited[i] == 0:
                queue.append(i)
                
                visited[i] = 1
    return ans
ans = BFS(1,data)
print(ans)
            
        
    
    

