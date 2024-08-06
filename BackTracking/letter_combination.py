# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Letter Combinations of a Phone Number
        return possible_letters

        Approach:
        Build a tree and use backtracking
        The leaf node will have the combination
        All possible combination means no condition applicable for a pruning

        Example:
        digits = "23"
        2 is mapped to abc, 3 is mapped to def
        
        L1:        [a]              [b]             [c]
        L2:  [a,d] [a,e] [a,f] [b,d] [b,e] [b,f] [c,d] [c,e] [c,f]

        return ["ad","ae","af","bd","be","bf","cd","cd","cf"]
        """

        if digits is None or len(digits) == 0:
            return []

        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}

        ret = []
        tmp = []
        len_digits = len(digits)

        def dfs(i):
            if len(tmp) == len_digits:
                ret.append("".join(tmp))
                return

            for c in d.get(digits[i]):
                tmp.append(c)
                dfs(i+1)
                tmp.pop()
        
        dfs(0)

        return ret
