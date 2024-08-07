## Leetcode PlayLists
https://www.youtube.com/@goungouna <br>
The recordings are without spoken words, instead typing sounds and peaceful music are included.

## Syntax Cheatsheet
### String
```python
9 return s == s[::-1] # "".join(list(reversed(s)))
28 haystack.find(needle)
191 return str(bin(n))[2:].count('1')
```

### List
```python
70 memo = [-1]*(n+1)
215 l = [-x for x in nums]
67 return "".join(l[::-1])
58 return len(s.strip().split()[-1])
189 nums[:] = nums[-a:] + nums[:-a]
463 adj = [(row,col-1), (row,col+1), (row-1,col), (row+1,col)]
463 adj_land = [(r,c) for r,c in adj if 0 <= r < m and 0 <= c < n and grid[r][c]==1]
1051 expected.extend([i]*counter[i])

6 l = [[0 for _ in range(n)] for _ in range(n)] # Do not initialize l = [[None] * n] * n 
78 l_subsets.append(tmp.copy()) # Do not append list tmp itself
75 nums.clear() # nums[:] = []

from functools import reduce
136 return reduce(lambda x, y: x ^ y, nums, 0)

90 return list(map(list, ret)) # ret={(1, 2), (2,), (1,), (1, 2, 2), (2, 2), ()}
```

### Stack
```python
67 l1 = [int(x) for x in a]
67 n1 = l1.pop() if l1 else 0 # Add Binary
67 n2 = l2.pop() if l2 else 0

1971 stack = [source]
1971 while stack:
1971     vertex = stack.pop() # dfs
1971     stack.append(adj) 

77 tmp.append(num)
77 dfs(num + 1) 
77 tmp.pop() # backtracking
```

### Queue
```python
637 from collections import deque
637 q = deque([root])
637 node = q.popleft() # bfs
637 q.append(node.left)
67 return "".join(map(str, q))
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

207 d = defaultdict(list) # d = {i:[] for i in range(numCourses)}

12 d1.update(d2)
12 for k, v in sorted(d1.items(), reverse=True):

208 d = {'T':{'r':{'i':{'e':{'<END>':''}}, 'y':{'<END>':''}}}} # Trie
```

### Set
```python
3 while s[r] in dup_chk:
3 dup_chk.remove(s[l])
14 s = set(t) # tuple is iterable
14 prefix.append(s.pop())
1971 visited = set([source])
1971 visited.add(adj_vertex)
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
2418 l = sorted(list(zip(names, heights)), key=lambda item: item[1], reverse=True)
```

### Loop
```python
704 l,r = 0, len(nums)-1 
704 while l <= r:

215 for _ in range(k):

172 from functools import reduce
172 factorial = reduce(lambda a,b: a*b, range(1, n+1), 1)
```

### Swap
```python
344 s[l], s[r] = s[r], s[l]
266 root.left, root.right = root.right, root.left
48 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### Exceptions
```python
70 raise ValueError (f"1 <= n <= 45, n={n}")
```

### Functions
```python
67 carry, r = divmod(n1 + n2 + carry,2)
49 l[ord(c)-ord('a')] += 1  # ord() is inverse of chr()
209 min_length = min(min_length, r-l+1)
```

## Errors
### RecursionError
RecursionError: maximum recursion depth exceeded in comparison
```python
200 grid[row][col] == "0" # Fix: grid[row][col] = "0"
912 pivot = len(nums)//2 # Fix: pivot = nums[len(nums)//2]
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
