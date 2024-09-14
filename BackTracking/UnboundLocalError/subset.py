# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def recset(i):
            if i == len(nums):
                return ret.append(tmp.copy())

            tmp = [] # Fix this: Move this variable to the outside of the recset function
            
            tmp.append(nums[i])
            recset(i+1)

            tmp.pop()
            recset(i+1)

        recset(0)

        return ret

"""
UnboundLocalError: cannot access local variable 'tmp' where it is not associated with a value
                      ^^^
    return ret.append(tmp.copy())
Line 8 in recset (Solution.py)
    recset(i+1)
Line 13 in recset (Solution.py)
    recset(i+1)
Line 13 in recset (Solution.py)
    recset(i+1)
Line 13 in recset (Solution.py)
    recset(0)
Line 18 in subsets (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().subsets(param_1)
Line 40 in _driver (Solution.py)
    _driver()
Line 51 in <module> (Solution.py)
"""
