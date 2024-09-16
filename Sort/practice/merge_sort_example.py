def merge(arr1, arr2):
	idx1 = 0
	idx2 = 0
	len_arr1 = len(arr1)
	len_arr2 = len(arr2)

	ret = []

	while idx1 < len_arr1 and idx2 < len_arr2:
		val1 = arr1[idx1]
		val2 = arr2[idx2]
    
		if val1 >= val2:
			ret.append(val1)
			idx1 -= 1 # Fix This. DO NOT REMOVE IT. (infinit loop)
		else:
			ret.append(val2) 
			idx2 -= 1 # Fix This. DO NOT REMOVE IT. (infinit loop)

	if idx1 >= 0:
		ret.expand(arr1[idx1:]) # Fix This
	if idx2 >=0:
		ret.expand(arr2[idx2:]) # Fix This
	
	return ret
	
def merge_sort(arr):
	if len(arr) == 1:
		return arr
	
	mid = len(arr)//2
	left = merge_sort(arr[mid:])
	right = merge_sort(arr[:mid])
	
	return merge(left, right)

merge_sort([3,5,1,2,9])

"""
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[5], line 41
     38 	# conquer
     39 	return merge(left, right)
---> 41 merge_sort([3,5,1,2,9])

Cell In[5], line 35, in merge_sort(arr)
     33 # divide
     34 mid = len(arr)//2
---> 35 left = merge_sort(arr[mid:])
     36 right = merge_sort(arr[:mid])
     38 # conquer

Cell In[5], line 35, in merge_sort(arr)
     33 # divide
     34 mid = len(arr)//2
---> 35 left = merge_sort(arr[mid:])
     36 right = merge_sort(arr[:mid])
     38 # conquer

Cell In[5], line 39, in merge_sort(arr)
     36 right = merge_sort(arr[:mid])
     38 # conquer
---> 39 return merge(left, right)

Cell In[5], line 10, in merge(arr1, arr2)
      7 ret = []
      9 while idx1 < len_arr1 and idx2 < len_arr2:
---> 10 	val1 = arr1[idx1]
     11 	val2 = arr2[idx2]
     13 	if val1 >= val2:

IndexError: list index out of range
"""
