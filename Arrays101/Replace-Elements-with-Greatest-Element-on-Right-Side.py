1# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
2class Solution:
3    def replaceElements(self, arr: List[int]) -> List[int]:  
4        # Initialize the maximum value seen so far (starts with -1 for the last element)
5        max_so_far = -1
6      
7        # Traverse the array from right to left
8        for i in reversed(range(len(arr))):
9            # Store the current element before replacing it
10            current_element = arr[i]
11          
12            # Replace current element with the maximum element seen to its right
13            arr[i] = max_so_far
14          
15            # Update the maximum to include the current element
16            max_so_far = max(max_so_far, current_element)
17      
18        return arr