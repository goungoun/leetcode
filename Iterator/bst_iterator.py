# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/description/?envType=problem-list-v2&envId=iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)
    
    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        """
        Generator function that takes the root node of a binary tree
        and iterates through the nodes of the tree via inorder traversal.
        """
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)
        
    def next(self) -> int:
        """
        Moves the pointer to the right, then returns the number at the pointer.
        """
        res, self.nxt = self.nxt, next(self.iter, None)
        return res
        
    def hasNext(self) -> bool:
        """
        Check the existence a number in the traversal to the right
        Returns True/False 
        """
        return self.nxt is not None
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# referenced a solution by Zayne Siew
# https://leetcode.com/problems/binary-search-tree-iterator/solutions/1965156/python-tc-o-1-sc-o-h-generator-solution/?envType=problem-list-v2&envId=iterator
