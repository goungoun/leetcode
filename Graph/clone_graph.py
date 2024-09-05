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
        Clone a connected undirected graph
        return the start node of a cloned graph

        Example:
        Graph looks the same, but the nodes are all new with the same way of connections.

        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]

        Approach: 
        Traverse the graph in BFS
        Prepare (create or get) a new node before the visit
        While visiting the existing node, get a new node and append the corresponding neighbors
        """

        if not node:
            return None

        new_n = Node(node.val)
        created = {node.val: new_n}

        q = deque()
        q.append(node)

        visited = set()
        visited.add(node)

        while q:
            n = q.popleft()
            new_n = created[n.val]
            
            for nei in n.neighbors:
                if nei.val not in created:
                    created[nei.val] = Node(nei.val)
                new_n.neighbors.append(created[nei.val])
                
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
            
        return created[node.val]
