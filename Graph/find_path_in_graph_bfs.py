# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph

from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # key:vertex , value: list of neighbors
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([source])
        visited = set()

        while q:
            vertex = q.popleft()

            if vertex == destination:
                return True

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in g.get(vertex):
                    if neighbor not in visited:
                        q.append(neighbor)

        return False

