# 98. Validate Binary Search Tree (Medium)
# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        min_val = float('-inf')
        max_val = float('inf')
        stack = [(root, min_val, max_val)]

        while stack:
            node, min_val, max_val = stack.pop()
            # preorder 
            if not (min_val < node.val < max_val):
                return False

            # stack is LIFO, put left later makes the traverse left first
            if node.right:
                stack.append((node.right, node.val, max_val))

            if node.left:
                stack.append((node.left, min_val, node.val))

        return True
      
