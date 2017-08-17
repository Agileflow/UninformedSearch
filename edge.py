#!/usr/bin/env python

class Edge:
    def __init__(self, toNode, weight = None):
        self.toNode = toNode
        self.weight = weight

    def __str__(self):
        return '',self.toNode,' ',self.weight
