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
    """

    def __init__(self, k: int):
        self.capacity = k
        self.front = self.rear = None
        self.size = 0

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
            self.rear.next = n      
            self.rear = n
        
        self.rear.next = self.front # circle back
        self.size += 1

        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. 
        Return true if the operation is successful.
        """
        if self.size == 0:
            return False

        if self.size == 1:
            self.front = self.rear = None
            self.size = 0
        else:
            self.front = self.front.next
            self.rear.next = self.front
            self.size -= 1

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
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        
