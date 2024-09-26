# 71. Simplify Path (Medium)
# https://leetcode.com/problems/simplify-path

from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Transform unix-style absolute path into simplified path
        return simple_path

        Example:
        /home/ => /home
        /home//foo/ => /home/foo
        /home/user/Documents/../Pictures => /home/user/Pictures
        /../ => /
        /.../a/../b/c/../d/./ => /.../b/d
        /a/./b/../../c/ => /a/./b/../../c/
        /a/../../b/../c//.// => /c

        Approach:
        Iterate tokens by splitting a path using '/'
        Append a token to a double ended queue(deque) if it is valid or remove the previous one if it is ".."
        Remove trailing and starting periods with O(1) from the deque
        """
        # It removes multiple consecutive slashes and trailing slash, but not enough
        # path_split = [x for x in path.split("/") if x != ""]
        
        if path is None or path.strip() == "":
            return ""

        path_split = deque([])
        
        for token in path.split("/"):
            if token == ".." and len(path_split) != 0:
                path_split.pop()
            elif token not in ['', '.']:
                path_split.append(token)
        
        # remove trailing periods
        while path_split and path_split[-1] in ["..", "."]:
            path_split.pop()

        # remove starting periods
        while path_split and path_split[0] in ["..", "."]:
            path_split.popleft()

        simple_path = "/" + "/".join(path_split)

        return simple_path
