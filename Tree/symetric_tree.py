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
        Validate if the given tree is symmetric

        Example:
        root = [1,2,2,3,4,4,3]
                   1
               2       2
             3   4   4   3 
        return True 

        root = [1,2,2,null,3,null,3]
                   1
            2           2
               3           3
        return False

        Approach:
        Split out two trees from the left and right of the root
        Flip the right tree recursively
        Traverse the left tree and compare its value with a value from the right tree
        """

        l = root.left
        r = root.right

        self.flip(r)
        
        return self.comp(l, r)
    
    def flip(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.flip(root.left)
        self.flip(root.right)
    
    def comp(self, l, r):
        if (not l and r) or (not r and l) or (l and r and l.val != r.val):
            return False
        elif l and r:
            if not self.comp(l.left, r.left):
                return False
            if not self.comp(l.right, r.right):
                return False
        return True


            
