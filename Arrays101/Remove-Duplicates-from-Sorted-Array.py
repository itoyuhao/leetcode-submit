# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        
        for i in range(n-1):
            if nums[i-k+1] - nums[i-k] == 0:
                nums.pop(i-k)
                k += 1
        
        return n - k