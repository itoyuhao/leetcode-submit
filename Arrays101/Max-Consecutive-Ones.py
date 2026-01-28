1# https://leetcode.com/problems/max-consecutive-ones/description/
2class Solution:
3    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
4        longest_record = 0
5        current_consecutive = 0
6        for i in nums:
7            if i == 1:
8                current_consecutive += 1
9            else:
10                if longest_record < current_consecutive:
11                    longest_record = current_consecutive
12                current_consecutive = 0
13        
14        if longest_record < current_consecutive:
15            longest_record = current_consecutive
16                    
17        
18        return longest_record
19                    
20                