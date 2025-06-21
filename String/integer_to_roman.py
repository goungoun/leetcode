# 12. Integer to Roman (Medium)
# https://leetcode.com/problems/integer-to-roman

class Solution:
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
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""

        ret = []
        weight = 1

        d = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M",
            4: "IV", 9:"IX", 40:"XL", 90:"XC", 400: "CD", 900: "CM"}

        while num > 0:
            num, value = divmod(num, 10)
            if value in [4,9]:
                ret.append(d.get(weight*value))
            elif value >=5 and value < 10: # 700 = 500 *1  + 100*2
                ret.append(d[weight]*(value-5))
                ret.append(d[5*weight])     
            else:
                ret.append(d.get(weight)*value)
            
            weight *= 10

        return "".join(reversed(ret))

