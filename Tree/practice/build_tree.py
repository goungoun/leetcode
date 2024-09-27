# 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Re-build a binary tree from a preorder and an inorder list
        return root (of the tree)

        Example: 
        preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
                  3
            9          20
        None  None   15    7

       [3, 9, 20, None, None, 15, 7]

        * The array notation of a tree follows the rule l=(i*2)+1, r=(i*2)+2
        * preorder or inorder itself is not a tree

        Approach: 
        The root is the first element of the preorder
        Build a preorder queue, pop it in order from the left, this is the mid
        Build a value-idx dictionary to get the mid idx from the inorder list
        Get the left and the right using resursive call with the decreased scope
        """
        if not preorder or not inorder:
            return None

        q = deque(preorder)
        d = dict([(val,idx) for idx,val in enumerate(inorder)]) # Optimize it. Build a dictionary directly

        def build(start, end):
            if start > end:
                return None

            root = TreeNode(q.popleft())
            mid_idx = d[root.val]

            root.left = ? # Complete this
            root.right = ? # Complete this

            return root

        return build(0, len(preorder) -1)
