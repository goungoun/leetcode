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
        Wrong Result!! Fix this!
        """
        if root:
            return True

        def dfs(node, min_val, max_val):
            # check current node is valid
            print(f"node.val={node.val if node else -1}")
            if not (min_val < node.val < max_val):
                return False
            
            # check left node is valid
            if node.left and not dfs(node.left, min_val, node.val):
                return False

            # check right node is valid
            if node.right and not dfs(node.right, node.val, max_val):
                return False

            return True

        return dfs(root, min_val=float('-inf'), max_val=float('inf'))

        

