# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert given num to a Roman String
        return roman_string

        Example 1:
        num = 3749

        3000 = MMM
        700 = DCC
        40 = XL
        9 = IX

        return "MMMDCCXLIX"

        Example 2:
        num = 58
        50 = L
        8 = VIII

        return "LVIII"

        Approach:
        Create a dictionary to map a value to symbol
        Sort the dictionary decreasing order
        Decompose given num by divide the key to get mapped characters
        """
        d1 = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500: 'D', 1000:'M'}
        d2 = {4:'IV', 9: 'IX', 40: 'XL',90: 'XC', 400: 'CD', 900: 'CM'}

        d1.update(d2)
        ret = []

        for k, v in sorted(d1.items(), reverse=True):
            s, r = divmod(num,k)
            if s > 0:
                ret.append(v*s)
                num -= k*s

        return "".join(ret)
