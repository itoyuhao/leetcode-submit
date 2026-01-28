1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        res = 0
4        for i in range(len(nums)):
5            digits = self.digitCounter(nums[i])
6            if digits % 2 == 0:
7                res += 1
8        
9        return res
10    
11    @staticmethod
12    def digitCounter(s: int):
13        digit_cnt = 0
14        while s > 0:
15            digit_cnt += 1
16            s //= 10
17        
18        return digit_cnt