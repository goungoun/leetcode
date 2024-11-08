# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Wrong Result!!
        root = [3,9,20,15,7]
        output = [3.00000,14.50000]
        expected = [3.00000,14.50000,11.00000]
        """
        if not root:
            return []

        q = deque([root])

        ret = []

        while q:
            #print(f"q={q}")
            tmp_sum = 0
            cnt = len(q)
            for _ in range(cnt):
                node = q.popleft()
                if node:
                    tmp_sum += node.val

            avg = tmp_sum/cnt if cnt != 0 else 0
            ret.append(avg)

            # Fix this!!! Where to put this code blocks?
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

        return ret
      
