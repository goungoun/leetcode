# 743. Network Delay Time (Medium)
# https://leetcode.com/problems/network-delay-time

# NEED TO FILL ???????

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return 0

        # Build a graph : departure -(interval)-> arrival
        g = defaultdict(list)
        for departure, arrival, interval in times:
            g[departure].append((arrival, interval))

        group = set()
        h = [(?, ?)] # The order is important to pick up the fastest path fisrt!!!
        min_delay = 0

        while h and len(group) < n:
            arrival_time, node = heapq.heappop(h) # nearest neighbor

            if node not in group:
                group.add(node) 
                min_delay = max(???????, min_delay)
  
                for neighbor_node, interval in g[node]:
                    if neighbor_node not in group:
                        heapq.heappush(h, (???????, neighbor_node))

        return min_delay if len(group) == n else -1
