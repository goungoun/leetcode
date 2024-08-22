# 433. Minimum Genetic Mutation (Medium)
# https://leetcode.com/problems/minimum-genetic-mutation

from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Minimum number of mutations required from a startGene to a endGene
        return count, or -1 if not found

        * bank: check valid gene mutations
        * 8-characters with choices from A,C,G,T

        Example: 
        "AACCGGTT" --> "AACCGGTA"
        one mutation

        return 1

        Approach: BFS
        Add startGene from the queue
        Check all banks to see if there is a possible mutation, "one char" difference
        Put the candidates on the queue and repeat
        """
        bankSet = set(bank)
        
        q = deque()
        q.append(startGene)
        
        visited = set()
        visited.add(startGene)
        
        count = 0
        
        # BFS
        while q:
            for _ in range(len(q)):
                gene = q.popleft()

                # no more mutation required
                if gene == endGene:
                    return count

                candidates = bankSet.difference(visited)
                
                # def. one mutation is one single character changed
                changed_cnt = 0
                for candidate in candidates:
                    changed_cnt = sum(1 for i in range(8) if gene[i] != candidate[i])
                    if changed_cnt == 1:
                        visited.add(candidate)
                        q.append(candidate)
                        
            count += 1
        
        return -1
