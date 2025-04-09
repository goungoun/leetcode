# 743. Network Delay Time (Medium)
# https://leetcode.com/problems/network-delay-time

from collections import defaultdict

class Solution:
    """
    Minimum time to travel n nodes from the source k
    return min_delay (or -1)

    * times[i] = (ui, vi, wi)

    Example 1: Possible to propagate a signal to all nodes
    times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    
          2 <- start node k
        /   \
       1     3
            / 
          4

    2 -(time:1)-> 1, 2 -(time:1)-> 3 in parallel
    3 -(time:1)-> 4

    Note that the node 1 and the node 3 receive a signal at once, so it take time 1
    2 -(time:1)-> 1, 2 -(time:1)-> 3 -(time:1)-> 4 in parallel

    return 2

    Example 2: Not possible, no outgoing edge from the start node
    times = [[1,2,1]], n = 2, k = 2

          1 
        /   
       2 <- start node k 
     
    1 -(time:1) -> 2

    return -1

    Approach: Dijkstra's shortest path
    From one source to reach out to all nodes with minimum time
    The time to the next node is the fastest from a group that includes all visited node (Greedy)
    The first element of the heap include accumulated time to take so far from k to current node (DP)
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return 0

        # Build a graph : departure -(interval)-> arrival
        g = defaultdict(list)
        for departure, arrival, interval in times:
            g[departure].append((arrival, interval))

        group = set()
        h = [(0, k)] # (arrival_time, curr_node)
        min_delay = 0

        while h and len(group) < n:
            arrival_time, node = heapq.heappop(h) # nearest neighbor

            if node not in group:
                group.add(node) 
                min_delay = max(arrival_time, min_delay)
  
                for neighbor_node, interval in g[node]:
                    if neighbor_node not in group:
                        heapq.heappush(h, (arrival_time + interval, neighbor_node))

        return min_delay if len(group) == n else -1
      
