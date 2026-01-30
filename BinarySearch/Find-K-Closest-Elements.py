# https://leetcode.com/problems/find-k-closest-elements/description/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1  # we don't need to retain mid because it would never be the answer.
            else:
                right = mid  # we need to retain mid because it may be the answer!
            
        
        return arr[left: left + k]
