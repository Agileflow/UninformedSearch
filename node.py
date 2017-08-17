#!/usr/bin/env python

from edge import Edge

class Node(Edge):

    def __init__(self, data,depth=0):
        self.data = data
        self.visited = False
        self.adj = list()
        self.depth = depth

    def compare(self, data):
        if self.data == data:
            return 1
        else:
            return -1

    def addNeighbor(self, toNode, weight = None):
        if toNode.__class__ == Node:
            if self.adj.count(toNode) < 1:
                self.adj.append(Edge(toNode, weight))

    def getNeighbors(self):
        return self.adj

    def nsize(self):
        return len(self.adj)

    def __str__(self):
        return str(self.data)