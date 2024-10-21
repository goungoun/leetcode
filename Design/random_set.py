# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1

from random import randint

class RandomizedSet:
    """
    Implement the RandomizedSet 
    For each function works in average O(1) time complexity

    Example:
    ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]

    [[],[1],[2],[2],[],[1],[2],[]]

    insert(1): [1] return True
    remove(2): [1] return False
    insert(2): [1,2] return True
    getRandom(): return 1 or 2
    remove(1): [2] return True
    getRandom(): return 2
    """

    def __init__(self):
        self.data = {} # key: val, value: idx
        self.dummy = []

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        """
        if val not in self.data:
            self.dummy.append(val)
            self.data[val] = len(self.dummy) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        """
        if val in self.data:
            last_idx = len(self.dummy)-1
            last_val = self.dummy[last_idx]

            idx = self.data[val]
            self.data[last_val] = idx
            self.dummy[idx] = last_val
            
            del self.data[val]
            self.dummy.pop()

            return True

        return False

    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
        """
        if self.data:
            idx = random.randint(0, len(self.dummy)-1)
            return self.dummy[idx]
        return
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
