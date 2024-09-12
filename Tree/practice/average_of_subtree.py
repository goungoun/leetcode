# 2265. Count Nodes Equal to Average of Subtree (Medium)
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        How many nodes has the value as an average of its subtree?
        return cnt_valid_nodes

        Example:
        root = [4,8,5,0,1,null,6]
              4
          8       5
        0   1  null 6  

        The node is valid if value has the average of its subtree.
        node.val=4: (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 (Valid)
        node.val=8: (8 + 0 + 1)/3 = 3 (Not valid, 8 !=3)
        node.val=5: (5 + 6) / 2 = 11 / 2 = 5. (Valid)
        node.val=0: 0 / 1 = 0. (Valid)
        node.val=1: 1 / 1 = 1. (Valid)
        node.val=6: 6 / 1 = 6. (Valid)

        Count valid nodes
        return 5

        Approach: DFS
        To calculate average of nodes, track two variable sum_vals and cnt_nodes for each nodes
        If there is no such left or right child, sum_val is the node.val itself and the node count is 1
        If there is a left or right child, recursive call to add the the sum and count of "subtrees"
        """

        if root is None:
            return 0

        self.cnt_valid_nodes = 0

        def dfs(node):
            sum_vals = node.val
            cnt_nodes = 1

            if node.left:
                # complete here #
            
            if node.right:
                # complete here #

            avg_vals = int(sum_vals/cnt_nodes)
            
            if avg_vals == node.val:
                self.cnt_valid_nodes += 1

            return (sum_vals, cnt_nodes)
        
        dfs(root)

        return self.cnt_valid_nodes
