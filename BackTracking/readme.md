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

### Permutations
https://leetcode.com/problems/permutations

### Combinations
https://leetcode.com/problems/combinations
