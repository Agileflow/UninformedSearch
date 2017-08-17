#!/usr/bin/env python

from node import Node
from graph import Graph
from edge import Edge
from path import Path

if __name__ == '__main__':

    dataset = [['A',0],['B',1],['C',2],['D',3],['E',3],['F',1],['G',2],['H',2]]
    edges = [['A','B',3],['A','F',2],['B','C',5],['C','D',1],['C','E',2],['F','G',1],['F','H',3]]


    #dataset = [[10,1],[20,1],[30,2],[40,0],[50,3],[60,3],[70,4]]
    #edges = [[40,20],[40,10],[20,10],[20,30],[20,50],[20,60],[10,30],[30,60],[50,70],[60,70]]


    #dataset = [['A','B'],['A','C'],['A','D'],['B','F'],['C','F'],['D','E'],['E','F']]
    #edge = [['A','B',5],['A','D',2],['B','E',1],['C','E',7],['D','E',5]]

    #dataset = [['A',0],['B',1],['C',1],['D',1],['E',2]]
   # edges = [['A','B',5],['A','C',1],['A','D',2],['B','E',1],['D','E',5],['C','E',7]]

    nodes = dict()

    for data in dataset:
        nodes[data[0]] = Node(data[0], data[1])

    g = Graph(nodes=len(dataset) - 1)

    for edge in edges:
        if nodes.get(edge[0]) and nodes.get(edge[1]):
            g.addEdge(nodes.get(edge[0]), nodes.get(edge[1]), edge[2])

    #print(g.ucs('E'))
    result = g.ucs('G')
    if result != None:
        for paths in result:
            data = ""
            for path in paths.path:
                data += path.data + " -> "
            print(data + str(paths.cost))
