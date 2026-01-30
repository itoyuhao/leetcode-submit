# https://leetcode.com/problems/max-consecutive-ones-ii/description/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_record = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeroes += 1
            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            
            max_record = max(max_record, right - left + 1)

            right += 1

        return max_record

        # n = len(nums)
        
        # life = 1
        # consecutive = 0
        # for i in range(n):
        #     if nums[i] == 1:
        #         consecutive += 1
        #     else:  # nums[i] == 0
        #         if life:
        #             life = 0
        #             consecutive += 1
        #             what_if = 1
        #         else:
        #             life = 1
        #             if consecutive > max_record:
        #                 max_record = consecutive
        #             consecutive = 0
        
        # if consecutive > max_record:
        #     max_record = consecutive
        
        # return max_record