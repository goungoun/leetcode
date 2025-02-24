# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stk = []
        stk.append((root.left,root.right))

        while stk:
            left, right = stk.pop()

            if (not left and right) or (not right and left) or \
                (left and right and left.val != right.val):
                return False
            elif left and right:
                stk.append((left.left, right.right))
                stk.append((left.right, right.left))    

        return True

# Follow up: Could you solve it both recursively and iteratively?
# See also: symmetric_tree.py

        
