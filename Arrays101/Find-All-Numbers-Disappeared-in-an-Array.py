# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1]) 

        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        
        return res