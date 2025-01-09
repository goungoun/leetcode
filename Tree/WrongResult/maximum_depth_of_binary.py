# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Warning!!! This causes wrong result, always return 0!!

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_depth = 0

        def dfs(node, tmp_depth = 0):
            if node is None:
                self.max_depth = max(self.max_depth, tmp_depth)
                return

            if node.right: # Fix This!! Hint: Remove this condition and adjust indentation
                dfs(node.right, tmp_depth+1)

            if node.left: # Fix This!! Hint: Remove this condition. and adjust indentation
                dfs(node.left, tmp_depth+1)

        dfs(root)

        return self.max_depth

       
            
       
