# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time

from collections import defaultdict

class Solution:
    """
    Minimum time to travel n nodes from the source k
    return delay (or -1)

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

    Approach: Dijkstra's shortest path
    Use min heap to decide the next node 
    The time to the next node is the fastest from a group that includes all visited node (Greedy)
    The first element of the heap include accumulated time to take so far from k to current node (DP)
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return 0

        # Build a graph : u -(time)-> v
        g = defaultdict(list)
        for u, v, time in times:
            g[u].append((v,time))

        group = set() # key: node, value: time to take from k
        h = [(0, k)] # (accumulated_time, curr_node)

        delay = 0

        while h:
            time, node = heapq.heappop(h) # nearest neighbor

            if node not in group:
                group.add(node) 
                delay = max(time, delay)
  
                for adj_node, adj_time in g[node]:
                    if adj_node not in group:
                        accumulated_time = time + adj_time
                        heapq.heappush(h, (accumulated_time, adj_node))

        return delay if len(group) == n else -1
      
