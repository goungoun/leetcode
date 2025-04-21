# 1286. Iterator for Combination (Medium)
# https://leetcode.com/problems/iterator-for-combination

from itertools import combinations

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.iter = combinations(characters, combinationLength)
        self.nxt = next(self.iter, None)

    def next(self) -> str:
        res = self.nxt
        self.nxt = next(self.iter, None)
        return "".join(res)
        
    def hasNext(self) -> bool:
        return self.nxt is not None
