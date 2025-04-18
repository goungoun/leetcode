# 622. Design Circular Queue (Medium)
# https://leetcode.com/problems/design-circular-queue/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    """
    Design circular queue (aka. Ring Buffer)
    1) It is a queue : FIFO (First In First Out)
    2) It is a cicle: The last is connected to the first

    * attributes: front, rear, capacity, size
    * operations: enQueue, deQueue, (get)Front, (get)Rear, isEmpty, isFull

    Example 1: capacity=3
    isEmpty() return True
    enQueue(1) return True <- Front
    enQueue(2) return True
    enQueue(3) return True <- Rear
    enQueue(4) return False // above the capaicty, just return False
    Rear() return 3
    isFull() return True
    deQueue() return True
    enQueue(4) return True
    Rear() return 4

    T=O(1) for all operations, beats 79.43
    S=O(n) for a single linked list, beats 10.88
    """

    def __init__(self, k: int):
        self.capacity = k
        self.front = self.rear = None
        self.length = 0

    def __len__(self):
        return self.length

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. 
        Return true if the operation is successful.
        """
        if self.isFull():
            return False

        n = ListNode(value)

        if self.isEmpty():
            self.rear = self.front = n
        else:
            self.rear.next = n # link the end node and the new node 
            self.rear = n # the new node becomes the rear
        
        self.rear.next = self.front # circle back
        self.length += 1

        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. 
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        # remove the front because it is FIFO
        self.front = self.front.next

        self.rear.next = self.front # circle back 
        self.length -= 1

        return True  

    def Front(self) -> int:
        """
        Gets the front item from the queue. 
        If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1

        return self.front.val

    def Rear(self) -> int:
        """
        Gets the last item from the queue. 
        If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1

        return self.rear.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity
        
