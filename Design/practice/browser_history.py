
# 1472. Design Browser History (Medium)
# https://leetcode.com/problems/design-browser-history
class BrowserHistory:
    """
    Design browser history
    Start from a homepage, visit url
    And then, back or forward the history

    Example 1:
    visit = [Leetcode, Google, Facebook, Youtube]
    back(1): Facebook
    back(1): Google
    forward(1): Facebook
    visits = [Leetcode, Google, Facebook, LinkedIn]
    forward(2): LinkedIn
    back(2): Google
    back(7): Leetcode

    Approach:
    History is a append only log.
    Use python list to append history which is O(1)
    To clear up the forward history is deleting tails, use pop() which is O(1)

    Beats 93.36%
    """

    def __init__(self, homepage):
        """
        Initializes the object with the homepage of the browser.
        """
        self.history = [?] ### Complete Here
        self.curr = 0
        
    def visit(self, url):
        """
        Visits url from the current page. It clears up all the forward history.
        """
        while ?: ### Complete Here
            self.history.pop()
         
        self.history.append(url)
        self.curr += ? ### Complete Here
    
    def back(self, steps):
        """
        Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
        """
        self.curr -= ? ### Complete Here
        self.curr = max(self.curr, 0)
        
        return self.history[self.curr]
    
    def forward(self, steps):
        """
        Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
        """
        self.curr += ? ### Complete Here
        self.curr = min(self.curr, ?) ### Complete Here

        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
