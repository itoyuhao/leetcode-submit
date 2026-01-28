1# https://leetcode.com/problems/move-zeroes/description/
2class Solution:
3    def moveZeroes(self, nums: List[int]) -> None:
4        """
5        Do not return anything, modify nums in-place instead.
6        """
7        zero_cnt = 0
8        for i in range(len(nums)):
9            if i-zero_cnt >= len(nums):
10                break
11            if nums[i-zero_cnt] == 0:
12                nums.pop(i-zero_cnt)
13                nums.append(0)
14                zero_cnt += 1