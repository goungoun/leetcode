# 1286. Iterator for Combination (Medium)
# https://leetcode.com/problems/iterator-for-combination

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.itr = self._combination(characters, combinationLength)
        self.nxt = next(self.itr, None)

    def _combination(self, characters: str, combinationLength: int) -> Generator[str, None, None]:
        tmp = []
        end = len(characters)

        def dfs(start):
            if len(tmp) == combinationLength:
                yield "".join(tmp)
                return

            for i in range(start, end):
                tmp.append(characters[i])
                yield from dfs(i+1)
                tmp.pop()

        yield from dfs(0)

    def next(self) -> str:
        nxt_combi = self.nxt
        self.nxt = next(self.itr, None)

        return nxt_combi

    def hasNext(self) -> bool:
        return self.nxt is not None
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
