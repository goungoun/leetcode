# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### WARNING!!! This is a buggy code for a practice!!!

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A tree is considered balanced when:
        1) The height of the two sub-trees differs by at most one
        2) each sub-tree is balanced

        This code does not pass the example below:
        [1,2,2,3,null,null,3,4,null,null,4]

                1
              2  2
             3    3
            4      4

        This is not a balanced tree. So, it must return False.
        The reason for the failure is it does not check its sub-trees' balance recursively.
        """
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0

            left, right = 0, 0

            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)
            
            return max(left, right) + 1

        # Fix This: need to check within the recursion as a postorder
        height_left = dfs(root.right)
        height_right = dfs(root.left)

        is_balanced = abs(height_left - height_right) <= 1

        return is_balanced

