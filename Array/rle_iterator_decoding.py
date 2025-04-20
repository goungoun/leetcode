# 900. RLE Iterator (Medium)
# https://leetcode.com/problems/rle-iterator

from collections import deque

class RLEIterator:
    """
    Example:
    [3, 8, 0, 9, 2, 5]
    seq = [8, 8, 8, 5, 5]
    next(2): [8, 5, 5] 8
    next(1): [5, 5] 8
    next(1): [5] 5
    next(2): Exhausted -1

    return -1

    Approach:
    Create a sequence and put in a queue
    Whenevere next(n) is called, pop left
    """
    def __init__(self, encoding: List[int]):
        self.decoding = deque([])
        len_encoding = len(encoding)

        i = 0
        while i < len_encoding:
            cnt = encoding[i]
            val = encoding[i+1]
            if cnt > 0:
                self.decoding.append([val, cnt])
            i += 2

    def next(self, n: int) -> int:
        val = -1
        while n > 0:
            if not self.decoding:
                return -1

            val, cnt = self.decoding[0]
            self.decoding[0][1] -= n
            if self.decoding[0][1] <= 0:
                self.decoding.popleft()
            n -= cnt
            
        return val

# To solve this problem, we do not need to decode the encoding
# See also: rle_iterator.py


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
