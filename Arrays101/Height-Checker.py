# https://leetcode.com/problems/height-checker/description/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        origin = heights.copy()
        n = len(heights)
        # bubble sort
        for i in range(n-1):
            for j in range(n-i-1):
                if heights[j] > heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        
        mismatch = 0
        for i in range(n):
            if origin[i] != heights[i]:
                mismatch += 1
        
        return mismatch