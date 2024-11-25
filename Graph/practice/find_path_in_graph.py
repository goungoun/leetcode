# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not n:
            return False

        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set([source])

        def dfs(vertex):
            if vertex == destination:
                return True

          
            for nei in g[vertex]:
                if nei not in visited:
                    visited.add(vertex)

                    # Fixed: Wrong result
                    if dfs(nei):
                        return True
                    #return dfs(nei) 

            return False

        return dfs(source) 
