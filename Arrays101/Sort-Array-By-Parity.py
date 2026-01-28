1# https://leetcode.com/problems/sort-array-by-parity/description/
2class Solution:
3    def sortArrayByParity(self, nums: List[int]) -> List[int]:
4        odd_cnt = 0
5        for i in range(len(nums)):
6            if i - odd_cnt >= len(nums):
7                break
8            if nums[i-odd_cnt] % 2 == 1:
9                odd_number = nums.pop(i-odd_cnt)
10                nums.append(odd_number)
11                odd_cnt += 1
12                
13        return nums