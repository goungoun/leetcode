# X. Tower of Hanoi
# leetcode.com does not include the problem

class Solution:
  """
  Problem:
  Data Structures by RRichard F.Gilberg, Behrouz A.Forouzan p. 282-283
  
  The monks moved one disk to another needle each hour, subject to the following rules
  1. Only one disk could be moved at a time
  2. A larger disk must never be stacked above a smaller one
  3. One and only one auxiliary needle could be used for the intermediate storage of disk

  Approach: Top-down DP, recursive
  It's easier to simplify to have just two rods or to split them into two group
  One is the longest rod and the other is the shorter rods
  The other rods may include more rods actually, but it will be resolved by its recursive design
  
  -
  --

  Step 1: Move the shorter one from Start to the Temp. Be recursive until it is no longer splittable.
  --          -
  Start  End Temp

  Step 2: Move the "longest rod" directly to the End.
         --    -
  Start  End Temp

  Step 3: Move the shorter one from Temp to End. Be recursive until it is no longer splittable.
         -
         --  
  Start  End Temp
  """
  def hanoi(self, n, start='S', end='E', temp='T'):
    if n == 0:
      return
    self.hanoi(n-1, start, temp, end)
    print (f"Move disk '{n}' from the rod '{start}' to '{end}'")
    self.hanoi(n-1, temp, end, start)






"""
* Dry run to imagine the excution order is actually not easier than the algorithm design if n is more than 3.
Thought process should like this, group 1 is 3 and the group 2 is the other, 1 and 2.

1
2
3
-- -- --
S  E  T

The recursive call don't move 1 and 2 at once, move one disk per one call 

      1
3     2
-- -- --
S  E  T

Moving 3 from S to E does not require recursive call. It is just easy. 
      1
   3  2 
-- -- --
S  E  T

The recursive call don't move 1 and 2 at once, move one disk per one call
   1
   2
   3   
-- -- --
S  E  T



s = Solution()

Example 1: s.hanoi(n = 1)

1
-- -- --
S  E  T

Move disk '1' from the rod 'S' to 'E'

   1
-- -- --
S  E  T

# Example 2: s.hanoi(n=2)

1
2
-- -- --
S  E  T

Move disk '1' from the rod 'S' to 'T'


2     1
-- -- --
S  E  T

Move disk '2' from the rod 'S' to 'E'

   2  1
-- -- --
S  E  T

Move disk '1' from the rod 'T' to 'E'
   1
   2  
-- -- --
S  E  T


# Example 3: s.hanoi(n=3)

1
2
3
-- -- --
S  E  T

Move disk '1' from the rod 'S' to 'E'

2
3  1   
---------
S  E  T

Move disk '2' from the rod 'S' to 'T'


3  1  2  
---------
S  E  T


Move disk '1' from the rod 'E' to 'T'

      1 
3     2  
---------
S  E  T


Move disk '3' from the rod 'S' to 'E'

      1 
   3  2  
---------
S  E  T


Move disk '1' from the rod 'T' to 'S'

       
1  3  2  
---------
S  E  T

Move disk '2' from the rod 'T' to 'E'

   2
1  3    
---------
S  E  T


Move disk '1' from the rod 'S' to 'E'
   1
   2
   3    
---------
S  E  T
"""
