# Leet code for Knap Sack problem is not found. 
# So, I wrote the python code for my practice after watching Tushar Roy's solution.
# https://www.youtube.com/watch?v=8LusJS5-AGo&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2

n_items = 4
values = [1,4,5,7]
weights = [1,3,4,5]
weight_limit = 7

T = [[0] * (weight_limit+1) for _ in range(n_items)]

for r in range(n_items):
    for c in range(weight_limit + 1):
        if r == 0:
            T[0][c] = values[0] if c >= weights[0] else 0
        else:
            add = values[r] + T[r-1][c - weights[r]] if c >= weights[r] else 0
            or_not = T[r-1][c]
            T[r][c] = max(add, or_not)

import numpy as np
print(np.array(T))

"""
[[0 1 1 1 1 1 1 1]
 [0 1 1 4 5 5 5 5]
 [0 1 1 4 5 6 6 9]
 [0 1 1 4 5 7 8 9]]
"""
