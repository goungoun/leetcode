# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time

from collections import defaultdict

class Solution:
    """
    Minimum time to travel n nodes from the source k
    return delay_time (or -1)

    * times[i] = (ui, vi, wi)

    Example 1:
    times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Start from the node 2 and the other "all nodes" will be receve a signal
          2 <- start
        /   \
       1     3
            / 
          4

    2 -(time:1)-> 1, 2 -(time:1)-> 3 in parallel
    3 -(time:1)-> 4

    Note that the node 1 and the node 3 receive a signal at once, so it take time 1 

    return 2
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return 0

        # Build a graph : u -(time)-> v
        g = defaultdict(list)
        for u, v, time in times:
            g[u].append((v,time))

        visited = set() # key: node, value: time to take from k
        h = [(0, k)] # (time from k, source)

        delay_time = 0

        while h:
            time, node = heapq.heappop(h)

            if node not in visited:
                visited.add(node) 
                delay_time = max(time, delay_time)
  
                for adj, adj_time in g[node]:
                    heapq.heappush(h, (time + adj_time, adj))

        return delay_time if len(visited) == n else -1
      
