# 155. Min Stack (Medium)
# https://leetcode.com/problems/min-stack
class MinStack:
    """
    Implement a solution with O(1) time complexity for each function.

    Approach:
    In python, list works with O(1) for push, pop, top
    But, calling min for the list is O(n)
    Add and maintain a min_stack additionally
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # cf. min(self.stack) is O(n)
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
