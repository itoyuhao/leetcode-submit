1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        longest_record = 0
4        current_consecutive = 0
5        for i in nums:
6            if i == 1:
7                current_consecutive += 1
8            else:
9                if longest_record < current_consecutive:
10                    longest_record = current_consecutive
11                current_consecutive = 0
12        
13        if longest_record < current_consecutive:
14            longest_record = current_consecutive
15                    
16        
17        return longest_record
18                    
19                