#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:55:17 2019

@author: saransh
"""

from graph_implement_list import Graph
N = int(input())
g = Graph()
for i in range(N):
    u,v = list(map(int,input().split()))
    g.add_edge(u,v)
    
g = Graph()
data = g.ret()

#visits all the connected nodes connected to the node.
def DFSUntill(node,visited,data,ans):
    visited[node] = 1
    ans.append(node)
    for i in data[node].neighbors:
        if visited[i]==0:
            DFSUntill(i,visited,data,ans)

#Depthfirst Search in Graph
def DFS(node,data):
    visited = [0]*(len(data)+1)
    ans = []
    DFSUntill(node,visited,data,ans)
    print(visited)
    return ans



print(DFS(1,data))
