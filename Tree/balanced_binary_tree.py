# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if it is height-balanced
        return True (or False)

        Balanced if ∣h(left(N))−h(right(N))∣ ≤ 1

        Example 1: balanced
        root = [3,9,20,null,null,15,7]
        return True

        example 2: skewed
        root = [1,2,2,3,3,null,null,4,4]
        return False

        Approach: DFS postorder

        T=O(n)
        S=O(n) for call stack. If balanced, O(log n).
        """
        if not root:
            return True

        self.balanced = True

        def dfs(node):
            if not node or not self.balanced:
                return 0

            left, right = 0, 0

            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)

            if abs(left-right) > 1:
                self.balanced = False
            
            return max(left, right) + 1
        
        dfs(root)

        return self.balanced

