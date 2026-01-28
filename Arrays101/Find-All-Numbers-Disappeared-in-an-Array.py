1# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
2class Solution:
3    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
4        n = len(nums)
5
6        for i in range(n):
7            nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1]) 
8
9
10        res = []
11        for i in range(n):
12            if nums[i] > 0:
13                res.append(i+1)
14            
15        return res