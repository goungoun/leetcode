class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """
        Design LRU cache

        Example 1:
        head(dummy) <-> tail(dummy)
        insert node n(key:value) between them

        LRUCache(2)
        put(1,1)  head(dummy) <-> n(1:1) <-> tail(dummy) 
        put(2,2)  head(dummy) <-> n(1:1) <-> n(2:2) <-> tail(dummy) 
        get(1)    head(dummy) <-> n(2:2) <-> n(1:1) <-> tail(dummy) del&ins n(1:1) return 1
        put(3,3)  head(dummy) <-> n(1:1) <-> n(3:3) <-> tail(dummy) delete n(2:2)
        get(2)    head(dummy) <-> n(1:1) <-> n(3:3) <-> tail(dummy)
        put(4,4)  head(dummy) <-> n(3:3) <-> n(4:4) <-> tail(dummy) delete n(1:1) 
        get(1)    head(dummy) <-> n(3:3) <-> n(4:4) <-> tail(dummy) return -1
        get(3)    head(dummy) <-> n(4:4) <-> n(3:3) <-> tail(dummy) return 3
        get(4)    head(dummy) <-> n(3:3) <-> n(4:4) <-> tail(dummy) return 4

        Approach: double linkedlist + dictionary
        """
        self.capacity = capacity
        self.cache = {}

        # head(dummy) <-> tail(dummy)
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def _append(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to the most recently used position
        self._delete(node)
        self._append(node)

        #print(f"get({key}), self.head.next = {self.head.next.key}, self.cache={[(k, v.value) for k, v in self.cache.items()]}")

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # Move to most recently used position
            self._delete(node)            
            self._append(node)

        else:
            # New key
            node = Node(key, value)
            self.cache[key] = node
            self._append(node)

            # Capacity exceeded
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                del self.cache[lru_node.key]
                self._delete(lru_node)

        #print(f"put({node.value}), self.head.next = {self.head.next.key}, self.cache={[(k, v.value) for k, v in self.cache.items()]}")

        return
