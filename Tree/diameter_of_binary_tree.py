# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Diameter of a binary tree
        return max_diameter

        Example:
        root = [1,2,3,4,5]
                      1(3)
               2(1)          3(0)
          4(0)    5(0) 

        return 3

        Approach: DFS, Post-Order traversal
        Use recursive call to traverse the nodes in the tree
        It goes down from the root to leaf node, if it goes more then a leaf node return 0
        After visiting left and right child, finally calculate its diameter for each node and update max_diameter
        """
        
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            len_l = dfs(node.left)
            len_r = dfs(node.right)

            self.max_diameter = max(len_l+len_r, self.max_diameter) 

            return max(len_l, len_r) + 1

        dfs(root)

        return self.max_diameter
      
