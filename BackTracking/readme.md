## BackTracking Patterns
### Subsets (Powerset) - Exists Or not
```python
"""
nums = [1,2,3]
              [1]                []
      [1,2]        [1]        [2]   []
  [1,2,3] [1,2] [1,3] [1]  [2,3] [3]  []

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
        [1]          [2]            [3]           # add one
    [1,2] [1,3]     [2,1] [2,3]    [3,1] [3,2]    # add something different
  [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1] # add something different

len(nums) = 3 x 2 x 1 = 6
return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""
def dfs():
    if len(tmp) == len_nums:
        ret.append(tmp.copy())
    
    for i in range(len_nums):
        if nums[i] not in tmp: # condition for something different
            tmp.append(nums[i])
            dfs()
            tmp.pop()
```

### Combinations
https://leetcode.com/problems/combinations
