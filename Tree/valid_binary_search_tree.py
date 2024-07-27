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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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

        def dfs(root, min_val = -2**31-1, max_val= 2**31):
            if not min_val < root.val < max_val:
                return False

            if root.right and root.val > root.right.val:
                return False

            if root.left and root.val < root.left.val:
                return False

            a = True
            b = True

            if root.left:
                a = dfs(root.left, min_val, min(max_val, root.val))

            if root.right:
                b = dfs(root.right, max(min_val, root.val), max_val)
 
            return a and b

        return dfs(root)

