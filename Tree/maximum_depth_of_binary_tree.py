# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _dfs(tree, i):
            if tree is None:
                return i
            depth_left = _dfs(tree.left, i+1)
            depth_right = _dfs(tree.right, i+1)

            return max(depth_left, depth_right)

        return _dfs(root, 0)
    