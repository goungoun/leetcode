# 900. RLE Iterator (Medium)
# https://leetcode.com/problems/rle-iterator

from collections import deque

class RLEIterator:
    """
    Example:
    [3, 8, 0, 9, 2, 5]
    seq = [8, 8, 8, 5, 5]
    next(2): [8, 5, 5]
    next(1): [5, 5]
    next(1): [5]
    next(2): Exhausted

    return -1

    Approach:
    Create a sequence and put in a queue
    Whenevere next(n) is called, pop left   
    """
    def __init__(self, encoding: List[int]):
        self.seq = deque([])

        i = 0
        while i < len(encoding):
            cnt = encoding[i]
            val = encoding[i+1]
            self.seq.extend([val]*cnt)
            i += 2

        print(f"self.seq={self.seq}")

    def next(self, n: int) -> int:
        val = -1
        while n > 0:
            if self.seq:
                val = self.seq.popleft()
            else:
                val = -1
                break
                
            n -= 1

        return val
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
