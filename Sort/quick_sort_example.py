def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  mid_idx = len(arr)//2
  pivot = arr[mid_idx]

  left_arr = []
  mid_arr = []
  right_arr = []

  for num in arr:
    if num < pivot:
      left_arr.append(num)
    elif num > pivot:
      right_arr.append(num)
    else:
      mid_arr.append(num)

  return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)

quick_sort([3,1,9,4,1])
