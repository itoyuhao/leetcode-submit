1# https://leetcode.com/problems/first-bad-version/description/
2# The isBadVersion API is already defined for you.
3# def isBadVersion(version: int) -> bool:
4
5class Solution:
6    def firstBadVersion(self, n: int) -> int:
7        L = 1
8        R = n
9
10        firstBad = 0
11
12        while L <= R:
13            M = (L + R) // 2
14            if isBadVersion(M):
15                firstBad = M
16                R = M - 1
17            else:
18                L = M + 1
19        
20        return firstBad