# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return ? # Complete here
        
        depth_left = self.maxDepth(root.left) 
        depth_right = self.maxDepth(root.right) 

        return max(depth_left, depth_right) + 1
    
    def maxDepth_bak1(self, root: Optional[TreeNode], i=0) -> int:
        """
        DFS - post order
        """
        if root is None:
            return ? # Complete here

        depth_left = self.maxDepth(root.left, i+1)
        depth_right = self.maxDepth(root.right, i+1)

        return max(depth_left, depth_right)


    def maxDepth_bak2(self, root: Optional[TreeNode]) -> int:
        """
        DFS - pre order, with helper function
        """
        self.max_length = 0

        def dfs(node, i=0):
            if not node:
                self.max_length = max(i, self.max_length)
                return # Do not need to fix this. Just return is enough.

            dfs(node.left, i+1)
            dfs(node.right, i+1)

        dfs(root)
        return self.max_length
