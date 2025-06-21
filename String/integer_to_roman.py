# 12. Integer to Roman (Medium)
# https://leetcode.com/problems/integer-to-roman

class Solution:
    """
    Convert a decimal place value into a Roman numeral
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
    First decompose decimal place value into each digit and its place value
    If the value is more than 5 and less than 9, decompose one more time
    Find the right character from the value-symbol map and repeat
    """
    def intToRoman(self, num: int) -> str:
        if not num or not 1 <= num <= 3999:
            raise ValueError("Valid range: 1 <= num <= 3999, num={num}")

        ret = []
        
        d = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M",
            4: "IV", 9:"IX", 40:"XL", 90:"XC", 400: "CD", 900: "CM"}

        place = 1
        while num > 0:
            num, digit = divmod(num, 10) # digit range: 0 ~ 9
            if digit in [4,9]:
                ret.append(d.get(place*digit))
            elif digit >=5 and digit < 10: # e.g 700 = 500 *1 + 100*2
                ret.append(d[place]*(digit-5))
                ret.append(d[5*place])
            else:
                ret.append(d.get(place)*digit)
            
            place *= 10

        return "".join(reversed(ret))

