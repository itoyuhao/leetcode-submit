1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        
6        if len(nums) == 1:
7            return 0 if nums[0] == target else -1
8        
9        while right - left >= 1:
10            middle = (left + right) // 2
11            
12            if right - left == 1:
13                if nums[left] == target:
14                    return left
15                if nums[right] == target:
16                    return right
17                return -1
18            
19            if nums[middle] == target:
20                return middle
21            if nums[middle] < target:
22                left = middle
23            else:
24                right = middle
25        
26        return -1