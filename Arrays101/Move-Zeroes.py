# https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        for i in range(len(nums)):
            if i-zero_cnt >= len(nums):
                break
            if nums[i-zero_cnt] == 0:
                nums.pop(i-zero_cnt)
                nums.append(0)
                zero_cnt += 1