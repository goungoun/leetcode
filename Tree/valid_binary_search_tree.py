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

        Example:
        root = [2,1,3]
        return True

        root = [2,2,2]
        return False

        root=[5,4,6,null,null,3,7]
             "5"
          4       6
               "3"  7
        return False
        """

        if root is None or not min_val < root.val < max_val:
            return False

        l = True
        r = True

        if root.left:
            l = self.isValidBST(root.left, min_val, min(max_val, root.val))

        if root.right:
            r = self.isValidBST(root.right, max(min_val, root.val), max_val)

        return l and r
