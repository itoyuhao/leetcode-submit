# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:  
        # Initialize the maximum value seen so far (starts with -1 for the last element)
        max_so_far = -1
       
        # Traverse the array from right to left
        for i in reversed(range(len(arr))):
            # Store the current element before replacing it
            current_element = arr[i]
          
            # Replace current element with the maximum element seen to its right
            arr[i] = max_so_far
          
            # Update the maximum to include the current element
            max_so_far = max(max_so_far, current_element)
      
        return arr