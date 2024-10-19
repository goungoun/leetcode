# 146. LRU Cache (Medium)
# https://leetcode.com/problems/lru-cache

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import ? # Complete here

class LRUCache:
    """
    Design LRU Cache with a capacity limitation
    get() and put() must run in O(1)
    
    Example:
    ["LRUCache","put","put","get","put","get","put","get","get","get"]
    [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    
    LRUCache: capacity = 2
    put(1,1) => {1:1}
    put(2,2) => {1:1, 2:2}
    get(1) => return 1, {2:2, 1:1} 
    put(3, 3) => {1:1, 3:3}
    get(2) => return -1, {1:1, 3:3}
    put(4, 4) => {3:3, 4:4}
    get(1) => return -1 {3:3, 4:4}
    get(3) => return 3 {4:4, 3:3}
    get(4) => return 4 {3:3, 4:4}
    
    Approach:
    Used built-in data structure in python, ordered dictionary
    Whenever put or get called, move the value to the end
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError(f"capacity must be a positive integer. capacity={capacity}")

        self.cache = {} # Fix here
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.
        """
        if key not in self.cache:
            return -1
        else:
            # Do not pop or remove it. Just return the value, but need to be "touched".
            # Instead we can use ordered dict built-in method: self.cache.?????(key)
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
          
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. 
        Otherwise, add the key-value pair to the cache. 
        
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        if key in self.cache:
            # self.cache..?????((key)
            del self.cache[key]
          
        self.cache[key] = value

        """
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: dict.popitem() takes no keyword arguments
        """
      
        if len(self.cache) > self.capacity:
            # evict the least recently used key, either get or put
            self.cache.popitem(last=False)

# Referenced and updated an idea of using ordered dict from a leet code user, deleted_user 
