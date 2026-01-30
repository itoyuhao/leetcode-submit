# https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # approah 1: sort and iterate
        # nums.sort()
        
        # seen = nums[0]
        
        # for i in range(1, len(nums)):
        #     if nums[i] == seen:
        #         return seen
        #     else:
        #         seen = nums[i]
        
        # approach 2: Negative Marking

        # for num in nums:
        #     cur = abs(num)
        #     if nums[cur] < 0:
        #         duplicate = cur
        #         break
        #     nums[cur] = -nums[cur]
        
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])
        
        # return duplicate

        # approach 3: binary search
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        
        return duplicate