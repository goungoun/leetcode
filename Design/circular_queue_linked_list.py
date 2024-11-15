# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        if not k or not (1 <= k <= 1000):
            raise ValueError (f"1 <= k <= 1000, k={k}")

        self.k = k
        self.dummy = ListNode(None)
        self.front = self.dummy 
        self.rear = self.dummy
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. 
        Return true if the operation is successful.
        """
        if self.isFull():
            return False

        n = ListNode(value)

        if self.cnt == 0:
            self.rear = n
            self.front = n

        else:
            self.rear.next = n      
            self.rear = n
        
        self.rear.next = self.front
        self.cnt += 1

        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. 
        Return true if the operation is successful.
        """
        if not self.cnt:
            return False

        if self.cnt == 1:
            self.dummy = ListNode(None)
            self.front = self.dummy 
            self.rear = self.dummy  # cannot be self.front
            self.cnt = 0
        else:
            if self.front.next: 
                self.front = self.front.next
            self.rear.next = self.front 
            self.cnt -= 1 

        return True      

    def Front(self) -> int:
        """
        Gets the front item from the queue. If the queue is empty, return -1.
        """
        if self.front is None or self.front.val is None:
            return -1

        return self.front.val

    def Rear(self) -> int:
        """
        Gets the last item from the queue. If the queue is empty, return -1.
        """
        if self.rear is None or self.rear.val is None:
            return -1

        return self.rear.val

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
