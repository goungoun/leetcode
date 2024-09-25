# 71. Simplify Path
# https://leetcode.com/problems/simplify-path

from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Transform unix-style absolute path into simplified path
        return path
        """
        # It removes multiple consecutive slashes and trailing slash, but not enough
        # path_split = [x for x in path.split("/") if x != ""]
        
        path_split = deque([])

        for token in path.split("/"):
            if token == ".." and len(path_split) > 0:
                path_split.pop()
            elif token not in ['', '.']:
                path_split.append(token)

        if len(path_split) > 0 and path_split[-1] in ['..', '.']:
            path_split.pop()

        if len(path_split) > 0 and path_split[0] in ['..','.']:
            path_split.popleft()

        return "/" + "/".join(path_split)
