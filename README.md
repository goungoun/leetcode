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
```

### Dictionary
```python
1 d = {}
1 if search in d: # O(1)

383 from collections import Counter
383 d = Counter(magazine)
```

### Set
```python
14 s = set(t)
14 prefix.append(s.pop())
```

### Heap
```python
215 heapify(l)
215 smallest_val = heappop(l)
```

### Zip
```python
14 z = zip(*strs)
```

### Loop
```python
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

