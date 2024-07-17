# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Minimum absolute difference between the values
        return min_diff

        Approach:
        Do inorder traversal of the binary search tree to get the sorted list l
        Iterate the list and diff l[i] and l[i-1]
        Update the min_difference in each iteration

        Example:
        root = [4,2,6,1,3]
            4
          2   6
        1   3

        DFS traversal result
        l = [1,2,3,4,6]
        diff = l[i+1] - l[i]
        2-1 = 1
        3-2 = 1
        4-3 = 1
        6-4 = 2

        return 1
        """

        min_diff = 100001
        l = []

        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            l.append(root.val) # inorder
            dfs(root.right)
        
        dfs(root)
 
        for i in range(len(l)-1):
            min_diff = min(min_diff, l[i+1] - l[i])
   
        return min_diff
