## BackTracking Patterns
### Subsets (Powerset) - Exists Or not
```python
"""
nums = [1,2,3]
              [1]                []          # nums[0] Exists or not
      [1,2]        [1]        [2]   []       # nums[1] Exists or not
  [1,2,3] [1,2] [1,3] [1]  [2,3] [3]  []     # nums[2] Exists or not

return [[1,2,3],[1,2],[1,3],[1],[2,3],[3],[]]
"""
def dfs(i):
    if i == len_nums:
        return ret.append(tmp.copy())

    tmp.append(nums[i]) # Exists
    dfs(i+1) 
    tmp.pop() # Or not
    dfs(i+1)  
```
https://leetcode.com/problems/subsets

### Permutations - Something different
https://leetcode.com/problems/permutations
```python
"""
* array nums of distinct integers

nums = [1,2,3]
        [1]          [2]            [3]           # add something
    [1,2] [1,3]     [2,1] [2,3]    [3,1] [3,2]    # add something different
  [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1] # add something different

len(nums) = 3 x 2 x 1 = 6
return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""
def dfs():
    if len(tmp) == len_nums:
        ret.append(tmp.copy())
    
    for i in range(len_nums):
        if nums[i] not in tmp: # a condition for something different
            tmp.append(nums[i])
            dfs()
            tmp.pop()
```

### Combinations - Something different and remove duplicate
https://leetcode.com/problems/combinations
```python
"""
Approach: 
Not like permutation, nothing but different order is a duplicate in combination!

Combinations of k numbers chosen from the range [1, n]
n = 3, k = 3
nums = [i for i in range(1, n+1)]
nums = [1,2,3]
        [1]         [2]      [3]   # add something
    [1,2] [1,3]    [2,3]     [3]   # add larger than the existing one to remove duplicate
  [1,2,3]                          # add larger than the existing one to remove duplicate

return [[1,2,3]]
"""
def dfs():
    if len(tmp) == k:
        ret.append(tmp.copy())
        return

    for i in range(len_nums):
        if nums[i] > max(tmp, default=0): # to remove duplicate
            tmp.append(nums[i])
            dfs()
            tmp.pop()
```
