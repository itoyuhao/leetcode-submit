1# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
2class Solution:
3    def findMin(self, nums: List[int]) -> int:
4        if len(nums) == 1:
5            return nums[0]
6        
7        left, right = 0, len(nums) - 1
8        
9        while left < right:
10            
11            if nums[left] < nums[right]:  # not rotated array: return the most-left element
12                return nums[left]
13            
14            mid = (left + right) // 2
15            
16            # rotated array: fold and choose one side
17            if nums[mid] > nums[right]:
18                left = mid + 1
19            elif nums[mid] == nums[right]:  # the key is the determination when left == right
20                right -= 1  
21                left += 1
22            else:
23                right = mid
24        
25        return min(nums[left], nums[right])