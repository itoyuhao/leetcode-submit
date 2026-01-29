1# https://leetcode.com/problems/valid-perfect-square/description/
2class Solution:
3    def isPerfectSquare(self, num: int) -> bool:
4        
5        left, right = 1, num
6        
7        while left <= right:
8            mid = (left + right) // 2
9            if mid * mid == num:
10                return True
11            elif mid * mid > num:
12                right = mid - 1
13            else:
14                left = mid + 1
15            
16        
17        return False