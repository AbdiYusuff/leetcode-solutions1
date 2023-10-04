Use two pointers, left and right
Compute the sum of the left and right pointers
If the current sum is too small, move the left
pointer to the right by 1
If the current sum is too large, shift the right 
pointeter to the left by 1


numbers = [1,2,3,4,5]
       i = 0,1,2,3,4
           l     r
target - numbers[l] ? numbers[r]
target 4
  4    -     1      ?      5
              3    <       5
  4    -     1      ?      4
              3     <      4



target = 5
target - numbers[l] ? numbers[r]
5      -    1       ?    5
         4          <    5
      