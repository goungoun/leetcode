# 12. Integer to Roman (Medium)
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
        First decompose numbers into each number and the weight
        If the value is more than 5 and less than 9, decompose one more time
        Find the right character from the value-symbol map and repeat
        """
        if not num or not isinstance(num, int):
            return ""       

        # Step 1. decompose
        decompose = [] 
        weight = 1

        while num > 0:
            num, value = divmod(num, 10)

            if value >= 5 and value < 9:
                decompose.append((value-5, weight))
                decompose.append((1, 5 * weight))
            else:
                decompose.append((value, weight))
            weight *= 10

        # Step 2. get symbols from a dictionary
        d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500: 'D', 1000:'M',
            4:'IV', 9: 'IX', 40: 'XL',90: 'XC', 400: 'CD', 900: 'CM'}

        n = len(decompose)
        res = []

        for i in range(n-1, -1, -1):
            if decompose[i][0] in [4,9]:
                symbol = d.get(decompose[i][1]*decompose[i][0])
            else:
                symbol = d.get(decompose[i][1])*decompose[i][0]

            res.append(symbol)

        return "".join(res)

