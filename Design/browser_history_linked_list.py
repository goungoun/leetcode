# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history

class VisitNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None
        
class BrowserHistory:
    """
    Design browser history
    Start from a homepage, visit url
    And then, back or forward the history
    
    Approach: Double linked list

    T=O(1) for visit()
    T=O(steps) for back() and forward(), it is up to 100 steps
    
    S=O(n)

    Beats 53.85%
    """
    def __init__(self, homepage: str):
        self.curr = VisitNode(homepage)

    def visit(self, url:str) -> None:
        """
        Visits url from the current page. 
        It clears up all the forward history.

        self.curr <=(link)=> new_node
        """
        # Create a new node with the given url
        new_node = VisitNode(url)

        # Link up the current node and the new one, bi-directionally (Double linked list)
        self.curr.next = new_node
        new_node.prev = self.curr

        # Update the current node to a new node
        self.curr = new_node
        
    def back(self, steps: int) -> str:
        """
        Move steps back in history. 
        If you can only return x steps in the history and steps > x, you will return only x steps. 
        Return the current url after moving back in history at most steps.
        """
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.url

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. 
        If you can only forward x steps in the history and steps > x, you will forward only x steps. 
        Return the current url after forwarding in history at most steps.
        """
        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Referenced and updated a solution by leetcode user 101leetcode
# https://leetcode.com/problems/design-browser-history/solutions/674447/python-very-simple-solution-using-double-linked-list/
