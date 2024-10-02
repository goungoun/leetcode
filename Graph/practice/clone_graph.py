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
        if not node:
            return None

        head = Node(node.val)
        created = {head.val:head} # Node.val is unique for each node.
        
        q = deque([node]) # not head
        visited = set([node]) # not head

        while q:
            old_n = q.popleft()
            new_n = created[old_n.val]

            for nei in old_n.neighbors:
                if nei.val not in created:
                    created[nei.val] = Node(nei.val)

                new_n.neighbors.append(created[nei.val])
              
                # Error: You must return a copy of all the nodes in the original graph
                if nei not in visited:
                    q.append(node) #FIX: q.append(nei)
                    visited.add(nei)

        return head
