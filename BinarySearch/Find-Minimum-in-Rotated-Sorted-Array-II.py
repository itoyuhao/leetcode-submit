# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            
            if nums[left] < nums[right]:  # not rotated array: return the most-left element
                return nums[left]
            
            mid = (left + right) // 2
            
            # rotated array: fold and choose one side
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:  # the key is the determination when left == right
                right -= 1  
                left += 1
            else:
                right = mid
        
        return min(nums[left], nums[right])