# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1

from random import randint

def log_self_value(method):
    def wrapper(self, *args, **kwargs):
        print(f"Bf {method.__name__}: self.rset = {self.rset}")
        result = method(self, *args, **kwargs)
        print(f"Af {method.__name__}: self.rset = {self.rset}")
        return result

    return wrapper

class RandomizedSet:
    """
    Insert Delete GetRandom O(1)
    """
    def __init__(self):
        self.rset = {} #key: val, value: idx
        self.dummy = []

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present. 
        Returns true if the item was not present, false otherwise.
        """
        if val in self.rset:
            return False

        self.dummy.append(val)
        last_idx = len(self.dummy) -1
        self.rset[val] = last_idx

        return True

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. 
        Returns true if the item was present, false otherwise.
        """
        if val not in self.rset:
            return False

        idx = self.rset[val]
        self.dummy[idx] = None ### Improve This: it will going to be larger if remove repeated
        del self.rset[val]

        return True
        
    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
        """
        rndkey = None
        # Best: T=O(1) ~ Worst: T=O(n)
        ### Improve This: Worst T=O(n) -> T=O(1)      
        while rndkey is None:
            rndidx = random.randint(0, len(self.dummy)-1)
            rndkey = self.dummy[rndidx]
            #print(f"rndkey={rndkey}")

        return rndkey


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
