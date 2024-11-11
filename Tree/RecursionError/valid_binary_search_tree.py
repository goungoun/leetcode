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
        """
        RecursionError: maximum recursion depth exceeded in comparison
        Previous line repeated 996 more times
        
        Hint: Which node is repeating?!!

        Example:
        root = [32,26,47,19,null,null,56,null,27]
        """
        if not root:
            raise ValueError ("expected 'root' to have 1 <= size <= 10000 but got 0")

        self.cnt = 0
      
        def dfs(node, min_val, max_val):
            print(f"self.cnt={self.cnt}, node={node.val}, min_val={min_val}, max_val={max_val}")
            self.cnt += 1
          
            if (root.left and root.left.val >= root.val) or \
                (root.right and root.val >= root.right.val):
                return False   
            
            if node.val <= min_val or node.val >= max_val:
                return False 

            if node.left and not dfs(root.left, min_val , root.val):
                return False
            
            if node.right and not dfs(root.right, node.val, max_val):
                return False
            
            return True

        return dfs(root, float('-inf'), float('inf'))
        

"""
RecursionError: maximum recursion depth exceeded in comparison
       ^^^^^^^^^^^^^^^^^^^
    if node.val <= min_val or node.val >= max_val:
Line 18 in dfs (Solution.py)
  [Previous line repeated 996 more times]
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    if node.left and not dfs(root.left, min_val , root.val):
Line 21 in dfs (Solution.py)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    if node.left and not dfs(root.left, min_val , root.val):
Line 21 in dfs (Solution.py)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    if node.left and not dfs(root.left, min_val , root.val):
Line 21 in dfs (Solution.py)

Hint: Which node is repeating?!!
self.cnt=0, node=32, min_val=-inf, max_val=inf
self.cnt=1, node=26, min_val=-inf, max_val=32
self.cnt=2, node=26, min_val=-inf, max_val=32
self.cnt=3, node=26, min_val=-inf, max_val=32
self.cnt=4, node=26, min_val=-inf, max_val=32
self.cnt=5, node=26, min_val=-inf, max_val=32
self.cnt=6, node=26, min_val=-inf, max_val=32
self.cnt=7, node=26, min_val=-inf, max_val=32
"""
