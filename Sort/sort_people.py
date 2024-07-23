# 2418. Sort the People
# https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        Sort the peolpe with the heights, not names
        return list_names

        Example 1:
        names = ["Mary","John","Emma"], heights = [180,165,170]
        return ["Mary","Emma","John"]

        Example 2:
        names = ["Alice","Bob","Bob"], heights = [155,185,150]
        return ["Bob","Alice","Bob"]
        """
        l = sorted(list(zip(names, heights)), key=lambda item: item[1], reverse=True)
        return [name for name, height in l]
