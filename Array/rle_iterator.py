# 900. RLE Iterator
# https://leetcode.com/problems/rle-iterator

from typing import List

class RLEIterator:
    """
    RLE Iterator
    return last_element
    
    Example 1:
    ["RLEIterator","next","next","next","next"]
    [[[3,8,0,9,2,5]],[2],[1],[1],[2]]

    RLEIterator [3,8,0,9,2,5]
    next(2) 3-2 = 1 return 8
    next(1) 1-1 = 0 return 8
    next(1) 2-1 = 1 return 5
    next(2) 1-2 = -1 return -1

    Example 2:
    ["RLEIterator","next","next","next","next","next","next"]
    [[[784,303,477,583,909,505]],[130],[333],[238],[87],[301],[276]]

    RLEIterator [784,303,477,583,909,505]

    next(130) 784-130=654 return 303
    next(333) 654-333=321 return 303
    next(238) 321-238=83 return 303

    next(87) (477+83)-87=473 return 583
    next(301) 473-301=172  return 583

    next(276) (172+909)-276 = 805 return 505

    Approach: 
    Do not decoding the given encoding which will improve the time and space complexity
    """

    def __init__(self, encoding: List[int]):
        if not encoding:
            return -1

        self.encoding = encoding
        self.len_encoding = len(encoding)
        self.cnt = 0
        self.val = 0
        self.i = 0     
        
    def next(self, n: int) -> int:
        if self.i > self.len_encoding -1 and self.cnt == 0:
            return -1
        
        if self.cnt == 0:           
            self.cnt = self.encoding[self.i]
            self.val = self.encoding[self.i+1]

            self.i += 2

        if self.cnt >= n:
            self.cnt = self.cnt - n
            return self.val
        else:
            n -= self.cnt
            self.cnt = 0
            return self.next(n) # recursive call


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

# Use this to debug the code in your editor
# rLEIterator = RLEIterator([3, 8, 0, 9, 2, 5]) 
# rLEIterator.next(2)
# rLEIterator.next(1) 
# rLEIterator.next(1)
# rLEIterator.next(2)
