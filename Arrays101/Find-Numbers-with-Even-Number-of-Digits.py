1# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
2class Solution:
3    def findNumbers(self, nums: List[int]) -> int:
4        res = 0
5        for i in range(len(nums)):
6            digits = self.digitCounter(nums[i])
7            if digits % 2 == 0:
8                res += 1
9        
10        return res
11    
12    @staticmethod
13    def digitCounter(s: int):
14        digit_cnt = 0
15        while s > 0:
16            digit_cnt += 1
17            s //= 10
18        
19        return digit_cnt