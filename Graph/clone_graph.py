# 133. Clone Graph (Medium)
# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a connected undirected (always bi-directional) graph
        return new_start_node

        * adjacency list : a collection of unordered lists used to represent a finite graph (1-indexed)

        Example 1: 
        adjList = [[2,4],[1,3],[2,4],[1,3]]
        
        1: {2,4}
        2: {1,3}
        3: {2,4}
        4: {1,3}
    
        1 - 2
        |   |
        4 - 3
        
        return [[2,4],[1,3],[2,4],[1,3]]

        Example 2:
        adjList = [[2,3],[1,3],[1,2]]
        
        1: {2,4}
        2: {1,3}
        3: {1,2}
    
        1 - 2
         \  |
            3
           
        return  [[1,2],[2,3],[1,2]]
    

        Approach: BFS
        Prepare (create or get) a new node before the visit
        While visiting the existing node, get a new node and append the corresponding neighbors
        Graph looks the same, but the nodes are all new with the same way of connections.

        Beats 90.46%
        """
        if not node:
            return
            
        # start node is given
        # print (f"node={node.val}, neighbor = {[x.val for x in node.neighbors]}")

        new_start_node = Node(node.val) # val=1
        created = {node:new_start_node}

        q = deque([node])

        while q:
            old_node = q.popleft()
            new_node = created[old_node]

            for nei in old_node.neighbors:
                if nei not in created:
                    created[nei] = Node(nei.val)
                    q.append(nei)
                
                new_node.neighbors.append(created[nei])

            #print(f"old_node={old_node.val}:{[x.val for x in old_node.neighbors]}")  
            #print(f"new_node={new_node.val}:{[x.val for x in new_node.neighbors]}")    

        return new_start_node
    
