1# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
2class Solution:
3    def removeDuplicates(self, nums: List[int]) -> int:
4        n = len(nums)
5        k = 0
6        
7        for i in range(n-1):
8            if nums[i-k+1] - nums[i-k] == 0:
9                nums.pop(i-k)
10                k += 1
11        
12        return n - k
13
14
15
16
17
18
19