class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Design and Implement LRU Cache

    Example 1:
    LRUCache(size=2) Head(dummy) <-> Tail(dummy)
    put(1,1)    Head(dummy) <-> Node(1,1) <-> Tail(dummy)
    put(2,2)    Head(dummy) <-> Node(1,1) <-> Node(2,2) <-> Tail(dummy)
    get(1)      Head(dummy) <-> Node(2,2) <-> Node(1,1) <-> Tail(dummy) return 1
    put(3,3)    Head(dummy) <-> Node(1,1) <-> Node(3,3) <-> Tail(dummy)
    get(2)      Head(dummy) <-> Node(1,1) <-> Node(3,3) <-> Tail(dummy) return -1
    put(4,4)    Head(dummy) <-> Node(3,3) <-> Node(4,4) <-> Tail(dummy)
    get(1)      Head(dummy) <-> Node(3,3) <-> Node(4,4) <-> Tail(dummy) return -1
    get(3)      Head(dummy) <-> Node(4,4) <-> Node(3,3) <-> Tail(dummy) return 3
    get(4)      Head(dummy) <-> Node(3,3) <-> Node(4,4) <-> Tail(dummy) return 4

    Approach: 
    Combine a doubly linked list and a dictionary
    Doubly linked list maintains the LRU order
    Dictionary provides O(1) key-to-node lookup  
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: key, value: addr of the node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _append(self, node: Node):
        # insert the node before the tail, always
        prev = self.tail.prev
        next = self.tail

        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def _delete(self, node: Node):
        # delete the node, it could be in the middle
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev  

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists.
        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
            node.value = value
            self._append(node)
        # Otherwise, add the key-value pair to the cache
        else:
            node = Node(key, value)
            self._append(node)
            self.cache[key] = node

            # Exceed capacity
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                del self.cache[lru_node.key]
                self._delete(lru_node)

        #print (f"self.cache={[(k, v.value) for k,v in self.cache.items()]}")    

        return
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        value = node.value

        # move the node to the end
        self._delete(node)
        self._append(node)

        return value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
