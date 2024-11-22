# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### WARNING!!! This is a buggy code for a practice!!!

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert tree
        return root

        Approach: Recursion and swap

        Example:
        root = [1,2]
              1
            2

        invert
              1
                2           
        """
        if not root:
            return None

        def rec(node):
            if node.left or node.right:  # Fix this!!
                node.left, node.right = node.right, node.left
            else:
                return

            if node.left:
                rec(node.left)

            if node.right:
                rec(node.right)     

        rec(root)

        return root  

### WARNING!!! This is a buggy code for a practice!!!

