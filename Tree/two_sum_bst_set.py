# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Approach:
        Visit all nodes using BFS
        Ignored the BST property
        Replaced the binary search O(log n) to use constant search from a set O(1)

        T=O(n), beats 100%
        S=O(n), beats 28.68%
        """
        if not root:
            return False
        
        # BFS to traverse all values - O(n)
        q = deque([root])
        visited = set()

        while q:
            node = q.popleft()
            target = k-node.val

            # O(1)
            if target != node.val and target in visited:
                return True

            visited.add(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False

