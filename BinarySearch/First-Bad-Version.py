# https://leetcode.com/problems/first-bad-version/description/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n

        firstBad = 0

        while L <= R:
            M = (L + R) // 2
            if isBadVersion(M):
                firstBad = M
                R = M - 1
            else:
                L = M + 1
        
        return firstBad