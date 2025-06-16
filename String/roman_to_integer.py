# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert roman numerals to an original integer value
        return number

        Example 1: value decreasing case
        II -> 2
        XII -> 10 + 1 + 1 = 12
        XXVII -> 10 + 10 + 5 + 1 + 1 = 27
        
        Example 2: value increasing case
        IV(4), IX(9), XL(40), XC(90), CD(400), CM(900)

        IV -> 1 + 5 != 6
        IV -> -1 + 5 != 4

        XL -> 10 + 50 != 60
        XL -> -10 + 50 = 40
        
        CD -> 100 + 500 != 600
        CD -> -100 + 50 = 50 

        Appraoch:
        Define a dictionary to map symbol and value
        Ideas to cover the edge cases:
        - Add more symbols IV, IX, XL, XC, CD, CM into the dictionary
        - Rule based conditions for each I, X, C
        - Simply check if the value is increasing or not (v)
        """
        if not s:
            return 0

        # key: symbol, value: value
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000      
        }

        len_s = len(s)
        num = 0

        for i, symbol in enumerate(s):
            if (i+1) < len_s and d.get(symbol) < d.get(s[i+1]):
                num -= d[symbol] # value increasing edge case
            else:
                num += d[symbol] # generally value decreasing case

        return num
