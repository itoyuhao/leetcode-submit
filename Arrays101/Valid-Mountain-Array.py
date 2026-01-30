# https://leetcode.com/problems/valid-mountain-array/description/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if n < 3:
            return False
        
        increasing = True
        for i in range(n-1):
            if arr[i] == arr[i+1]:  # not strictly ordered
                return False
            if increasing and (arr[i+1] - arr[i] < 0):
                top = i #  record index of mountain top
                increasing = False
            if not increasing and (arr[i+1] - arr[i] > 0):
                return False
        
        
        return True if not increasing and top != 0 else False         