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
        """
        check whether it is symmetric or not
        return True/False

        Example 1: symmetric
        root = [1,2,2,3,4,4,3]
                 1
              2    2
            3  4  4  3

        return True

        Example 2: Not symmetric
        root = [1,2,2,null,3,null,3]

               1
            2     2
        null 3    null 3

        return False

        Approach: recursive
        """
        self.is_symmetric = True

        def rec_compare(left, right):
            if (not left and right) or \
                (not right and left) or \
                (left and right and left.val != right.val):
                self.is_symmetric = False
                return

            if left and right:
                rec_compare(left.left, right.right)
                rec_compare(left.right, right.left)

        rec_compare(root.left, root.right)

        return self.is_symmetric
        
    # Follow up: Could you solve it both recursively and iteratively?
    # See also: symetric_tree_iterative.py
