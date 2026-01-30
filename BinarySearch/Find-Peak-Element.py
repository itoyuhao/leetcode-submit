# https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:  # 比到剩最後兩個再互相比較
            
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]: # 如果前後都比自己小 自己就是 peak 了
                return mid
            
            if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:  # 如果還是 ascending order 就往右走
                left = mid + 1
            else:
                right = mid # 如果不是ascending order( mid 可能是 valley 或 descending order ) 就往左走
            
        
        return right if nums[right] > nums[left] else left
                