1# https://leetcode.com/problems/sqrtx/editorial/
2class Solution:
3    def mySqrt(self, x: int) -> int:
4        # x is the target
5        
6        if x < 2:
7            return x
8
9        left, right = 2, x // 2
10
11        while left <= right:
12            pivot = (left + right) // 2
13            num = pivot * pivot
14            if num > x:
15                right = pivot - 1
16            elif num < x:
17                left = pivot + 1
18            else:
19                return pivot
20
21        return right