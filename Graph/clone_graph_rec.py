# 133. Clone Graph (Medium)
# https://leetcode.com/problems/clone-graph

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach:
        Recursive DFS
        
        T=O(V+E)
        S=O(V+E)
        """
        if not node:
            return None

        created = {} # key: old, value: new
        
        def clone(node):
            if node in created:
                return created[node]
            
            new_node = Node(node.val)
            created[node] = new_node

            new_node.neighbors = [clone(neighbor) for neighbor in node.neighbors]
            
            return new_node
        
        return clone(node)
      
