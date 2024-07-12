## Leetcode PlayLists

https://www.youtube.com/@UnNaGo

The recordings are without spoken words, instead typing sounds and peaceful music are included. This is to keep calm and write code focusing more on my thought process. You will find a certain length of annotations for each question, sometimes longer than its actual code, this is intentional as opposed to an immediate jump into answering questions. I start recordings by paraphrasing the question with my own words and then explain my problem-solving process based on the examples. While writing Python codes, sometimes I fix them if something is wrong or if typing errors by human nature. By the end of the writing code, I also added my test cases.

## Syntax Cheatsheet
### List
```python
215 l = [-x for x in nums]
67 l1 = [int(x) for x in a]
67 n1 = l1.pop() if l1 else 0
67 return "".join(l[::-1])
70 memo = [-1]*(n+1)
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

