#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:21:30 2020

@author: PetersMacBook
"""


#Needs:
#grid.nodes as list containing all nodes
#grid.size as number of nodes. or just len(grid.nodes)
#node.adj as list of what is adjacent to 
#node.dist as list of distances correlating to adjacency list

# Adjascency List representation in Python

from random import randint
from string import ascii_uppercase as caps

class Grid:
    def __init__(self, node_list, num):
        keys = [node_list[i] for i in range(num)]
        dicts = {}
        
        for i in keys:
            dicts[i] = {"adj": [], "dist": []}   
            
        self.dict = dicts
        
    def __repr__(self):
        rep = ""
        
        for key in self.dict:
            rep += f"\n{key}: {self.dict[key]}"
        
        return rep
                 
    def edge(self, node1, node2, distance = None):
        """ 
        specify a connection between two nodes, and their distance if desired - 
        if distance not input will be randomly assigned an integer value 
        """
        if distance == None:
            distance = randint(0, 9)
        
        d = self.dict
     
        if node1 in d and node2 in d and node1 != node2:      
            d[node1]['adj'].append(node2)
            d[node1]['dist'].append(distance)
            
            d[node2]['adj'].append(node1)
            d[node2]['dist'].append(distance)
        else:
            raise KeyError("Input names of two different existing nodes")
            
    def fill(self):
        """ auto-fills all remaining possible connections betweeen nodes """
        nodes = self.nodes()
        d = self.dict
        
        for node1 in nodes:
            for node2 in nodes:
                if node2 not in d[node1]['adj'] and node1 != node2:
                    self.edge(node1, node2)

    def nodes(self):
        """ return list of all nodes within Grid class """
        node_list = []
        
        for key in self.dict.keys():
            node_list.append(key)  
            
        return node_list
       
    def size(self):
        """ return size of Grid class """
        return len(self.dict)   
              
    def adj(self, node):
        """ return all adjacencies of an inputted node """
        return self.dict[node]['adj']
    
    def dist(self, node):
        """ return all distances from an inputted node """
        return self.dict[node]['dist']
  
    
  
if __name__ == "__main__":    
    g = Grid(caps, 5)
    g.edge('A', 'B', 3)
    g.edge('A', 'C', 7)
    g.edge('A', 'E', 2)
    g.edge('B', 'C', 5)
    g.edge('B', 'D', 9)
    g.edge('B', 'E', 8)
    print(g)

