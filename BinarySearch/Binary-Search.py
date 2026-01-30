class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        while right - left >= 1:
            middle = (left + right) // 2
            
            if right - left == 1:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                return -1
            
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle
            else:
                right = middle
        
        return -1