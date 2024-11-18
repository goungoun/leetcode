# 98. Validate Binary Search Tree (Medium)
# https://leetcode.com/problems/validate-binary-search-tree

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val = -2**31-1, max_val= 2**31) -> bool:
        """
        Validate if the given tree is Binary Search Tree
        return True or False

        Definition:
        A binary search tree is a binary tree with the following properties:
        - All items in the left subtree are less than the root
        - All items in the right subtree are greater than the root
        - Each subtree is itself a binary search tree

        Example 1: basic case
        root = [2,1,3]
        return True

        Example 2: edge case, equal condition
        root = [2,2,2]
        return False

        Example 3: edge case, hidden case
        root=[5,4,6,null,null,3,7]
             "5"
          4       6
               "3"  7
        return False
        """
        
        if root is None or not min_val < root.val < max_val:
            return False

        if root.left and not self.isValidBST(root.left, min_val, min(max_val, root.val)):
            return False

        if root.right and not self.isValidBST(root.right, max(min_val, root.val), max_val):
            return False

        return True
        
