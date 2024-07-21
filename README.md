## Leetcode PlayLists

https://www.youtube.com/@goungouna

The recordings are without spoken words, instead typing sounds and peaceful music are included. This is to keep calm and write code focusing more on my thought process. 

## Syntax Cheatsheet
### List
```python
70 memo = [-1]*(n+1)
215 l = [-x for x in nums]
67 l1 = [int(x) for x in a]
67 n1 = l1.pop() if l1 else 0
67 return "".join(l[::-1])
58 return len(s.strip().split()[-1])
189 nums[:] = nums[-a:] + nums[:-a]
733 valid_adjs = [(r, c) for r, c in adjs if r >= 0 and c >= 0 and r < m and c < n]

6 # Unexpected behavior with this initialization: l = [[None] * n] * n
6 l = [[0 for _ in range(n)] for _ in range(n)]
```
### String
```python
9 # rs = "".join(list(reversed(s)))
9 return s == s[::-1]
```

### Queue
```python
637 from collections import deque
637 q = deque([root])
637 node = q.popleft()
637 q.append(node.left)
```

### Dictionary
```python
1 d = {}
1 if search in d: # O(1)
508 if n not in memo:

383 from collections import Counter
383 d = Counter(magazine)

6 d = {(0,0):s[0]} # key: (row,col), value: char
6 d[(row, col)] = c

1971 from collections import defaultdict
1971 graph = defaultdict(list)
1971 graph[u].append(v)
```

### Set
```python
14 s = set(t) # tuple is iterable
14 prefix.append(s.pop())
1971 visited = set([source])
```

### Heap
```python
215 import heapq
215 heapify(l)
215 smallest_val = heappop(l)
```

### Graph
```python
200 def numIslands(self, grid: List[List[str]]) # matrix
1971 def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
1971 edges = [[0,1],[1,2],[2,0]]
1971 graph = defaultdict(list)
     for u, v in edges:
       graph[u].append(v)
       graph[v].append(u)
```

### Zip
```python
14 z = zip(*strs)
```

### Loop
```python
704 l,r = 0, len(nums)-1 
704 while l <= r:

215 for _ in range(k):
```

### Swap
```python
344 s[l], s[r] = s[r], s[l]
266 root.left, root.right = root.right, root.left
```

### Exceptions
```python
70 raise ValueError (f"1 <= n <= 45, n={n}")

```

### Functions
```python
67 carry, r = divmod(n1 + n2 + carry,2)
```


## Errors
### RecursionError
RecursionError: maximum recursion depth exceeded in comparison
```python
200   grid[row][col] == "0" # Fix: grid[row][col] = "0"
```
### RuntimeError
Invalid Syntax <br>
NameError: Name mergeTwoLIsts is not defined <br>
TypeError: Solution.mergeTwoLists() takes 2 positional arguments but 3 were given
```python
23 def mergeTwoLIsts (list1, list2) # Fix: mergeTwoLIsts (self, list1, list2)
```
### TypeError
TypeError: divmod expected 2 arguments, got 1
```python
67 carry, r = divmod(n1 + n2 + carry) # Fix:  carry, r = divmod(n1 + n2 + carry, 2)
```
