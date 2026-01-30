# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # how to use binary search?
        
        if len(numbers) == 2:
            return [1, 2]
        
        low, high = 0, len(numbers) - 1
        
        while low < high:
            
            sum = numbers[low] + numbers[high]
            
            if sum == target:
                return [low + 1, high + 1]
            
            elif sum > target:
                high -= 1
            
            else:
                low += 1
        
        return [low + 1, high + 1]