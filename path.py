#!/usr/bin/env python

from edge import Edge

class Path:
    def __init__(self, node=None):
        self.path = list()
        self.cost = 0
        self.addPath(Edge(node,0))

    def addPath(self,edge):
        self.path.append(edge.toNode)
        self.cost += edge.weight
        return self

    def compare(self,path):
        if self.path == path:
            return 1
        else:
            return -1

    def clone(self, edge):
        p = Path(self.path[0])
        p.path = self.path
        p.cost = self.cost
        p.addPath(edge)
        return p

    def peek(self):
        return self.path[len(self.path)-1]