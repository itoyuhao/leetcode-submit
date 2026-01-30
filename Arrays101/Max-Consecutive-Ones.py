# https://leetcode.com/problems/max-consecutive-ones/description/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_record = 0
        current_consecutive = 0
        for i in nums:
            if i == 1:
                current_consecutive += 1
            else:
                if longest_record < current_consecutive:
                    longest_record = current_consecutive
                current_consecutive = 0
        
        if longest_record < current_consecutive:
            longest_record = current_consecutive
        
        return longest_record