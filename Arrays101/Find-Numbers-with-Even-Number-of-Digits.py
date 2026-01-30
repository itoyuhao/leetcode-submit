# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            digits = self.digitCounter(nums[i])
            if digits % 2 == 0:
                res += 1
        
        return res
    
    @staticmethod
    def digitCounter(s: int):
        digit_cnt = 0
        while s > 0:
            digit_cnt += 1
            s //= 10
        
        return digit_cnt