1# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
2class Solution:
3    def searchRange(self, nums: List[int], target: int) -> List[int]:
4        
5        lower_bound = self.findBound(nums, target, isFirst=True)
6        if lower_bound == -1:
7            return [-1, -1]
8        
9        upper_bound = self.findBound(nums, target, isFirst=False)
10
11        return [lower_bound, upper_bound]
12
13    
14    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
15        n = len(nums)
16        begin, end = 0, n-1
17
18        while begin <= end:
19            mid = (begin + end) // 2
20
21            if nums[mid] == target:
22                
23                if isFirst:
24                    # This means we found our lower bound.
25                    if mid == begin or nums[mid - 1] < target:
26                        return mid
27                    # Search on the left side for the bound.
28                    end = mid - 1
29                else:
30                    # This means we found our upper bound.
31                    if mid == end or nums[mid + 1] > target:
32                        return mid
33                    begin = mid + 1
34            
35            elif nums[mid] > target:
36                end = mid - 1
37            
38            else:
39                begin = mid + 1
40
41        return -1
42