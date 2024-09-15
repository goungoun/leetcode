def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  mid_idx = len(arr)//2
  pivot = arr[mid_idx]

  left_arr = []
  mid_arr = []
  right_arr = []

  for num in arr:
    # complete here #
  
  return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)

quick_sort([3,1,9,4,1])
