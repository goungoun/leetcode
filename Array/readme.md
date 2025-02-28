### Slice assignment
Slice assignment selects a specific portion of the list and replaces it with new values, directly modifying the original list object.
```python3
189 nums[:] = nums[-k:] + nums[:-k]

>>> l1 = [1,2,3]
>>> l2 = [10,20,30]
>>> l1[1:2]
[2]
>>> l1[1:2] = l2
>>> l1
[1, 10, 20, 30, 3]
>>> l2[1] = 200
>>> l2
[10, 200, 30]
>>> l1
[1, 10, 20, 30, 3]
```
