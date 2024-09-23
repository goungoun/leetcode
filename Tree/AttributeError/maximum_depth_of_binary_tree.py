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
        if root is None:
            return 0

        self.max_depth = 0

        def dfs(node, depth=0):
            # base case
            if node is None:
                self.max_depth = max(depth, self.max_depth)
                #return      # Note: base case always need to return without recursive call

            # recursive case
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root)

        return self.max_depth

"""
AttributeError: 'NoneType' object has no attribute 'left'
        ^^^^^^^^^
    dfs(node.left, depth+1)
Line 20 in dfs (Solution.py)
    dfs(node.left, depth+1)
Line 20 in dfs (Solution.py)
    dfs(node.left, depth+1)
Line 20 in dfs (Solution.py)
    dfs(root)
Line 23 in maxDepth (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().maxDepth(param_1)
Line 45 in _driver (Solution.py)
    _driver()
Line 56 in <module> (Solution.py)
"""
        
