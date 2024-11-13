# 1472. Design Browser History (Medium)
# https://leetcode.com/problems/design-browser-history

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.last = 0

    def visit(self, url: str) -> None:
        """
        T=O(1), S=O(1)
        """
        if not url:
            return

        if self.curr < len(self.history) -1:
            self.curr += 1
            self.history[self.curr] = url
            self.last = self.curr
        else:
            self.curr += 1
            self.history.append(url)
            self.last += 1

    def back(self, steps: int) -> str:
        """
        T=O(1), S=O(1)
        """
        if not steps:
            return

        self.curr -= steps
        self.curr = max(self.curr, 0)

        return self.history[self.curr]      

    def forward(self, steps: int) -> str:
        """
        T=O(1), S=O(1)
        """
        if not steps:
            return

        self.curr += steps
        self.curr = min(self.curr, self.last)

        return self.history[self.curr]
      
