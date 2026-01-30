# https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        p = 0
        
        for i in range(n):
            if nums[i-p] == val:
                nums.pop(i-p)
                p += 1
        
        return n - p