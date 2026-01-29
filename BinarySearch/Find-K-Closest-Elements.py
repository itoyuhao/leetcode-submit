1# https://leetcode.com/problems/find-k-closest-elements/description/
2class Solution:
3    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
4        if len(arr) == k:
5            return arr
6
7        left, right = 0, len(arr) - k
8
9        while left < right:
10            mid = (left + right) // 2
11            if x - arr[mid] > arr[mid+k] - x:
12                left = mid + 1  # we don't need to retain mid because it would never be the answer.
13            else:
14                right = mid  # we need to retain mid because it may be the answer!
15            
16        
17        return arr[left: left + k]
18