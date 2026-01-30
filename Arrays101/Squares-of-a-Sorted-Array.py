# https://leetcode.com/problems/squares-of-a-sorted-array/description/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        start_pointer = 0
        end_pointer = len(nums) - 1
        
        
        while start_pointer < end_pointer:
            if nums[start_pointer] * nums[start_pointer] >= nums[end_pointer] * nums[end_pointer]:
                res.insert(0, nums[start_pointer]*nums[start_pointer])
                start_pointer += 1
            else:
                res.insert(0, nums[end_pointer]*nums[end_pointer])
                end_pointer -= 1
        
        res.insert(0, nums[start_pointer]*nums[start_pointer])
        
        return res