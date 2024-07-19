# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Verify a path from source to destination from a graph
        return True (if there is a path)

        Example 1: Valid Paths
        edges = [[0,1],[1,2],[2,0]]
            0
          /  \ 
         1  - 2

        source = 0, destination = 2
        e.g. 0 -> 1 -> 2, 0 -> 2
   
        return True

        Example 2: No path
        edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
           0
          /  \ 
         1    2

        3  - 5
          \  | 
             4

        source = 0, destination = 5
        return False

        Approach:
        Convert edges to an explicit bi-directional graph using a default dictionary
        Traverse the graph DFS or BFS
        Return True if the destination is visited
        """

        # key: vertex, value: adjacent vertexs e.g. {0: [1,2]}
        graph = defaultdict(list)

        # bi-directional edge: u->v, v->u
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(vertex):
            if vertex == destination:
                return True

            for adj_vertex in graph[vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    if dfs(adj_vertex):
                        return True

            return False

        return dfs(source)
