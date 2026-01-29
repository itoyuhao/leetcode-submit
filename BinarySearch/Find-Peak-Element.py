1# https://leetcode.com/problems/find-peak-element/description/
2class Solution:
3    def findPeakElement(self, nums: List[int]) -> int:
4        
5        if len(nums) == 1:
6            return 0
7        
8        
9        left, right = 0, len(nums) - 1
10        
11        while left + 1 < right:  # 比到剩最後兩個再互相比較
12            
13            mid = (left + right) // 2
14            
15            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]: # 如果前後都比自己小 自己就是 peak 了
16                return mid
17            
18            if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:  # 如果還是 ascending order 就往右走
19                left = mid + 1
20            else:
21                right = mid # 如果不是ascending order( mid 可能是 valley 或 descending order ) 就往左走
22            
23        
24        return right if nums[right] > nums[left] else left
25                