# Leetcode PlayLists
https://www.youtube.com/@UnNaGo

# Syntax Cheatsheet
## List
67 return "".join(l[::-1])
215 l = [-x for x in nums]
67 l1 = [int(x) for x in a]
67 n1 = l1.pop() if l1 else 0
70 memo = [-1]*(n+1)

## Set
14 s = set(t)
14 prefix.append(s.pop())

## Heap
215 heapify(l)
215 smallest_val = heappop(l)

## Zip
z = zip(*strs)

# Loop
215 for _ in range(k):

# Swap
344 s[l], s[r] = s[r], s[l]
266 root.left, root.right = root.right, root.left

## Exception
70 raise ValueError (f"1 <= n <= 45, n={n}")

## Function
67 carry, r = divmod(n1 + n2 + carry,2)

