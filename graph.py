#!/usr/bin/env python

from node import Node
from path import Path

class Graph(Node):

    def __init__(self, nodes = 0, directed = False):
        self.stack = list()
        self.directed = directed
        self.depth = 0
        self.size = nodes

    def addEdge(self, fromNode, toNode, weight = None):
        # check for Node type
        if fromNode.__class__ == Node and toNode.__class__ == Node:
            if len(self.stack) < 1:
                self.stack.append(fromNode)
            temp = max(fromNode.depth, toNode.depth)
            self.depth = max(temp,self.depth)
            fromNode.addNeighbor(toNode, weight)
        else:
            print("Invalid Type Argument")

    def dfs(self, goal):
        print('\nDepth-First Search')
        stack = list(self.stack)
        length = len(stack)
        visited = list()
        while length > 0:
            node = stack[-1]
            if node.compare(goal) > 0:
                print('Goal state reached!')
                return node
            visited.append(node)
            print(node)
            nn = node.getNeighbors()
            for n in nn:
                if visited.count(n.toNode) < 1:
                    stack.append(n.toNode)
                    break
                else:
                    node = None
            if node == None or len(nn) < 1:
                if visited.count(stack[-1]) > 0:
                    stack.pop()
            length = len(stack)
        print('No potential goal state!')

    def bfs(self,goal):
        print('\nBreadth-First Search')
        stack = list(self.stack)
        visited = list()
        length = len(stack)
        while length > 0:
            node = stack.pop(0)
            print(node)
            if node.compare(goal) > 0:
                print('Goal state reached!')
                return node
            visited.append(node)
            nn = node.getNeighbors()
            for n in nn:
                if visited.count(n.toNode) < 1:
                    if stack.count(n.toNode) < 1:
                        stack.append(n.toNode)
            length = len(stack)
        print('No potential goal state!')

    def dls(self,goal,limit=0):
        print('\nDepth-Limited Search')
        stack = list(self.stack)
        length = len(stack)
        nn = list()
        visited = list()
        while length > 0:
            node = stack[-1]
            if node.compare(goal) > 0:
                print('Goal state reached at depth -> ', node.depth, '!')
                return node
            visited.append(node)
            if node.depth < limit:
                nn = node.getNeighbors()
            for n in nn:
                if visited.count(n.toNode) < 1:
                    stack.append(n.toNode)
                    break
                else:
                    node = None
            if node == None or len(nn) < 1:
                if visited.count(stack[-1]) > 0:
                    stack.pop()
            length = len(stack)
        print('No potential goal state at depth -> ', limit,'!')

    def ids(self,goal):
        print('\nIterative Deepening Search')
        depth = 0
        found = self.dls(goal,depth)
        while found == None:
            depth += 1
            found = self.dls(goal, depth)
            if depth == self.depth:
                break
        if found == None:
            print('No potential goal state at max depth -> ', depth,'!')
        return found

    def bidi(self,goal):
        print('\nBidirectional Search')


    def ucs(self,goal):
        print('\nUniform Cost Search')
        paths = list()
        ex = 0
        depth = 0
        while True:
            if self.stack[0].compare(goal) > 0:
                print('No cyclic path on same node!')
                break
            if len(paths) < 1:
                nn = self.stack[0].getNeighbors()
                if len(nn) < 1:
                    print('Single node exists!')
                    break
                for n in nn:
                    paths.append(Path(self.stack[0]).addPath(n))
            for path in paths:
                current = path.peek()
                print('Peek: ', current.data)
                if current.compare(goal) > 0:
                    depth = current.depth
                    continue
                ex = max(current.depth,ex)
                nn = current.getNeighbors()
                for n in range(len(nn)):
                    if n == 0:
                        index = paths.index(path)
                        paths[index] = path.addPath(nn[n])
                    else:
                        paths.append(path.clone(nn[n]))
            if depth >= ex:
                break
            if ex == self.depth:
                print("No path exist to goal state!")
                break
        return paths