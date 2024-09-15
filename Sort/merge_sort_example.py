def merge(left, right):
  len_left = len(left)
  len_right = len(right)

  result = []
  left_idx = 0
  right_idx = 0

  while left_idx < len_left and right_idx < len_right:
    if left[left_idx] <= right[right_idx]:
      result.append(left[left_idx])
      left_idx += 1
    else:
      result.append(right[right_idx])
      right_idx += 1

  if left_idx == len_left:
    result.extend(right[right_idx:])
  elif right_idx == len_right:
    result.extend(left[left_idx:])

  return result

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid_idx = len(arr)//2
  left_arr = merge_sort(arr[:mid_idx])
  right_arr = merge_sort(arr[mid_idx:])

  return merge(left_arr, right_arr)

merge_sort([3,1,9,4,1])
