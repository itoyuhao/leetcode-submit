1# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
2class Solution:
3    def findMin(self, nums: List[int]) -> int:
4        if len(nums) == 1:
5            return nums[0]
6        
7        left, right = 0, len(nums) - 1
8        
9        
10        while left < right:
11            if nums[left] < nums[right]:
12                return nums[left]
13        
14            mid = (left + right) // 2
15            
16            if nums[mid] > nums[right]:
17                left = mid + 1
18            else:
19                right = mid
20                
21        
22        return nums[left]