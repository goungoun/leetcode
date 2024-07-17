# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Average value on each level of the tree
        return level_avgs

        Example:
        1) root = [3,9,20,null,null,15,7]
           3
        9     20
           15    7

        L1 : 3,        avg = 3
        L2 : 9, 20     avg = 29/2 = 14.5
        L3 : 15, 7     avg = 22/2 = 11
        return [3, 14.5, 11]

        2) root = [3,9,20,15,7]
                3
             9    20
          15   7

        L1 : 3         avg = 3 
        L2 : 9, 20     avg = 29/2 = 14.5
        L3 : 15, 7     avg = 22/2 = 11
        return [3, 14.5, 11]
        
        The results of Example 1 and Example 2 are the same. 
        The level does matter, it doesn't matter if the child belongs to left or right.

        Approach:
        To traverse the tree BFS (level order), a queue is required to control its order in FIFO
        Consider using double loop to ensure one iteration on the while loop collects all values within the same level
        No avg() in Python, combine sum() and len() instead.
        """

        q = deque([root])
        level_avgs = []

        # double loop, but T=O(n)
        while q:
            # nodes in the same level
            level_sum = 0
            level_cnt = 0
            for _ in range(len(q)): 
                node = q.popleft()
                node_val = node.val if node.val else 0
                level_sum += node_val
                level_cnt += 1

                # all children belongs to the node to be ready on the queue
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            
            level_avg = level_sum/level_cnt if level_cnt !=0 else 0
            level_avgs.append(level_avg)

        return level_avgs
