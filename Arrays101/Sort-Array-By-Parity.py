# https://leetcode.com/problems/sort-array-by-parity/description/
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_cnt = 0
        for i in range(len(nums)):
            if i - odd_cnt >= len(nums):
                break
            if nums[i-odd_cnt] % 2 == 1:
                odd_number = nums.pop(i-odd_cnt)
                nums.append(odd_number)
                odd_cnt += 1
                
        return nums