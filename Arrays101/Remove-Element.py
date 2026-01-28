1# https://leetcode.com/problems/remove-element/description/
2class Solution:
3    def removeElement(self, nums: List[int], val: int) -> int:
4        
5        n = len(nums)
6        p = 0
7        
8        for i in range(n):
9            if nums[i-p] == val:
10                nums.pop(i-p)
11                p += 1
12        
13        return n - p