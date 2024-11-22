# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder Traversal
        return seq_val

        Example:
        root = [1,null,2,3]
        return [1, 3, 2]

        Approach: DFS

        T=O(n), S=O(n)
        """
        if not root:
            return []

        ret = []

        def dfs(node):
            if not node:
                return

            if node.left:
                dfs(node.left)
            
            ret.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)

        return ret

