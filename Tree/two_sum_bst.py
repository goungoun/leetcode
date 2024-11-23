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
        Find two elements to make their sum is equal to k
        return True (or False)

        Example 1:
        root = [5,3,6,2,4,null,7], k = 9

        5, target = 4
        dfs, go to the left and right, there is 4
        return True

        Approach: Binary Search
        Use BFS to traverse nodes
        For each node, calculate the target for search.
        Do binary search
        
        T = O(nlogn), beats 5.13 %
        S = avg O(nlogn) max O(n) for call stack, beats 28.68%

        * It performs better to use set and dfs ignoring the BST property
        """
        if not root:
            return False
        
        # binary search to find the value from the root- O(log n)
        def binary_search(node, target):
            if not node:
                return False

            if node.val == target and node.val != root.val:
                return True

            if node.left and binary_search(node.left, target):
                return True

            if node.right and binary_search(node.right, target):
                return True

            return False

        # BFS to traverse all values - O(n)
        q = deque([root])
        while q:
            node = q.popleft()
            target = k-node.val

            if target != node.val and binary_search(root, target):
                return True

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False

        
