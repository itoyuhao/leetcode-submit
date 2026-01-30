# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # edge case: no characters in letters that is lexicographically greater than target
        if target >= letters[-1]:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            
            elif letters[mid] > target:
                right = mid
        
        
        return letters[left] if letters[left] > target else letters[right]