# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history

########### DEBUGGING PRACTICE ###########
class ListNode:    
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    """
    Warning!!! I made a buggy code to practice debug. This will be failing on the leetcode test cases.
    """
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        node.next = None # without it, it is already clear up the forward history
        self.curr = node

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            #print(f"self.curr.url={self.curr.url}, self.curr.prev={self.curr.prev.url}")
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.url
        
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
